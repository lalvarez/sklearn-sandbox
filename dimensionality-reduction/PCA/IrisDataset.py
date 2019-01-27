import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from sklearn import datasets
from sklearn.decomposition import PCA

iris = datasets.load_iris()

X = iris.data
y = iris.target

features = iris.feature_names
targets = iris.target_names

print(dir(iris))
print(iris.feature_names)
print(y)
