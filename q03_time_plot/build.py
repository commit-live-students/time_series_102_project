# %load q03_time_plot/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from greyatomlib.time_series_day_02_project.q01_load_data.build import q01_load_data
plt.switch_backend('agg')
path = 'data/elecdemand.csv'
def q03_time_plot(path):
    shape,data = q01_load_data(path)
    plt.figure(figsize=(16,7))
    plt.plot(data.Datetime,data.Demand)
    plt.title('Electricity Demand in Australia for a year')
    plt.xlabel('Time')
    plt.ylabel('Demand')
    plt.show()


