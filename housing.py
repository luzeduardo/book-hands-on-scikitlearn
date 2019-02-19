import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

def load_housing_data(housing_path):
  csv_path = os.path.join(housing_path, 'housing.csv')
  return pd.read_csv(csv_path)

def split_train_test(data, test_ratio):
  shuffled_indices = np.random.permutation(len(data))
  test_set_size = int(len(data)) * test_ratio
  test_indices = shuffled_indices[:test_set_size]
  train_indices = shuffled_indices[test_set_size:]
  return data.iloc[train_indices], data.iloc[test_indices]

housing = load_housing_data('./')
train_set, test_set = split_train_test(housing, 0.2)
#print (housing.head())
#print (housing.info())
print (housing.describe())
#print (housing['ocean_proximity'].value_counts())
#housing.hist(bins=50, figsize=(20,15))
#plt.show()
