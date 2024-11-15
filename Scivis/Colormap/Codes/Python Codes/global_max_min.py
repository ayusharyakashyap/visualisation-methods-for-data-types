import numpy as np
from netCDF4 import Dataset

def calculate_global_min_max(filename, var_name):
    data = Dataset(filename, 'r')
    variable_data = data.variables[var_name][:]
    day_indices = [236, 238, 239, 240, 241, 242, 243]
    
    global_min = np.inf
    global_max = -np.inf
    
    for index in day_indices:
        day_data = variable_data[index, :, :]
        
        day_min = np.min(day_data[day_data > 0]) if np.any(day_data > 0) else global_min
        day_max = np.max(day_data)
        
        global_min = min(global_min, day_min)
        global_max = max(global_max, day_max)
    
    data.close()
    return global_min, global_max
