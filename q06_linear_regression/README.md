# Fitting your first linear regression model

## Let's write a function `q06_linear_regression()` that
* Takes as input the path and column names.
* Fits a LinearRegression with default parameters model on it.
* Returns the mean RMSE.

### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| path | str | compulsory | | file path of the csv file |
| column_names | list | compulsory | ["WorkDay", "Peakhours", "Peakmonths"] |  |


### Returns:

| Return | dtype | description |
| --- | --- | --- |
| lm | sklearn.linear_model.LinearRegression | Fitted Linear Regression model |
