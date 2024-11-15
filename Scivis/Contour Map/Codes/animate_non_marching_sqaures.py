# animate_non_marching_sqaures.py

import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# Function to create an animated plot
def create_animation(filepath, selected_attribute, dates, cmap, number_of_levels, min_val, max_val, colorbar_title, plot_title, save_path):
    
    ds = xr.open_dataset(filepath)   # Opening the dataset
    
    fig, ax = plt.subplots(figsize=(12, 6))   # Create a figure and axes for plotting
    
    def update_frame(date):  # Generate frames for each date
        ax.clear()
        contour = create_contour(ds, selected_attribute, date, cmap, number_of_levels, min_val, max_val, ax, plot_title)
        if len(fig.get_axes()) == 1:            # Checking if colorbar exists
            fig.colorbar(contour, ax=ax, label=colorbar_title)
    
    ani = animation.FuncAnimation(fig, update_frame, frames=dates, repeat=True)
    
    # Save as GIF
    ani.save(save_path, writer='pillow', fps=1)  # Adjust fps if needed
    
    print(f"Animation saved as {save_path}")
    
    
    
# create contour create the contour line
def create_contour(ds, selected_attribute, date, cmap, number_of_levels, min_val, max_val, ax, plot_title):
    lats = ds['lat'][:] # Extract latitude
    lons = ds['lon'][:] # Extract longitutde
    subset = ds[selected_attribute].sel(day=date) # to select dates
    
    ax.clear() # Clear the previous plot in the animation loop
    
    # Define custom contour levels using linspace for better control
    levels = np.linspace(min_val, max_val, number_of_levels)   
    
    # Plotting the contour lines
    contour = ax.contourf(lons, lats, subset, levels=levels, cmap=cmap, vmin=min_val, vmax=max_val)
    
    # Customize the plot (axis labels, title, colorbar)
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.set_title(f'{plot_title} {date}')
    ax.set_xticks([-120, -110, -100, -90, -80, -70])
    ax.set_xticklabels([f'{abs(x)}°W' for x in [-120, -110, -100, -90, -80, -70]])
    ax.set_yticks([30, 35, 40, 45])
    ax.set_yticklabels([f'{y}°N' for y in [30, 35, 40, 45]])

    # Return the contour for the colorbar
    return contour


########################################################################################
# This function can take values such as : 
#   1)  number_of_levels : number of contour lines 
#   2)  cmap : colormap to be used
#   3)  dates : the range of dates over which we wish to see the animation for
#   4)  min_val : min value of selected attributes across all dates for the colorbar
#   5)  max_val : max value of selected attributes across all dates for the colorbar
#   6)  plot_title
#   7)  colorbar_title
#   8)  selected_attribute
#   9)  filepath : the dataset path
#   10) save_path : the location at which we wish to save the GIF


#########################################################################################
# I have shown the particular case of gif over the dates as mentioned in selected_dates for both precipitation and wind speed
# with 'plasma' and 'viridis' colormaps for 10 contour levels 


selected_dates = ['2005-08-25','2005-08-27', '2005-08-28', '2005-08-29', '2005-08-30', '2005-08-31', '2005-09-01']

# calling the function for wind speed
create_animation(
    filepath='vs_2005.nc',
    selected_attribute = "wind_speed",
    dates=selected_dates,
    cmap='plasma',    
    number_of_levels = 10,
    min_val=0.4,
    max_val=19.700000000000003,
    plot_title = "Wind Speed on",
    colorbar_title = "Wind Speed (m/s)",
    save_path="Wind Speed1 (10 levels).gif"
)

# calling the function for wind speed
create_animation(
    filepath='vs_2005.nc',
    selected_attribute = "wind_speed",
    dates=selected_dates,
    cmap='viridis',    
    number_of_levels = 5,
    min_val=0.4,
    max_val=19.700000000000003,
    plot_title = "Wind Speed on",
    colorbar_title = "Wind Speed (m/s)",
    save_path="Wind Speed2 (5 levels).gif"
)

# calling the function for precipitation
create_animation(
    filepath='pr_2005.nc',
    selected_attribute = "precipitation_amount",
    dates=selected_dates,
    cmap='plasma',    
    number_of_levels = 10,
    min_val=0.0,
    max_val=205.0,
    plot_title = "Precipitation on",
    colorbar_title = "Precipitation amount (m/s)",
    save_path="Precipitation1 (10 levels).gif"
)

# calling the function for precipitation
create_animation(
    filepath='pr_2005.nc',
    selected_attribute = "precipitation_amount",
    dates=selected_dates,
    cmap='viridis',    
    number_of_levels = 20,
    min_val=0.0,
    max_val=205.0,
    plot_title = "Precipitation on",
    colorbar_title = "Precipitation amount (m/s)",
    save_path="Precipitation2 (20 levels).gif"
)
