# %load q05_feature_engineering/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from greyatomlib.time_series_day_02_project.q01_load_data.build import q01_load_data
plt.switch_backend('agg')

path='data/elecdemand.csv'

def q05_feature_engineering(path):
    shape,df = q01_load_data(path)
    corr=np.corrcoef(df['Temperature'], df['Demand'])
    plt.figure(figsize=(16, 6))
    plt.scatter(df['Temperature'], df['Demand'])
    plt.xlabel('Temperature')
    plt.ylabel('Demand')
    plt.title('Temperature vs Demand')
    plt.show()

# q05_feature_engineering(path)






