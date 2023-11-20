import numpy as np
import pandas as pd

class Utils:
    def check_type(self, value):
        return type(value)
    
    def compare_two_types(self, value1, value2):
        type1 = self.check_type(value1)
        type2 = self.check_type(value2)

        return (type1 == type2)
    
    def compare_variable_names(self, name1, name2):
        return (name1 == name2)
    
    def compare_values_of_variables(self, value1, value2):
        return (value1 == value2)