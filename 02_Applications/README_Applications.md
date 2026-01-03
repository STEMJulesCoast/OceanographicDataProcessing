# 02_Applications – Ocean Processes, Time Series, and Spectral Analysis

This folder contains the notebooks for the **second on-site session** of the *Oceanographic Data Processing Course*.  
Here, we move from basic data handling to **applied analyses of ocean–atmosphere processes**, time series variability, and frequency-domain methods.

We will work through these notebooks together during class. Any unfinished parts can be completed independently afterward.

----
### Overview:
-----

- **`04_EkmanDynamics.ipynb`**  
  Analysis of wind-driven ocean dynamics.  
  We compute wind stress, Ekman transport, wind stress curl, and Ekman pumping, and interpret the resulting spatial patterns.

- **`05_4DOceanData.ipynb`**  
  Introduction to four-dimensional ocean data (time, depth, latitude, longitude).  
  We analyze temperature, salinity, density, and mixed layer depth using profile-based datasets (e.g. Argo / EN4).

- **`06_FFT_OOP.ipynb`**  
  Time series analysis in the frequency domain.  
  We apply FFT and spectral methods, introduce an object-oriented workflow, and automate common analysis steps using classes.

- **`EOFanalysis_demo.ipynb`**  
  Demonstration notebook for Empirical Orthogonal Function (EOF) analysis, illustrating dominant spatial and temporal modes of variability.



### Key Learning Outcomes:

- **Physical Oceanography:** Understand wind-driven processes such as Ekman transport and Ekman pumping.  
- **4D Data Analysis:** Work with depth-resolved ocean datasets and compute diagnostics like mixed layer depth.  
- **Time Series Analysis:** Quantify variability across seasonal to interannual timescales.  
- **Spectral Methods:** Analyze dominant timescales using FFT and related techniques.  
- **Object-Oriented Programming:** Use classes and methods to structure and automate analysis workflows.  
- **Reproducible Workflows:** Combine physics, statistics, and clean code design in applied climate data analysis.

### Tip
These notebooks build on concepts from `01_Fundamentals`. If something feels unfamiliar, revisit earlier notebooks or take time to rerun cells and read the explanations carefully, most questions are answered directly in the notebook text.
