import pandas as pd
import numpy as np

# 1. Load Data
print("Loading datasets...")
df_vehicles = pd.read_csv("747e71a4-18fd-4205-ace2-aa7d786478fe.csv", encoding='latin1')
df_stations = pd.read_csv("Indian_EV_Stations_Simplified.csv")

# 2. Clean EV Stations Data
print("Cleaning EV Stations data...")
df_stations.dropna(subset=['Latitude', 'Longitude'], inplace=True)

median_power = df_stations['Power (kW)'].median()
df_stations['Power (kW)'] = df_stations['Power (kW)'].fillna(median_power)

# 3. Clean Vehicle Traffic Data (Feature Engineering)
print("Processing Vehicle Data...")
df_vehicles.rename(columns={'Category': 'City'}, inplace=True)

cols_2018 = [col for col in df_vehicles.columns if '2017-18' in col]

# Fixing the String vs Float issue
for col in cols_2018:
    df_vehicles[col] = pd.to_numeric(df_vehicles[col], errors='coerce')

df_vehicles['Total_Vehicles_Proxy'] = df_vehicles[cols_2018].sum(axis=1, numeric_only=True)
df_city_traffic = df_vehicles[['City', 'Total_Vehicles_Proxy']].copy()

# 4. Calculate City-level EV Supply
print("Calculating Demand-Supply Metrics...")
city_station_counts = df_stations.groupby('City').size().reset_index(name='Total_EV_Stations')
city_metrics = pd.merge(city_station_counts, df_city_traffic, on='City', how='left')

city_metrics['Total_Vehicles_Proxy'] = city_metrics['Total_Vehicles_Proxy'].fillna(0) 
city_metrics['Vehicles_per_Station'] = np.where(
    city_metrics['Total_EV_Stations'] > 0, 
    city_metrics['Total_Vehicles_Proxy'] / city_metrics['Total_EV_Stations'], 
    0
)

# 5. Merge Everything for Power BI
print("Finalizing data for Power BI...")
final_df = pd.merge(df_stations, city_metrics, on='City', how='left')

# 6. Export to CSV
final_df.to_csv("cleaned_EV_data_for_PowerBI.csv", index=False)
print("Done! File saved as 'cleaned_EV_data_for_PowerBI.csv'. You can now import this into Power BI.")