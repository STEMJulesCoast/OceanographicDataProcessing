from scipy.stats import linregress
import xarray as xr
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.ticker as mticker



def calc_trend(y):
    """
    Calculates the linear trend (slope) for a time series.
    Multiplies the slope by 10 to convert from Unit/year to Unit/decade.
    """
    # Assuming y is a numpy array with no missing values, evenly spaced in time (e.g. monthly data)
    x = np.arange(len(y))
    # Apply linear regression
    slope = linregress(x, y).slope
    # Multiply by 120 to convert from per year to per decade
    return slope * 120

def calculate_trend_per_decade(data):
    """
    Apply the calc_trend function to each grid cell to calculate trend per decade.
    
    Parameters:
    - data: xarray.DataArray with variable values.
    
    Returns:
    - trend_decade: xarray.DataArray with variable trend per decade for each grid cell.
    """
    trend_decade = xr.apply_ufunc(
        calc_trend,
        data,
        vectorize=True,
        input_core_dims=[['time']],  # Time is the core dimension
        dask='allowed'  # Allow Dask for parallel computation
    )
    return trend_decade



def plot_trend(trend_decade, vmin=-0.5, vmax=0.5):
    """
    Plot the trend per grid cell using xarray and matplotlib (no Basemap).
    
    Parameters:
    - trend_decade: xarray.DataArray with SST trend per decade.
    - vmin: Minimum value for colorbar (default is -0.5).
    - vmax: Maximum value for colorbar (default is 0.5).
    """
    # Create symmetrical contour levels centered around zero
    trend_levels = MaxNLocator(nbins=21).tick_values(vmin, vmax)

    # Create a figure for the plot
    fig, ax = plt.subplots(figsize=(12, 7))

    # Plot the trend data using xarray's built-in plotting method
    cf = trend_decade.plot.contourf(ax=ax, levels=trend_levels, cmap='RdBu_r', vmin=vmin, vmax=vmax, 
                                    extend='neither', cbar_kwargs={'label': '°C/decade'})


    # Set titles and labels
    plt.title('Trend of SST per Grid Cell per Decade (°C/decade)')
    
    # Adjust layout for better readability
    plt.tight_layout()
    #plt.savefig("trend.png", transparent=True)
    # Show the plot
    plt.show()


def adjust_longitude(data_array, central_lon):
    """
    Adjusts the longitude to center around 180°.
    """
    if central_lon not in [0, 180]:
        raise ValueError("central_lon must be either 0 or 180.")
    
    data_array = data_array.copy()  # Create a copy to avoid modifying the original data
    lon = data_array['lon']

    if central_lon == 0 and float(lon.max()) > 180:
        data_array = data_array.assign_coords(lon=((lon + 180) % 360) - 180).sortby('lon')
    elif central_lon == 180 and float(lon.min()) < 0:
        data_array = data_array.assign_coords(lon=((lon % 360 + 360) % 360)).sortby('lon')
    return data_array

def plot_trend_cartopy(trend_decade, vmin=-0.5, vmax=0.5, variable='SST', label='°C', central_lon=0):
    """
    Plot trend per decade with Cartopy (no Basemap).

    Parameters
    ----------
    trend_decade : xarray.DataArray
        Grid of trends per decade (same units as input variable).
    vmin, vmax : float
        Color limits (use symmetric around 0 for anomalies/trends).
    variable : str
        Variable name for title.
    label : str
        Units label (e.g., '°C').
    central_lon : int
        0 -> center at Greenwich (lon in -180..180), 180 -> Pacific centered.
    """
    # recentre longitudes if needed
    td = adjust_longitude(trend_decade, central_lon=central_lon)

    # symmetric levels around zero
    maxabs = max(abs(vmin), abs(vmax))
    vmin, vmax = -maxabs, maxabs
    levels = MaxNLocator(nbins=21).tick_values(vmin, vmax)

    proj = ccrs.Robinson(central_longitude=central_lon)
    fig, ax = plt.subplots(figsize=(12, 7), subplot_kw={'projection': proj})

    # map context
    ax.add_feature(cfeature.LAND, facecolor='white')
    ax.coastlines(resolution='110m', linewidth=0.8)
    ax.add_feature(cfeature.BORDERS, linewidth=0.5, edgecolor='gray')

    # gridlines (labels off to avoid duplication in Robinson)
    gl = ax.gridlines(draw_labels=True, linestyle='--', color='gray', linewidth=0.5, alpha=0.8)
    #gl.xlocator = mticker.FixedLocator(np.arange(-180, 181, 60))
    #gl.ylocator = mticker.FixedLocator(np.arange(-90,   91, 30))

    # filled contours
    p = td.plot.contourf(
        ax=ax,
        transform=ccrs.PlateCarree(),
        levels=levels,
        cmap='RdBu_r',
        vmin=vmin, vmax=vmax,
        add_colorbar=True,
        cbar_kwargs={'label': f'{label}/decade'}
    )

    # optional thin contour lines for structure
    td.plot.contour(
        ax=ax,
        transform=ccrs.PlateCarree(),
        levels=levels,
        colors='k',
        linewidths=0.25,
        add_colorbar=False
    )

    ax.set_title(f'Trend of {variable} per decade ({label}/decade)')
    plt.tight_layout()
    plt.show()