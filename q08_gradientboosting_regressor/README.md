# Fitting your first Gradient Boosting regressor model

## Let's write a function `q08_gradientboosting_regressor()` that
* Takes as input the path and column names.
* Load the data using the previous assignment function.
* Split the data into two pairs of arrays for train and test indices using the second function of this project. 
* Extract the values of the train and test for only the given column names.
* Fits a Gradient Boosting regressor with default parameters model on it.
* Returns the mean RMSE.
* Set random_state equal to **9** inside the function parameter.
* Set the hyperparameters for GradientBoostingRegressor as 'n_estimators=200, min_samples_leaf=10, learning_rate=0.01, random_state=random_state`

### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| path | str | compulsory | | file path of the csv file |
| column_names | list | compulsory | ["WorkDay", "Peakhours", "Peakmonths"] | columns whose values are to be considered |


### Returns:

| Return | dtype | description |
| --- | --- | --- |
| rmse | float | RMSE of the Gradient Boosting regressor model |
