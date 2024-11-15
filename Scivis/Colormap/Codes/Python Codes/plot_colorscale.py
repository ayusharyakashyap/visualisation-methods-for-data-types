import os
from netCDF4 import Dataset
from get_data import get_data
from get_day import get_date
from global_max_min import calculate_global_min_max
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from netCDF4 import Dataset
import matplotlib as mpl
import numpy.ma as ma
import matplotlib.colors as mcolors
from matplotlib.animation import FuncAnimation
from scipy.ndimage import maximum_filter, minimum_filter

#This function creates plot using continuous scale
def plot_variable_continuous(filename, var_name, day_index, units):

    lons, lats, day_data, vmin, vmax = get_data(filename, var_name, day_index)

    lon, lat =np.meshgrid(lons, lats)

    fig, ax =plt.subplots(figsize=(16, 8))
    cmap=plt.get_cmap('viridis')

    pcm = ax.pcolormesh(lon, lat, day_data, shading='auto', cmap=cmap, vmin=vmin, vmax=vmax)

    cbar = fig.colorbar(pcm, ax=ax, orientation='vertical')
    cbar.set_label(f'{var_name} Amount {units}')

    date = get_date(day_index)
    ax.set_title(f'{var_name} on {date}')

    ax.set_xticks([-120, -110, -100, -90, -80, -70])
    ax.set_xticklabels([f'{abs(x)}°W' for x in [-120, -110, -100, -90, -80, -70]])
    ax.set_yticks([30, 35, 40, 45])
    ax.set_yticklabels([f'{y}°N' for y in [30, 35, 40, 45]])

    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    
    plt.show()
    plt.savefig('continuous.png')


#This function creates plot using discrete scale
def plot_variable_discrete(filename, var_name, day_index,units):
    lons, lats, day_data, vmin, vmax = get_data(filename, var_name, day_index)
    lon, lat = np.meshgrid(lons, lats)
    
    fig, ax = plt.subplots(figsize=(16, 8))

   
    colors = plt.get_cmap('viridis', 9).colors.tolist()  
    colors.append((1.0, 0.0, 0.0))  
    d_cmap = mcolors.ListedColormap(colors)  
    
    pcm = ax.pcolormesh(lon, lat, day_data, shading='auto', cmap=d_cmap, vmin=vmin, vmax=vmax)
    
    cbar = fig.colorbar(pcm, ax=ax, orientation='vertical')
    cbar.set_label(f'{var_name} Amount {units}')

    date=get_date(day_index)
    ax.set_xticks([-120, -110, -100, -90, -80, -70])
    ax.set_xticklabels([f'{abs(x)}°W' for x in [-120, -110, -100, -90, -80, -70]])
    ax.set_yticks([30, 35, 40, 45])
    ax.set_yticklabels([f'{y}°N' for y in [30, 35, 40, 45]])

    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.set_title(f'{var_name} on {date}')

    plt.show()
    plt.savefig('discrete.png')
  
#This function creates plot using logarithmic scale 
def plot_variable_log(filename, var_name, day_index):

    lons, lats, day_data, vmin, vmax = get_data(filename, var_name, day_index)
    lon, lat = np.meshgrid(lons, lats)
    
    min_positive_value = np.min(day_data[day_data > 0])


    day_data_adjusted = np.where(day_data > 0, day_data, min_positive_value)


    day_data_masked = ma.masked_where(day_data < 0, day_data_adjusted)


    fig, ax = plt.subplots(figsize=(16, 8))
    cmap = plt.get_cmap('viridis')  
    cmap.set_bad(color='white') 

    
    pcm = ax.pcolormesh(lon, lat, day_data_masked, shading='auto', cmap=cmap,
                        norm=LogNorm(vmin=min_positive_value, vmax=day_data_masked.max()))

    
    cbar = fig.colorbar(pcm, ax=ax, orientation='vertical')
    cbar.set_label(f'{var_name} Amount (log scale)')

    date=get_date(day_index)
    ax.set_xticks([-120, -110, -100, -90, -80, -70])
    ax.set_xticklabels([f'{abs(x)}°W' for x in [-120, -110, -100, -90, -80, -70]])
    ax.set_yticks([30, 35, 40, 45])
    ax.set_yticklabels([f'{y}°N' for y in [30, 35, 40, 45]])

    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.set_title(f'{var_name} on {date}')

    plt.show()
    plt.savefig('logarithmic.png')
    

plot_variable_continuous('pr_2005.nc', 'precipitation_amount', day_index=240, units="mm")
plot_variable_discrete('pr_2005.nc', 'precipitation_amount', day_index=240, units="mm")
plot_variable_log('pr_2005.nc', 'precipitation_amount', day_index=240)