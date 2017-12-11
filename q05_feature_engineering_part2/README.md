

## Let's write a function `q05_feature_engineering_part2()` that
Visualizing is the key to extract insights from the data. We will use matplotlib plot command to visualize the data.

* Takes as input the file path.
* Makes use of the first function in the assignment.

**To do :**
- Convert the time_col to datetime format using pandas to_datetime api
- Extract the **hour** from time_col (int)
- Extract the **month** from time_col (int)
- Extracts the values for the **Demand** column hourwise and append it to a list.
- Plot the same in a boxplot.


### Parameters:

Function should take list of time values and predictor variable as input and output a plot.

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| path | str | compulsory |  | file path of the csv file |



### Returns:
None.
