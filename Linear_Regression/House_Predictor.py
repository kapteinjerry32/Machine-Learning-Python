#This python file will predict house prices using linear regression
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns # aesthetic versions of matplotlib graphs
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

%matplotlib inline

housing_dataset = pd.read_csv("BostonHousing.csv")
housing_dataset.head()