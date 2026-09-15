# ⚡ EV-ChargeNet: Geospatial Data Analysis for EV Infrastructure

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)

## 📌 Project Overview
The rapid transition towards Electric Vehicles (EVs) is a critical step for sustainable urban mobility. However, the uneven geographical distribution of charging infrastructure creates "range anxiety" among EV drivers. 

**EV-ChargeNet** is a Business Intelligence and Geospatial Analytics project that identifies optimal, data-driven locations to install new Electric Vehicle charging stations. By mapping registered vehicle demand against existing charging supply, this project highlights "charging deserts" and potential investment zones.

## ⚙️ Tech Stack
* **Data Wrangling & Cleaning:** Python, Pandas, NumPy
* **Data Visualization:** Microsoft Power BI
* **Key Techniques:** Geospatial Mapping, Data Imputation, Cross-Filtering, Feature Engineering

## 📊 The Data Pipeline
1. **Data Sourcing:** Utilized open-source datasets containing GPS coordinates of 855 EV charging stations and a proxy dataset representing ~5.06 million registered vehicles across Indian cities.
2. **Data Cleaning (Python):** 
   * Dropped malformed spatial coordinates.
   * Handled text-to-float conversion errors in vehicle data using `pd.to_numeric()`.
   * Imputed missing Power (kW) capacities with median values.
3. **Feature Engineering:** Engineered a custom demand score metric: `Vehicles_per_Station`.
4. **BI Integration:** Built a 4-page interactive dashboard in Power BI.

---

## 📈 Dashboard Interfaces & Insights

### 1. Executive Overview & Geospatial Distribution
*Highlights the macro-level concentration of charging infrastructure. The custom bubble map visually scales charging capabilities (kW).*
<img src="images/Page 1.jpeg" width="800">

### 2. Infrastructure Demand Gap Analysis
*The analytical core of the project. A scatter plot matrix that categorizes cities into 'Critical Gap', 'Moderate', or 'Balanced' zones based on vehicle density versus charger availability.*
<img src="images/Page 2.jpeg" width="800">

### 3. Operator & Technology Landscape
*Analyzes market competition (e.g., ChargeMod dominating the sample data) and reveals that ultra-fast DC chargers (150kW+) currently make up only 0.1% of the infrastructure.*
<img src="images/Page 3.jpeg" width="800">

### 4. Station Explorer (Operational View)
*A highly interactive tool allowing stakeholders to drill down by city, operator, and power rating with conditional color formatting.*
<img src="images/Page 4.jpeg" width="800">

---

## 🚀 Future Scope
* **Machine Learning Integration:** Implementing **K-Means Clustering** on GPS coordinates and traffic density to mathematically predict the exact spatial 'Centroids' for building new charging hubs.
* **Live API Integration:** Transitioning from static CSVs to the live OpenStreetMap (OSMnx) API for real-time Point of Interest (POI) data.

## 👨‍💻 Author
**Sonu Kumar Thakur**
* B.Tech Computer Science & Engineering
* GitHub: [@sonukrthakur3](https://github.com/sonukrthakur3)
.
