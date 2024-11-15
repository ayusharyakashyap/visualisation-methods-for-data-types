# marching_sqaures.py

# for plotting contour plots using marching sqaures while chanhing parameters like : 
# 1. number of contour lines
# 2. colormap
# 3. line width

import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

def plot_contour_lines(filepath, selected_attribute, date, cmap, min_val, max_val, number_of_levels, line_width):
    
    # Open the dataset and extract data
    ds = xr.open_dataset(filepath)
    lats = ds['lat'][:]
    lons = ds['lon'][:]
    wind_speed = ds[selected_attribute].sel(day=date)

    # Set up the plot with a PlateCarree projection
    fig, ax = plt.subplots(figsize=(16,12), subplot_kw={'projection': ccrs.PlateCarree()})

    # Define contour levels and plot contour lines
    levels = np.linspace(min_val, max_val, number_of_levels)
    
    contour_lines = ax.contour(lons, lats, wind_speed, levels=levels, cmap=cmap, transform=ccrs.PlateCarree(), linewidths=line_width)
    cbar = plt.colorbar(contour_lines, ax=ax, label='Wind Speed (m/s)', shrink=0.55, aspect=15)
    cbar.set_label('Wind Speed (m/s)', fontsize=12)  # Set colorbar label size
    
    cbar.ax.tick_params(width=1)  # Set the tick line width (e.g., to 2)

    # Add map features (coastlines, borders, land, ocean)
    ax.add_feature(cfeature.COASTLINE, edgecolor='black')
    ax.add_feature(cfeature.BORDERS, edgecolor='black')
    ax.add_feature(cfeature.LAND, facecolor='lightgray')
    ax.add_feature(cfeature.OCEAN, facecolor='aliceblue')

    # Set axis labels and title
    ax.set_xlabel("Longitude", fontsize=11, labelpad=6)
    ax.set_ylabel("Latitude", fontsize=11, labelpad=6)
    ax.set_title(f'Wind Speed on {date}', fontsize=13)

    # Set latitude and longitude ticks
    ax.set_xticks([-120, -110, -100, -90, -80, -70])
    ax.set_xticklabels([f'{abs(x)}°W' for x in [-120, -110, -100, -90, -80, -70]])
    ax.set_yticks([30, 35, 40, 45])
    ax.set_yticklabels([f'{y}°N' for y in [30, 35, 40, 45]])

    # Adjust the subplot layout to reduce padding
    plt.tight_layout()  # Ensures minimum padding around the plot
    
    # Fine-tune the padding further if needed
    fig.subplots_adjust(left=0.05, right=0.75, top=0.65, bottom=0.05)  # Adjusts padding to your needs

    plt.show()
  
  
  
  
  
  
    
#  min and max wind speed values already calculated using the code in : "global_min_max_values.py" with vs_2005.nc dataset for selected dates
vs_min = 0.4
vs_max = 19.700000000000003

#  min and max precipitation values already calculated using the code in : "global_min_max_values.py" with vs_2005.nc dataset for selected dates
min_val = vs_min
max_val = vs_max



############################################################################################

# i experimented with different values for number of contour levels, colormap and line width 
# These examples have been done only for wind_speed on a particular day

# for 5 contour levels , plasma colormap and line width 1 
plot_contour_lines(
    filepath = "vs_2005.nc",
    selected_attribute = "wind_speed",
    date = "2005-08-29",
    cmap = "plasma",
    min_val = vs_min,
    max_val = vs_max,
    number_of_levels = 5,
    line_width = 1
)

# for 10 contour levels , plasma colormap and line width 0.5
plot_contour_lines(
    filepath = "vs_2005.nc",
    selected_attribute = "wind_speed",
    date = "2005-08-29",
    cmap = "viridis",
    min_val = vs_min,
    max_val = vs_max,
    number_of_levels = 10,
    line_width = 0.5
)

# for 10 contour levels , plasma colormap and line width 1 
plot_contour_lines(
    filepath = "vs_2005.nc",
    selected_attribute = "wind_speed",
    date = "2005-08-29",
    cmap = "viridis",
    min_val = vs_min,
    max_val = vs_max,
    number_of_levels = 10,
    line_width = 1
)

# for 10 contour levels , plasma colormap and line width 1 
plot_contour_lines(
    filepath = "vs_2005.nc",
    selected_attribute = "wind_speed",
    date = "2005-08-29",
    cmap = "viridis",
    min_val = vs_min,
    max_val = vs_max,
    number_of_levels = 10,
    line_width = 1
)

# for 25 contour levels , plasma colormap and line width 0.5 
plot_contour_lines(
    filepath = "vs_2005.nc",
    selected_attribute = "wind_speed",
    date = "2005-08-29",
    cmap = "jet",
    min_val = vs_min,
    max_val = vs_max,
    number_of_levels = 25,
    line_width = 0.5
)

############################################################################################


