
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from greyatomlib.time_series_day_02_project.q01_load_data.build import q01_load_data

def q03_time_plot(path):
    'write your solution here'
    shape, data = q01_load_data(path)
    plt.figure(figsize=(16, 6))
    plt.plot(data['Datetime'], data['Demand'])
    plt.xlabel('Time')
    plt.ylabel('Demand')
    plt.title('Electricity demand in Australia for an Year')

