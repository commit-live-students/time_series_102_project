# %load q05_feature_engineering_part2/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from greyatomlib.time_series_day_02_project.q01_load_data.build import q01_load_data
path = 'data/elecdemand.csv'

plt.switch_backend('agg')

path = 'data/elecdemand.csv'

def q05_feature_engineering_part2(path):
    df_shape, df = q01_load_data(path)
    df['hour'] = df['Datetime'].dt.hour
    hours = []
    for i in range(24):
        one = df[df['hour'] == i]['Demand'].values
        hours.append(one)
    plt.boxplot(hours, labels=[str(i) for i in range(24)])
    plt.show()

# q05_feature_engineering_part2(path)


