# %load q01_load_data/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def q01_load_data(path):
    tss=pd.read_csv(path)
    tss['Datetime']=pd.to_datetime(tss['Datetime'])
    return tss.shape, tss




    


