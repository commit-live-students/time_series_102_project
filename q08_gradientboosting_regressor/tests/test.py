import unittest
from inspect import getfullargspec
from ..build import q08_gradientboosting_regressor as student
from greyatomlib.time_series_day_02_project.q08_gradientboosting_regressor.build import q08_gradientboosting_regressor as originalx
import pandas as pd
from pandas.util.testing import assert_frame_equal
fe =  ["WorkDay", "Peakhours", "Peakmonths"]

class Testing(unittest.TestCase):
    def setUp(self):
        self.student_func = student
        self.solution_func = original
        self.data = 'data/elecdemand.csv'
        self.student_return = self.student_func(self.data)
        self.original_return = self.solution_func(self.data)

    #  Check the arguements of the function
    def test_timeseries(self):
        # Input parameters tests
        args_student = getfullargspec(student)
        args_original = getfullargspec(original)
        self.assertEqual(len(args_student[0]),len(args_original[0]),  "Expected argument(s) %d, Given %d" % ( len(args_original[0],len(args_student[0]))))

    def test_timeseries_default(self):
        args_student = getfullargspec(student)
        args_original = getfullargspec(original)
        self.assertEqual(args_student[3],args_original[3], "Expected default values do not match given default values")


    def test_return(self):
        self.ssertAlmostEqual(self.student_return, self.original_return, "The return values do not match expected values")

