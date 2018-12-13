# %load q03_time_plot/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from greyatomlib.time_series_day_02_project.q01_load_data.build import q01_load_data
plt.switch_backend('agg')

path = 'data/elecdemand.csv'

def q03_time_plot(path):
    shp,df=q01_load_data(path)
    plt.figure(figsize=(16, 6))
    plt.plot(df['Datetime'], df['Demand'])
    plt.xlabel('Time')
    plt.ylabel('Demand')
    plt.title('Electricity Demand in Australia for a year')
    plt.show()

# q03_time_plot(path)




