import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

import os

base = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base, 'input',
    'On_Time_Marketing_Carrier_On_Time_Performance_(Beginning_January_2018)_2025_1.csv')
df = pd.read_csv(csv_path)
print(df.head())