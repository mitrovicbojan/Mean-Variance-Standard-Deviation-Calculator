import numpy as np;
import pandas as pd;

data = [1,2,3,4,5,6,7,8,9]

# create 3x3 matrix

def calculate(list):
    matrix = np.array(list).reshape(3,3)
    return matrix

# calculate mean

def mean_calc(list):
    #nums = calculate(list)
    #return nums.mean(axis=0).tolist() 
    mean_matrix = calculate(list)
    mean_dict = {
        "mean": [
            mean_matrix.mean(axis=0).tolist(), mean_matrix.mean(axis=1).tolist(), float(mean_matrix.mean()),
            
        ]
    }
    return mean_dict

# calculate variance

def var_calc(list):
    var_matrix = calculate(list)
    var_dict = {
        "variance": [
            var_matrix.var(axis=0).tolist(), var_matrix.var(axis=1).tolist(), float(var_matrix.var())
        ]
    }
    return var_dict


#calculate standard deviation
def std_calc(list):
    std_matrix = calculate(list)
    std_dict = {
        "standard deviation": [
            std_matrix.std(axis=0).tolist(), std_matrix.std(axis=1).tolist(), float(std_matrix.std())
        ]
    }
    return std_dict

#calculate minimum values
def min_calc(list):
    min_matrix = calculate(list)
    min_dict = {
        "min": [
            min_matrix.min(axis=0).tolist(), min_matrix.min(axis=1).tolist(), float(min_matrix.min())
        ]
    }
    return min_dict
# calculate max values
def max_calc(list):
    max_matrix = calculate(list)
    max_dict = {
        "max": [
            max_matrix.max(axis=0).tolist(), max_matrix.max(axis=1).tolist(), float(max_matrix.max())
        ]
    }
    return max_dict
# calculate sum of all elements
def sum_calc(list):
    sum_matrix = calculate(list)
    sum_dict = {
        "sum": [
            sum_matrix.sum(axis=0).tolist(), sum_matrix.sum(axis=1).tolist(), float(sum_matrix.sum())
        ]
    }
    return sum_dict
    
def all_calc(data):
    return {
        'mean': mean_calc(data)['mean'],
        'variance': var_calc(data)['variance'],
        'standard deviation': std_calc(data)['standard deviation'],
        'max': max_calc(data)['max'],
        'min': min_calc(data)['min'],
        'sum': sum_calc(data)['sum']
    }

    
result = all_calc(data)
print(result)
'''
The function should convert the list into a 3 x 3 Numpy array, and then return a dictionary containing the mean, variance, standard deviation, max, min, and sum along both axes and for the flattened matrix.

The returned dictionary should follow this format:

{
  'mean': [axis1, axis2, flattened],
  'variance': [axis1, axis2, flattened],
  'standard deviation': [axis1, axis2, flattened],
  'max': [axis1, axis2, flattened],
  'min': [axis1, axis2, flattened],
  'sum': [axis1, axis2, flattened]
}
'''

