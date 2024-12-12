import pandas as pd
import numpy as np

num_rows = 1000


dates = pd.date_range(start="2023-01-01", end="2023-12-31", freq="H")  
random_dates = np.random.choice(dates, num_rows, replace=True)  

np.random.seed(42)  


temperature = np.round(10 + 15 * np.sin(2 * np.pi * pd.to_datetime(random_dates).dayofyear / 365) + 
                        np.random.normal(0, 3, num_rows), 1)


precipitation = np.random.choice([0, 0, 5, 10, 15, 20], size=num_rows, p=[0.6, 0.2, 0.1, 0.05, 0.03, 0.02])


humidity = np.round(np.clip(50 + 20 * np.sin(2 * np.pi * pd.to_datetime(random_dates).dayofyear / 365) + 
                            np.random.normal(0, 10, num_rows), 30, 100), 1)


latitude = np.random.uniform(-90, 90, num_rows)
longitude = np.random.uniform(-180, 180, num_rows)


weather_data = pd.DataFrame({
    "Date": random_dates,
    "Temperature": temperature,
    "Precipitation": precipitation,
    "Humidity": humidity,
    "Latitude": latitude,
    "Longitude": longitude
})


weather_data["Temperature_F"] = weather_data["Temperature"] * 9/5 + 32  
weather_data["Is_Hot"] = (weather_data["Temperature"] > 25).astype(int)  


weather_data = weather_data.sort_values(by="Date").reset_index(drop=True)


weather_data.to_csv("weather_data_1000.csv", index=False)

print("Dataset météo avec 1000 lignes généré et sauvegardé dans 'weather_data_1000.csv'.")
