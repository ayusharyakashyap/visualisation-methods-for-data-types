import os
from netCDF4 import Dataset
from get_data import get_data
from get_day import get_date
from global_max_min import calculate_global_min_max
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

def create_animation(file_name, variable_name, output_file, units):
    
    current_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(current_dir, file_name)
    
    data = Dataset(file_path)
    lats = data.variables['lat'][:]
    lons = data.variables['lon'][:]
    variable_data = data.variables[variable_name][:]
    data.close()
    
    lon, lat = np.meshgrid(lons, lats)
    vmin, vmax = calculate_global_min_max(file_path, variable_name)
    
    fig, ax = plt.subplots(figsize=(10, 6))

    # We can try out using different colormaps by changing the cmap variable
    cmap = plt.get_cmap('viridis')
    pcm = ax.pcolormesh(lons, lats, np.zeros_like(variable_data[0, :, :]),
                        shading='auto', cmap=cmap, vmin=vmin, vmax=vmax)
    cbar = fig.colorbar(pcm, ax=ax, orientation='vertical', pad=0.02)
    cbar.set_label(f'{variable_name} {units}')
    
    ax.set_xticks([-120, -110, -100, -90, -80, -70])
    ax.set_xticklabels([f'{abs(x)}°W' for x in [-120, -110, -100, -90, -80, -70]])
    ax.set_yticks([30, 35, 40, 45])
    ax.set_yticklabels([f'{y}°N' for y in [30, 35, 40, 45]])

    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    day_indices = [236, 238, 239, 240, 241, 242, 243]
    
    def update(day_index):
        date = get_date(day_index)
        ax.set_title(f'{variable_name} on {date}')
        day_data = variable_data[day_index, :, :]
        pcm.set_array(day_data.ravel())
    
    ani = FuncAnimation(fig, update, frames=day_indices, interval=1000, repeat=True)

  
    if not output_file.endswith('.gif'):
        output_file+='.gif'

    ani.save(output_file, writer='pillow', fps=1)
    print(f"saved as {output_file}")
    plt.close(fig)

create_animation('pr_2005.nc', 'precipitation_amount', 'finalprecipitation_animation.gif', units="mm")
create_animation('vs_2005.nc', 'wind_speed', 'finalwind_animation.gif', units="m/s")
