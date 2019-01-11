# %load q05_feature_engineering_part2/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from greyatomlib.time_series_day_02_project.q01_load_data.build import q01_load_data

path = 'data/elecdemand.csv'

def q05_feature_engineering_part2(path):
    shape, data = q01_load_data(path)
    data['hour'] = data['Datetime'].dt.hour
    plt.figure(figsize=(16, 6))
    hours = []
    for i in range(24):
        one = data[data['hour'] == i]['Demand'].values
        hours.append(one)
    plt.boxplot(hours, labels=[str(i) for i in range(24)])
    plt.xlabel('Hour')
    plt.ylabel('Demand')
    plt.title('Change in Electricity demand wrt to Hour') 
    
# q05_feature_engineering_part2(path)


