# Predicting electricity demand in GW for Victoria, Australia using Time Series Forecasting
Welcome to the Time-Series Project-2 !
In this project, you will demonstrate what you have learned in this course by Predicting the melectricity demand for Victoria, Australia

We have seen in the in-class session how Time Series Forecasting Problem needs to be approached using Machine Learning approach. We learnt about:

* Feature Engineering for Time-Series Problems
* Building Linear Regression on Time-Series data


## Whats new in this data ?
Throughout this Course we have only dealt with monthly data. Now can we model only for monthly data ? What happens if we need predictions for every 5 mins interval, every 30 mins, every hour, every day, every week , every Quarter, every year?

We can deal with them. We can build models for any kind of data. Lets deal with this data which needs predictions for every half an hour. 


### Load the required libraries

You can use pandas, datetime, math, sklearn, matplotlib, seaborn for this exercise


## Dataset

For this exercise, we will use electricity demand in GW for Victoria, Australia measured every half-hour during 2014.
This dataset has three columns

- Demand:	Total electricity demand in GW for Victoria, Australia, every half-hour during 2014.  (Predictor Variable)
- WorkDay: Taking value 1 on work days, and 0 otherwise.  
- Temperature: Half-hourly temperatures for Melbourne (BOM site 086071).  



## Why solve this assignment?

Solving this assignment would help you :-

* Visualize Time-Series data effectively
* Build models using Machine Learning on Time-Series data

* For the assignment we will be using the following below packages:
    * **pandas**
    * **datetime**
    * **math**
    * **sklearn**
    * **matplotlib**

- Yes No Seaborn. I am doing this purposefully as you should know how to plot using matplotlib.

Reason: matplotlib is faster than seaborn. Find out Why?  

By completing this project you have an opportunity to win 250 points!

Let's get started!
