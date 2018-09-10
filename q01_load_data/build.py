# %load q01_load_data/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

path = 'data/elecdemand.csv'

def q01_load_data(data):
    
    df = pd.read_csv(data)  # Load data and converting to DataFrame
    
    # Make the Datetime column as object and Drop the index.
    df['Datetime'] = pd.to_datetime(df['Datetime'], format = '%Y-%m-%d')
    #df.index = df['Datetime']
    return (df.shape, df)
    
q01_load_data(path)


