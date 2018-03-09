
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from greyatomlib.time_series_day_02_project.q01_load_data.build import q01_load_data

def q05_feature_engineering_part3(path):
    shape, data = q01_load_data(path)    
    'write your solution here'
    plt.figure(figsize=(16, 6))
    data['month'] = data['Datetime'].dt.strftime('%b')
    month = []
    month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    for i in month_names:
        one = data[data['month'] == i]['Demand'].values
        month.append(one)
    plt.boxplot(month, labels=month_names)
    plt.xlabel('Hour')
    plt.ylabel('Demand')
    plt.title('Change in Electricity demand wrt to Hour')
    

