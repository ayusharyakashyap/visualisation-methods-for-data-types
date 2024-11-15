import os
from netCDF4 import Dataset
from get_data import get_data
from get_day import get_date
from global_max_min import calculate_global_min_max
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm
import matplotlib.colors as mcolors
import numpy.ma as ma
from matplotlib.animation import FuncAnimation
from scipy.ndimage import maximum_filter, minimum_filter


def plot_div_seq(filename, var_name, day_index, colormaps, units):
    lons, lats, day_data, vmin, vmax = get_data(filename, var_name, day_index)
    
    lon, lat = np.meshgrid(lons, lats)
    
    for cmap_name in colormaps:
        fig, ax = plt.subplots(figsize=(16, 8))
        cmap = plt.get_cmap(cmap_name)  

        pcm = ax.pcolormesh(lon, lat, day_data, shading='auto', cmap=cmap, vmin=vmin, vmax=vmax)

        cbar = fig.colorbar(pcm, ax=ax, orientation='vertical')
        cbar.set_label(f'{var_name} Amount {units}')

        date = get_date(day_index)
        ax.set_xticks([-120, -110, -100, -90, -80, -70])
        ax.set_xticklabels([f'{abs(x)}°W' for x in [-120, -110, -100, -90, -80, -70]])
        ax.set_yticks([30, 35, 40, 45])
        ax.set_yticklabels([f'{y}°N' for y in [30, 35, 40, 45]])

        ax.set_xlabel('Longitude')
        ax.set_ylabel('Latitude')
        ax.set_title(f'{var_name} on {date} - Colormap: {cmap_name}')
        
        plt.show()

# Trying out different divergent colormap
plot_div_seq('vs_2005.nc', 'wind_speed', day_index=240, colormaps=['bwr', 'coolwarm', 'seismic', 'BrBG'], units="m/s")

# Trying out different sequential colormaps
plot_div_seq('vs_2005.nc', 'wind_speed', day_index=240, colormaps=['Blues', 'viridis', 'YlGnBu', 'cividis', 'inferno'], units="m/s")
