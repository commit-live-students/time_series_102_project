# %load q03_time_plot/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from greyatomlib.time_series_day_02_project.q01_load_data.build import q01_load_data
plt.switch_backend('agg')

def q03_time_plot(path):
    path = 'data/elecdemand.csv'
    shape, df = q01_load_data(path)
    plt.plot(df['Datetime'], df['Demand'])
    plt.title('Electricity Demand for Australia for a year')
    plt.xlabel('Year-Month')
    plt.ylabel('Demand')
    plt.show();




