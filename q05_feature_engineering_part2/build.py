# %load q05_feature_engineering_part2/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from greyatomlib.time_series_day_02_project.q01_load_data.build import q01_load_data
path = 'data/elecdemand.csv'
plt.switch_backend('agg')

def q05_feature_engineering_part2(path):
    shape, data = q01_load_data(path)
    data['hour'] = data['Datetime'].dt.hour

    hour = []
    for i in range(24):
        hour_demand = data[data['hour'] == i]['Demand'].values
        hour.append(hour_demand)
    plt.figure(figsize=(16,6))
    plt.boxplot(hour,labels=[str(i) for i in range(24)])
    plt.xlabel('Hour')
    plt.ylabel('Demand')
    plt.title('Change in Electricity demand wrt to Hour')    
    plt.show()

