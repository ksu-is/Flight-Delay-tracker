import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

import os

#read csv file
base = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base, 'input',
    'On_Time_Marketing_Carrier_On_Time_Performance_(Beginning_January_2018)_2025_1.csv')
df = pd.read_csv(csv_path, low_memory=False)

# Normalize column names to lowercase
df.columns = [col.lower() for col in df.columns]

# Display the first few rows of the dataframe
print(df.head( 15 ))

# checking the dimensions of the 'flight_data' dataset
print("DataFrame shape:", df.shape)

# Deal with the four key columns
time_cols = ['deptime', 'depdelay', 'arrtime', 'arrdelay']

# Fill nulls with 0 and convert to int64
for col in time_cols:
    df[col] = df[col].fillna(0).astype('int64')

# Confirm conversion
print("\nDtypes after conversion:")
print(df[time_cols].dtypes)

