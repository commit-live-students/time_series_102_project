# %load q05_feature_engineering_part2/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from greyatomlib.time_series_day_02_project.q01_load_data.build import q01_load_data
plt.switch_backend('agg')

def q05_feature_engineering_part2(path):
    path = 'data/elecdemand.csv'
    shape, data = q01_load_data(path)
    data['hour'] = data['Datetime'].dt.hour
    data['month'] = data['Datetime'].dt.month
    plt.figure(figsize=(16, 6))
    demand_hours = []
    for i in range(1,25):
        one = data[data['hour'] == i]['Demand'].values
        demand_hours.append(one)
    demand_months = []
    for j in range(1,13):
        demand_months.append(data[data['month'] == j]['Demand'].values)
    plt.subplot(211)
    plt.boxplot(demand_hours, labels=[str(i) for i in range(1,25)])
    plt.xlabel('Hour')
    plt.ylabel('Demand')
    plt.title('Change in Electricity demand wrt to Hour') 
    plt.subplot(212)
    plt.boxplot(demand_months, labels=[str(i) for i in range(1,13)])
    plt.xlabel('Months')
    plt.ylabel('Demand')
    plt.title('Change in Electricity demand wrt to months') 
    plt.show();




