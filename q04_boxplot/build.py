
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
from greyatomlib.time_series_day_02_project.q01_load_data.build import q01_load_data

def q04_boxplot(path):
    shape,data =q01_load_data(path)
    'write your solution here'
    plt.figure(figsize=(16, 6))

    one = data[data['WorkDay'] == 0]['Demand'].values
    two = data[data['WorkDay'] == 1]['Demand'].values

    plt.boxplot([one, two], labels=['0', '1'])
    plt.xlabel('WorkDay')
    plt.ylabel('Demand')
    plt.title('Change in Electricity demand wrt to Workday')  

