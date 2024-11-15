# global_min_max_values.py

# code which finds out the max and min values of parameters like : precipitation_amount , wind_speed for selected dates

import xarray as xr

def find_global_max_min(dataset_path, selected_dates, selected_attribute):
    ds = xr.open_dataset(dataset_path) # open the dataset
    selected_subset = ds[selected_attribute].sel(day=selected_dates) # find the subset for selected dates
    
    min_val = float(selected_subset.min())
    max_val = float(selected_subset.max())
    
    print(f'Global {selected_attribute} Min : {min_val}')
    print(f'Global {selected_attribute} Max : {max_val}')

# these are the selected dates for the plotting of the contour maps
selected_dates = ['2005-07-15','2005-08-27', '2005-08-28', '2005-08-29', '2005-08-30', '2005-08-31', '2005-09-15']

find_global_max_min("vs_2005.nc", selected_dates, "wind_speed")
find_global_max_min("pr_2005.nc", selected_dates, "precipitation_amount")





### output : 
# Global wind_speed Min : 0.4
# Global wind_speed Max : 19.700000000000003
# Global precipitation_amount Min : 0.0
# Global precipitation_amount Max : 205.0