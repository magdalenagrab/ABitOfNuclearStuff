# Cs-137 Gamma Spectrum Analysis (Python & C++)

This repository demonstrates gamma spectrum analysis of Cs-137 implemented in both **Python** and **C++** for comparison.

- **Experimental detector data** (red dots) is compared with a **simulated spectrum** (blue dashed line). 
- The simulation includes a **main gamma peak** at 662 keV and a **bulk/Compton background** with realistic Poisson noise. 
- The simulated spectrum is **manually scaled** to match the experimental detector data, mimicking real-life nuclear physics data analysis. 
- The scripts automatically generate plots for visualization (`spectrum_analysis.png` in Python, equivalent in C++).

## Why Cs-137?

Cesium-137 is a **radioactive isotope** widely used in science and industry due to its gamma emission at 662 keV. Its main applications include:

1. **Calibration of radiation detectors** – ideal for checking detector performance and energy calibration.  
2. **Environmental monitoring and nuclear safety** – tracking radioactive contamination in soil, water, and air.  
3. **Medical and industrial applications** – radiotherapy (brachytherapy) and industrial radiography.  
4. **Scientific research** – reference in nuclear physics experiments, studies of radioactive decay, and gamma spectrum simulations.

**Why it’s useful in this project:**  
- The clear gamma peak at 662 keV allows comparison of experimental detector data with simulated spectra, demonstrating **data analysis, simulation, and manual scaling skills**.  

## Files

- `spectrum_analysis.py` – Python implementation (reads `detector_data.txt` and generates plots).  
- `spectrum_analysis.cpp` – C++ implementation (similar functionality for comparison).  
- `detector_data.txt` – Example detector data (energy [keV], counts).  
- `results/` – Folder for output plots.

## How to run (Python)

1. Make sure you have `numpy` and `matplotlib` installed:
   ```bash
   pip install numpy matplotlib

