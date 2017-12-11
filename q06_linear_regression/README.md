# Fitting your first linear regression model

## Let's write a function `q06_linear_regression()` that
* Takes as input the path and column names.
* Load the data using the previous assignment function.
* Split the data into two pairs of arrays for train and test indices using the second function of this project. 
* Extract the values of the train and test for only the given column names.
* Fits a LinearRegression with default parameters model on it.
* Returns the mean RMSE.

### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| path | str | compulsory | | file path of the csv file |
| column_names | list | compulsory | ["WorkDay", "Peakhours", "Peakmonths"] | columns whose values are to be considered |


### Returns:

| Return | dtype | description |
| --- | --- | --- |
| rmse | float | RMSE of the linear regression model |
