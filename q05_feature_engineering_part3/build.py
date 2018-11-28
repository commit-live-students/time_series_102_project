# %load q05_feature_engineering_part3/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from greyatomlib.time_series_day_02_project.q01_load_data.build import q01_load_data
plt.switch_backend('agg')
def q05_feature_engineering_part3(path):
    tss,df=q01_load_data(path)
    df.info()
    df['hour']=df['Datetime'].dt.hour
    df['month']=df['Datetime'].dt.strftime('%b')
    
    sns.factorplot(x='month', y='Demand', data=df, kind='box', order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug','Sep', 'Oct', 'Nov', 'Dec'], size=8, aspect=float(16/7))
    
#path='data/elecdemand.csv'    
#q05_feature_engineering_part3(path)

