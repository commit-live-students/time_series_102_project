

## Let's write a function `q05_feature_engineering_part4()` that
Visualizing is the key to extract insights from the data. We will use matplotlib plot command to visualize the data.

* Takes as input the file path.
* Makes use of the first function in the assignment.

**To do :**
- Convert the time_col to datetime format using pandas to_datetime api
- Extract the **hour** from time_col (int)
- Extract the **month** from time_col (int)
- Make a new column `Peakhours` whose value is **1** if value of the `hour` column created in the above steps is in the range     (6,20). Else set it to **0**. **Note that 20 will not be included in the range(6,20)**
- Make a new column `Peakmonths` whose value is **1** if value of the `month` column created in the above steps is in the range   ['Feb', May', 'Jun', 'Jul', 'Aug'] . Else set it to **0**.
- Return the new dataframe.


### Parameters:


| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| path | str | compulsory |  | file path of the csv file |



### Returns:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| data | pandas Dataframe | compulsory |  | new dataframe consisting of the `Peakhours` and `Peakmonths` columns. |


