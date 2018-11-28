# %load q05_feature_engineering_part3/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from greyatomlib.time_series_day_02_project.q01_load_data.build import q01_load_data
plt.switch_backend('agg')
path = 'data/elecdemand.csv'

def q05_feature_engineering_part3(path):
    shape,data = q01_load_data(path)
    data['Month'] = data['Datetime'].dt.strftime('%b')
    sns.factorplot(x='Month',y='Demand',data=data,kind='box',size=8,aspect=(16/9))
    plt.title('Change in Demand of Electricity wrt Month')
    plt.show()

