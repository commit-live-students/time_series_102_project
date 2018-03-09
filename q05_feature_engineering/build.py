import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from greyatomlib.time_series_day_02_project.q01_load_data.build import q01_load_data

def q05_feature_engineering(path):
    shape, data = q01_load_data(path)
    'write your solution here'
    data[['Temperature', 'Demand']].corr(method='pearson')

    plt.figure(figsize=(16, 6))

    plt.scatter(data['Temperature'], data['Demand'])
    plt.xlabel('Temperature')
    plt.ylabel('Demand')
    plt.title('Temperature vs Demand')
    #plt.show()   


