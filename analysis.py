
# Loading dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
col=['sepal_length','sepal_width','petal_length','petal_width','type']
iris = pd.read_csv ("iris.csv",names=col)

#Outputs of Shape and Size
print ("First five rows")
print(iris.head())
#
print("columns", iris.columns)
#
print("shape:", iris.shape)
#
print("Size:",iris.size)
#
print("no of  samples available for each type")
print(iris["type"].value_counts())
#
print(iris.describe())
#Observations: each type of iris flowers(3) it is = 50

# Divide data

iris_setosa=iris.loc[iris["type"]=="Iris-setosa"]
iris_virginica=iris.loc[iris["type"]=="Iris-virginica"]
iris_versicolor=iris.loc[iris["type"]=="Iris-versicolor"]

# histograms
sns.FacetGrid(iris,hue="type",size=3).map(sns.distplot,"petal_length").add_legend()
plt.show()


