
# Oceanographic Data Processing Course

Welcome to **Oceanographic Data Processing** — a hands-on introduction to working with oceanographic and climate datasets using Python.

The course is divided into two main parts, each focusing on different skills and applications.


## Course Structure:

### Part 1 - Fundamentals
Focus: data structures, visualization, and introduction to wind-driven dynamics.

- **Topic 1**: Introduction to Data Structures and Basic Visualization
- **Topic 2**: Working with Climate Data
- **Topic 3**: Functions, Modules and Introduction into Wind Driven Ocean Dynamics

### Part 2 - Applications
Focus: advanced analysis and dynamic processes.

- **Topic 4**: Analysis of Wind-Driven Ocean Dynamics: Ekman Transport and Vertical Motion
- **Topic 5**: Variability Analysis of 4D-Oceanographic Data 
- **Topic 6**: Frequency Patterns and Object-Oriented Programming – Introducing Fourier Transforms, Wavelets, and EOF Analysis

### Folder Structure:

- [**`/Modules`**](/Modules/): contains reusable Python modules
- [**`/Data`**](/Data/): datasets used in the course
- [**`/01_Fundamentals`**](/01_Fundamentals/): notebooks and materials for the first block (November 29). 
- [**`/02_Applications`**](/02_Applications/): notebooks and materials for the second block (January 10, 2026).


Each notebook contains exercises — some will be covered together, others you can complete independently.  
**Reading carefully is key:** most answers can be found by understanding the instructions.

### Setup Instructions:

1. Install [Python 3.13](https://www.python.org/downloads/release/python-3139/):  [Windows](https://www.python.org/ftp/python/3.13.9/python-3.13.9-amd64.exe) | [macOS](https://www.python.org/ftp/python/3.13.9/python-3.13.9-macos11.pkg)
    
    and [Visual Studio (VS) Code](https://code.visualstudio.com/download): [Windows](https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user) | [macOS](https://code.visualstudio.com/sha/download?build=stable&os=darwin-universal)

    Alternatively, use **Anaconda** (includes JupyterLab).  
3. Download this GitHub repository, unzip the folder, and make yourself familiar with the structure. 
4. Download the required datasets:
    - Download Wind Data (Copernicus Marine Service): [Wind Data](https://data.marine.copernicus.eu/product/WIND_GLO_PHY_CLIMATE_L4_MY_012_003/files?subdataset=cmems_obs-wind_glo_phy_my_l4_P1M_202411&path=WIND_GLO_PHY_CLIMATE_L4_MY_012_003%2Fcmems_obs-wind_glo_phy_my_l4_P1M_202411%2F2024%2F
    ) (12 files, one for each month of 2024) and store them in [`Data/Wind`](/Data/Wind/) directory.
5. Please note that we will be working with Jupyter Notebooks throughout the course, and during the first session, we will install the necessary libraries and set up the virtual environment together.

-----
#### System Tips (Mac) 

If you’re new to Python on macOS, follow [here](https://www.stuartellis.name/articles/mac-setup/). You may need to install XCode, Homebrew, and update your `.zshrc`.

---
#### Virtual Environment

FYI How to create a virtual environment and install the necessary libaries in Visual Studio Code

1. **Create a virtual environment** (optional, but recommended):
    ```bash
    python -m venv .venv
    ```

2. **Activate the virtual environment**:
   - **Windows**:
     ```bash
     .venv\Scripts\activate
     ```
   - **Linux**:
     ```bash
     source .venv/bin/activate
     ```

3. **Install the required libraries**:
    ```bash
    pip install -r requirements.txt
    ```

Normally, VS Code guides you through this process – you just need to open a notebook and click on 'Select Kernel' in the upper-right corner, then let the VS Code magic happen.

---

### Access the course via Binder

You can run all notebooks online without local installation:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/STEMJulesCoast/OceanographicDataProcessing/main?urlpath=%2Fdoc%2Ftree%2F%2F01_Fundamentals%2F01_DataStructures_and_Plotting.ipynb)

Note: Binder sessions are temporary and reset after inactivity (~10 min).

---
## Data Sources

**Wind**:   
[E.U. Copernicus Marine Service Information](https://doi.org/10.48670/moi-00181)

**SST**:   
NOAA Extended Reconstructed SST V6 data provided by the NOAA PSL, Boulder, Colorado, USA, from their [website](https://www.ncei.noaa.gov/products/extended-reconstructed-sst)

**Argo**:   
EN.4.2.2 (analysis.g10) data were obtained from https://www.metoffice.gov.uk/hadobs/en4/ and are © British Crown Copyright, Met Office, provided under a Non-Commercial Government Licence http://www.nationalarchives.gov.uk/doc/non-commercial-government-licence/version/2/.

--- 
### License

This work is licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0). To view a copy of this license, visit https://creativecommons.org/licenses/by/4.0/.

### Third-Party Libraries and Licenses

This project uses several open-source Python libraries for data processing, visualization, and analysis.  
All libraries are distributed under permissive licenses (BSD, MIT, or Apache 2.0) and are used in accordance with their respective terms.

- **NumPy**, **Pandas**, **GeoPandas**, **SciPy**, **GSW**, **HoloViews**, **hvPlot**, **Bokeh**, **Dask**, **IPykernel**, **IPython**, **Jupyter Client** – BSD 3-Clause License  
- **Matplotlib** – Matplotlib License (BSD-like)  
- **Xarray** – Apache License 2.0  
- **netCDF4**, **h5netcdf**, **nc-time-axis**, **Cartopy**, **EOFs**, **Pytest** – MIT License  
- **Emoji**, **PyCWT** – BSD 3-Clause License  

For detailed license texts, please refer to the official documentation of each library or its [PyPI project page](https://pypi.org/).