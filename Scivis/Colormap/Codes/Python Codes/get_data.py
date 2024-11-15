import numpy as np
from netCDF4 import Dataset
from global_max_min import calculate_global_min_max
import os

def get_data(filename, var_name, day_index):
    current_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(current_dir, filename)
    data = Dataset(file_path, 'r')
    lats = data.variables['lat'][:]
    lons = data.variables['lon'][:]
    variable_data = data.variables[var_name][:]
    
    vmin, vmax = calculate_global_min_max(file_path, var_name)
    day_data = variable_data[day_index, :, :]
    
    data.close()
    return lons, lats, day_data, vmin, vmax
