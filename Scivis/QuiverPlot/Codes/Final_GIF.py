import numpy as np
import matplotlib.pyplot as plt
import xarray as xr
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import imageio
import os
from IPython.display import Image, display

# Load wind speed and direction data
vs_file_path = 'vs_2005.nc'
th_file_path = 'th_2005.nc'
vs_data = xr.open_dataset(vs_file_path)
th_data = xr.open_dataset(th_file_path)

# Days to plot
days = ["2005-08-25", "2005-08-27", "2005-08-28", "2005-08-29", 
        "2005-08-30", "2005-08-31", "2005-09-01"]

# Create a directory for images
output_dir = "temp_images"
os.makedirs(output_dir, exist_ok=True)

image_files = []

# Create frames for each day
for day in days:
    fig, ax = plt.subplots(figsize=(15, 10), subplot_kw={'projection': ccrs.PlateCarree()})
    
    # Get wind speed and direction for the day
    wind_speed = vs_data.wind_speed.sel(day=day)
    wind_direction = th_data.wind_from_direction.sel(day=day)
    
    # Convert direction to radians and calculate components
    theta = np.deg2rad(wind_direction)
    u = wind_speed * np.cos(theta)
    v = wind_speed * np.sin(theta)
    
    # Subset data for better visualization
    lon = wind_speed.lon[::40]
    lat = wind_speed.lat[::30]
    u = u[::30, ::40]
    v = v[::30, ::40]
    speed = wind_speed[::30, ::40]
    
    # Plot the quiver
    quiver = ax.quiver(lon, lat, u, v, speed, cmap='viridis', transform=ccrs.PlateCarree())
    ax.set_title(f"Wind Direction and Speed on {day}", fontsize=16)
    
    # Add map features
    ax.coastlines()
    ax.add_feature(cfeature.BORDERS, linestyle=':')
    
    # Add color bar
    cbar = plt.colorbar(quiver, ax=ax, orientation='vertical', pad=0.02)
    cbar.set_label("Wind Speed (m/s)", fontsize=14)

    # Save frame
    file_path = os.path.join(output_dir, f"frame_{day.replace('-', '_')}.png")
    plt.savefig(file_path, dpi=100)
    image_files.append(file_path)
    
    plt.close(fig)

# Create GIF from saved frames
gif_path = "wind_speed_direction_aug25_sep01_2005.gif"
with imageio.get_writer(gif_path, mode='I', duration=20.0) as writer:
    for filename in image_files:
        image = imageio.imread(filename)
        for _ in range(15):
            writer.append_data(image)

# Clean up images
for filename in image_files:
    os.remove(filename)
os.rmdir(output_dir)

# Display the GIF
display(Image(filename=gif_path))