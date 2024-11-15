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
from plot_colorscale import plot_variable_continuous


# For all the sampled days ,precipitation_amount variable 
day_indices =[236, 238, 239, 240, 241, 242,243]
for day_index in day_indices:
    plot_variable_continuous('pr_2005.nc', 'precipitation_amount', day_index,units="mm")

# For all sampled days ,wind_speed variable
day_indices = [236, 238, 239, 240, 241, 242,243]
for day_index in day_indices:
    plot_variable_continuous('vs_2005.nc', 'wind_speed', day_index,units="m/s")