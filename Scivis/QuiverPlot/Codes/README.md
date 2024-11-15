# Wind Data Visualization

This project contains two Python scripts, `Final.py` and `Final_GIF.py`, that visualize wind speed and direction data. Each script loads data from `.nc` files, processes it, and generates visualizations to analyze wind patterns for specific dates in 2005.

## Scripts Overview

1. **Final.py** - Generates static wind direction and speed plots for specific days and displays them individually.
2. **Final_GIF.py** - Creates animated GIFs showing wind speed and direction for specific days, displaying and saving each GIF after generation.


## Prerequisites

Make sure you have the following dependencies installed before running the scripts:

- `numpy`
- `matplotlib`
- `xarray`
- `cartopy`
- `imageio` (only for `Final_GIF.py`)
- `IPython` (only for `Final_GIF.py` for displaying GIFs in a Jupyter environment)
- `os`

You can install these libraries using pip:
```bash
pip install numpy matplotlib xarray cartopy imageio ipython os
```


## Dataset Requirements

Both scripts require wind data in `.nc` format:
- `vs_2005.nc`: Contains wind speed data.
- `th_2005.nc`: Contains wind direction data.

Ensure both files are located in the same directory as the scripts.



## Scripts Description

### 1. Final.py

**Purpose**: This script generates static wind speed and direction visualizations for a set of selected dates and displays them individually.

**How It Works**:
- Loads wind speed (`vs_2005.nc`) and wind direction (`th_2005.nc`) data.
- Processes wind data for the following days: `2005-07-15`, `2005-08-25`, `2005-08-27`, `2005-08-28`, `2005-08-29`, `2005-08-30`, `2005-08-31`, `2005-09-01`, `2005-09-15`.
- For each selected day:
  - Calculates U and V components of the wind vectors.
  - Creates a quiver plot displaying wind direction and speed on a map.
  - Displays the plot with coastlines, borders, and a color bar indicating wind speed.

**Usage**:
```bash
python Final.py
```

This script will display each wind plot in a pop-up window. Each plot corresponds to a specific date listed above.

### 2. Final_GIF.py

**Purpose**: This script generates animated GIFs for wind speed and direction on specific dates, displaying each GIF and saving it as a `.gif` file.

**How It Works**:
- Loads wind speed (`vs_2005.nc`) and wind direction (`th_2005.nc`) data.
- Processes wind data for the following days: `2005-07-15`, `2005-08-25`, `2005-08-27`, `2005-08-28`, `2005-08-29`, `2005-08-30`, `2005-08-31`, `2005-09-01`, `2005-09-15`.
- For each selected day:
  - Calculates U and V components of the wind vectors.
  - Saves each plot as a PNG image in a temporary folder.
  - Combines saved images into an animated GIF with a 3-second duration.
  - Displays each GIF inline (if running in Jupyter) and saves it with the filename format `wind_speed_direction_<date>.gif`.
- Deletes temporary PNG images after each GIF is created.

**Usage**:
```bash
python Final_GIF.py
```

After running the script, each GIF will display in-line (for Jupyter environments) and will be saved to the working directory with the format `wind_speed_direction_<date>.gif`.



## Example Output

1. **Final.py** - Displays a static map for each date, showing wind speed and direction.
2. **Final_GIF.py** - Saves and displays animated GIFs with wind speed and direction.



## Notes
- **Running Environment**: `Final_GIF.py` is optimized for Jupyter Notebook or compatible environments due to inline GIF display functionality. In other environments, the saved GIF files can be viewed manually.
- **Map Projection**: Both scripts use the `ccrs.PlateCarree()` projection to ensure accurate geographical representation.
- **Data Sampling**: To avoid overcrowding in plots, data is downsampled (sampling every 30th latitude and every 40th longitude).
- **Seasonal Trends**: I have chosen `2005-07-15` and `2005-09-15`, which were not selected in the contour and color mapping, to highlight seasonal wind trends in the Gulf area, in addition to the focus on hurricane patterns.
