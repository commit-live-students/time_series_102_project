# %load q05_feature_engineering/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from greyatomlib.time_series_day_02_project.q01_load_data.build import q01_load_data
plt.switch_backend('agg')
path = 'data/elecdemand.csv'
def q05_feature_engineering(path):
    shape,data = q01_load_data(path)
    corr = data['Temperature'].corr(data['Demand'])
    plt.figure(figsize=(16,6))
    plt.scatter(data['Temperature'],data['Demand'])
    plt.title('Temperature vs. Demand')
    plt.xlabel('Temperature')
    plt.ylabel('Demand')
    plt.show()



