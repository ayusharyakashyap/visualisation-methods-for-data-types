import numpy as np
import matplotlib.pyplot as plt
import xarray as xr
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# Load wind speed and direction data
vs_file_path = 'vs_2005.nc'
th_file_path = 'th_2005.nc'
vs_data = xr.open_dataset(vs_file_path)
th_data = xr.open_dataset(th_file_path)

# Define the days to plot
days_august = ["2005-07-15", "2005-08-25", "2005-08-27", "2005-08-28", "2005-08-29", 
               "2005-08-30", "2005-08-31", "2005-09-01", "2005-09-15"]
selected_days = days_august

# Extract data for selected days
vs_selected = vs_data.sel(day=selected_days)
th_selected = th_data.sel(day=selected_days)

for day in selected_days:
    # Create a figure for each day
    fig, ax = plt.subplots(figsize=(15, 10), subplot_kw={'projection': ccrs.PlateCarree()})
    
    # Get wind speed and direction
    wind_speed = vs_selected.wind_speed.sel(day=day)
    wind_direction = th_selected.wind_from_direction.sel(day=day)
    
    # Convert direction to radians and calculate U, V components
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

    plt.tight_layout()
    plt.show()  # Display plot
