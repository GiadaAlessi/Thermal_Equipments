# Exercise 01 - Heating System Design for a Tensile Structure

This project analyzes the design and optimization of a **water-to-water heat pump** system to replace the methane boiler in a tensile sports facility structure located in Bologna, Italy. The analysis includes heat loss estimation, thermodynamic cycle evaluation, and performance comparison using different refrigerants.

## 📄 Report
For a detailed explanation of the methodology, results, and conclusions, please refer to the full report:

➡️ [Heating System Design Report - Giada Alessi](https://github.com/GiadaAlessi/Thermal_Equipments/blob/main/Exercise_01/Own%20Heating%20Problem%20Report.pdf)

## 🔍 Project Overview
The project explores:
- Calculation of heat loss coefficients through the structure, floor, and ventilation.
- Estimation of the maximum heating demand for the facility (**140 kW**).
- Design and evaluation of a **water-to-water heat pump** with:
  - Refrigerant **R1234ze(E)** (low GWP).  
  - Analysis with and without **subcooling** and **superheating**.
- Performance comparison using refrigerants like **R1234ze**, **R410a**, and **NH₃**.

## 🐍 Python Code
The Python code implements:
- Thermodynamic calculations using **CoolProp** for accurate property evaluation.
- Calculation of refrigerant mass flow rate, compressor work, and COP.
- Generation of **T-s** and **P-h** diagrams for visualizing the vapor compression cycle.

For code details, refer to the file **`TE_ex1_ownheating.py`**.

---
**Author:** Giada Alessi

