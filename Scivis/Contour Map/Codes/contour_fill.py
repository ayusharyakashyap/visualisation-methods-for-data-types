# contour_fill.py

# This code gives contour fill plots 
# certain attributes like number of contour levels, dates etc can be changed 

import xarray as xr
import numpy as np
import matplotlib.pyplot as plt

def create_contour(filepath, selected_attribute, date, cmap, number_of_levels, min_val, max_val, plot_title, colorbar_title):
    # Open the dataset
    ds = xr.open_dataset(filepath)
    
    # Extract latitude and longitude values from the dataset
    lats = ds['lat'][:]
    lons = ds['lon'][:]
    
    # Extract wind speed data for the specific date
    subset = ds[selected_attribute].sel(day=date)
    
    # Create a figure and axes object
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Adjust margins around the plot
    fig.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    
    # Define contour boundaries: 10 boundaries give 9 color bands
    contour_levels = np.linspace(min_val, max_val, number_of_levels)
    
    # Plot the filled contours
    contour = ax.contourf(lons, lats, subset, levels=contour_levels, cmap=cmap, vmin=min_val, vmax=max_val)
    
    # Add a colorbar
    cbar = plt.colorbar(contour, ax=ax, label=colorbar_title, ticks=contour_levels)
    
    # Customize axis labels and title
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.set_title(f'{plot_title} {date}')
    
    # Set tick labels for latitude and longitude
    ax.set_xticks([-120, -110, -100, -90, -80, -70])
    ax.set_xticklabels([f'{abs(x)}°W' for x in [-120, -110, -100, -90, -80, -70]])
    ax.set_yticks([30, 35, 40, 45])
    ax.set_yticklabels([f'{y}°N' for y in [30, 35, 40, 45]])
    
    # Ensure layout is neat
    fig.tight_layout()
    
    # Display the plot
    plt.show()

#  min and max wind speed values already calculated using the code in : "global_min_max_values.py" with vs_2005.nc dataset for selected dates
vs_min = 0.4
vs_max = 19.700000000000003

#  min and max precipitation values already calculated using the code in : "global_min_max_values.py" with vs_2005.nc dataset for selected dates
pr_min = 0.0
pr_max = 205.0


################################################################################################
# I have shown the implementation for 3 days :  28 , 29 and 39 th August  + 10 contour levels + viridis colormap 


# create_contour(
#     filepath='vs_2005.nc',
#     selected_attribute = "wind_speed",
#     date='2005-08-25',
#     cmap='viridis',    
#     number_of_levels = 10,
#     min_val=vs_min,
#     max_val=vs_max,
#     plot_title = "Wind Speed on",
#     colorbar_title = "Wind Speed (m/s)",
# )
# create_contour(
#     filepath='vs_2005.nc',
#     selected_attribute = "wind_speed",
#     date='2005-08-27',
#     cmap='viridis',    
#     number_of_levels = 10,
#     min_val=vs_min,
#     max_val=vs_max,
#     plot_title = "Wind Speed on",
#     colorbar_title = "Wind Speed (m/s)",
# )
create_contour(
    filepath='vs_2005.nc',
    selected_attribute = "wind_speed",
    date='2005-08-28',
    cmap='viridis',    
    number_of_levels = 10,
    min_val=vs_min,
    max_val=vs_max,
    plot_title = "Wind Speed on",
    colorbar_title = "Wind Speed (m/s)",
)
create_contour(
    filepath='vs_2005.nc',
    selected_attribute = "wind_speed",
    date='2005-08-29',
    cmap='viridis',    
    number_of_levels = 10,
    min_val=vs_min,
    max_val=vs_max,
    plot_title = "Wind Speed on",
    colorbar_title = "Wind Speed (m/s)",
)
create_contour(
    filepath='vs_2005.nc',
    selected_attribute = "wind_speed",
    date='2005-08-30',
    cmap='viridis',    
    number_of_levels = 10,
    min_val=vs_min,
    max_val=vs_max,
    plot_title = "Wind Speed on",
    colorbar_title = "Wind Speed (m/s)",
)
# create_contour(
#     filepath='vs_2005.nc',
#     selected_attribute = "wind_speed",
#     date='2005-08-31',
#     cmap='viridis',    
#     number_of_levels = 10,
#     min_val=vs_min,
#     max_val=vs_max,
#     plot_title = "Wind Speed on",
#     colorbar_title = "Wind Speed (m/s)",
# )
# create_contour(
#     filepath='vs_2005.nc',
#     selected_attribute = "wind_speed",
#     date='2005-09-01',
#     cmap='viridis',    
#     number_of_levels = 10,
#     min_val=vs_min,
#     max_val=vs_max,
#     plot_title = "Wind Speed on",
#     colorbar_title = "Wind Speed (m/s)",
# )

# ####

# create_contour(
#     filepath='pr_2005.nc',
#     selected_attribute = "precipitation_amount",
#     date='2005-08-25',
#     cmap='viridis',    
#     number_of_levels = 10,
#     min_val=pr_min,
#     max_val=pr_max,
#     plot_title = "Precipitation on",
#     colorbar_title = "Precipitation (mm)",
# )
# create_contour(
#     filepath='pr_2005.nc',
#     selected_attribute = "precipitation_amount",
#     date='2005-08-27',
#     cmap='viridis',    
#     number_of_levels = 10,
#     min_val=pr_min,
#     max_val=pr_max,
#     plot_title = "Precipitation on",
#     colorbar_title = "Precipitation (mm)",
# )
# create_contour(
#     filepath='pr_2005.nc',
#     selected_attribute = "precipitation_amount",
#     date='2005-08-28',
#     cmap='viridis',    
#     number_of_levels = 10,
#     min_val=pr_min,
#     max_val=pr_max,
#     plot_title = "Precipitation on",
#     colorbar_title = "Precipitation (mm)",
# )
# create_contour(
#     filepath='pr_2005.nc',
#     selected_attribute = "precipitation_amount",
#     date='2005-08-29',
#     cmap='viridis',    
#     number_of_levels = 10,
#     min_val=pr_min,
#     max_val=pr_max,
#     plot_title = "Precipitation on",
#     colorbar_title = "Precipitation (mm)",
# )
# create_contour(
#     filepath='pr_2005.nc',
#     selected_attribute = "precipitation_amount",
#     date='2005-08-30',
#     cmap='viridis',    
#     number_of_levels = 10,
#     min_val=pr_min,
#     max_val=pr_max,
#     plot_title = "Precipitation on",
#     colorbar_title = "Precipitation (mm)",
# )
# create_contour(
#     filepath='pr_2005.nc',
#     selected_attribute = "precipitation_amount",
#     date='2005-08-31',
#     cmap='viridis',    
#     number_of_levels = 10,
#     min_val=pr_min,
#     max_val=pr_max,
#     plot_title = "Precipitation on",
#     colorbar_title = "Precipitation (mm)",
# )
# create_contour(
#     filepath='pr_2005.nc',
#     selected_attribute = "precipitation_amount",
#     date='2005-09-01',
#     cmap='viridis',    
#     number_of_levels = 10,
#     min_val=pr_min,
#     max_val=pr_max,
#     plot_title = "Precipitation on",
#     colorbar_title = "Precipitation (mm)",
# )