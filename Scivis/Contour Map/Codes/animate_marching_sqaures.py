# animate_marching_sqaures.py

# to create the animated GIFs for showing contour maps made using marching sqaures algorithm to show contour lines.
# i have used matplotlib.animation for this with 1 fps

import xarray as xr
import numpy as np
import matplotlib.pyplot as pltc
import matplotlib.animation as animation
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# Define the animation function
def create_animation(filepath, selected_attribute, dates, cmap, min_val, max_val, number_of_levels, line_width, plot_title, colorbar_title, save_path):
 
    ds = xr.open_dataset(filepath) # opening the dataset
   
    fig, ax = plt.subplots(figsize=(16, 12), subplot_kw={'projection': ccrs.PlateCarree()})  # Set up the plot with a PlateCarree projection

    # Initial contour lines to avoid multiple colorbars
    levels = np.linspace(min_val, max_val, number_of_levels)
    lats = ds['lat'][:]  # extract latitude
    lons = ds['lon'][:]  # extract longitude
    wind_speed = ds[selected_attribute].sel(day=dates[0])
    contour_lines = ax.contour(lons, lats, wind_speed, levels=levels, cmap=cmap, transform=ccrs.PlateCarree(), linewidths=line_width)

    # Create a single colorbar
    cbar = fig.colorbar(contour_lines, ax=ax, shrink=0.60, aspect=15)
    cbar.set_label(colorbar_title, fontsize=12)
    cbar.ax.tick_params(width=1)

    # Add map features
    ax.add_feature(cfeature.COASTLINE, edgecolor='black')
    ax.add_feature(cfeature.BORDERS, edgecolor='black')
    ax.add_feature(cfeature.LAND, facecolor='lightgray')
    ax.add_feature(cfeature.OCEAN, facecolor='aliceblue')

    # Set axis labels and tick marks
    ax.set_xlabel("Longitude", fontsize=11, labelpad=6)
    ax.set_ylabel("Latitude", fontsize=11, labelpad=6)
    ax.set_xticks([-120, -110, -100, -90, -80, -70], crs=ccrs.PlateCarree())
    ax.set_xticklabels([f'{abs(x)}°W' for x in [-120, -110, -100, -90, -80, -70]])
    ax.set_yticks([30, 35, 40, 45], crs=ccrs.PlateCarree())
    ax.set_yticklabels([f'{y}°N' for y in [30, 35, 40, 45]])

    # Function to update each frame
    def update_frame(date):
        nonlocal contour_lines
        contour_lines = create_contour_lines(ds,selected_attribute, date, cmap, min_val, max_val,  number_of_levels, line_width, ax, contour_lines,plot_title)

    # Create the animation
    ani = animation.FuncAnimation(fig, update_frame, frames=dates, repeat=True)

    # Save the animation as a GIF
    ani.save(save_path, writer='pillow', fps=1)  # Adjust fps as needed
    print(f"Animation saved as {save_path}")

# Define the function to create a contour line plot for a single frame
def create_contour_lines(ds,selected_attribute,  date, cmap, min_val, max_val,  number_of_levels, line_width, ax, contour_lines,plot_title):
    lats = ds['lat'][:]
    lons = ds['lon'][:]
    wind_speed = ds[selected_attribute].sel(day=date)

    # Remove previous contour lines
    for coll in contour_lines.collections:
        coll.remove()

    # Define contour levels and plot contour lines
    levels = np.linspace(min_val, max_val,  number_of_levels)
    contour_lines = ax.contour(lons, lats, wind_speed, levels=levels, cmap=cmap, transform=ccrs.PlateCarree(), linewidths=line_width)

    # Update the title with the current date
    ax.set_title(f'{plot_title} {date}', fontsize=13)

    return contour_lines





# selected dates for visualization
dates = ['2005-08-25', '2005-08-27', '2005-08-28', '2005-08-29', '2005-08-30', '2005-08-31', '2005-09-01']


#######################################################################
# I have shown the implementation for 3 different animations :
# Used 'viridis' colormap for each
# Shown this for wind speed and not for precipitation

# 1. WS_marching_sqaures1 (10 levels, width 1)  -> 10 levels, line width 1 
# 2. WS_marching_sqaures1 (10 levels, width 2)  -> 10 levels, line width 2
# 3. WS_marching_sqaures1 (25 levels, width 0.5) -> 25 levels, line width 0.5

#######################################################################

create_animation(
    filepath='vs_2005.nc',
    selected_attribute = "wind_speed",
    dates=dates,
    cmap='viridis',    
    min_val=0.4,         
    max_val=19.700000000000003,      
    number_of_levels=10,        
    line_width=1,  
    plot_title = "Wind Speed on",
    colorbar_title = "Wind Speed (m/s)",
    save_path="WS_marching_sqaures1 (10 levels, width 1).gif"
)

create_animation(
    filepath='vs_2005.nc',
    selected_attribute = "wind_speed",
    dates=dates,
    cmap='viridis',    
    min_val=0.4,         
    max_val=19.700000000000003,      
    number_of_levels=10,        
    line_width=2,  
    plot_title = "Wind Speed on",
    colorbar_title = "Wind Speed (m/s)",
    save_path="WS_marching_sqaures1 (10 levels, width 2).gif"
)

create_animation(
    filepath='vs_2005.nc',
    selected_attribute = "wind_speed",
    dates=dates,
    cmap='viridis',    
    min_val=0.4,         
    max_val=19.700000000000003,      
    number_of_levels=25,        
    line_width=0.5,  
    plot_title = "Wind Speed on",
    colorbar_title = "Wind Speed (m/s)",
    save_path="WS_marching_sqaures1 (25 levels, width 0.5).gif"
)