
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


# Histograms

plt.figure(figsize = (10,7))
x = iris["sepal_width"]

plt.hist(x, bins = 20, color = "purple")
plt.title("Sepal Width")
plt.xlabel("Sepal Width")
plt.ylabel("Sepal Length")
plt.show()

plt.figure(figsize = (10,7))
x = iris["sepal_length"]

plt.hist(x, bins = 20, color = "purple")
plt.title("Sepal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.show()

plt.figure(figsize = (10,7))
x = iris["petal_width"]

plt.hist(x, bins = 20, color = "purple")
plt.title("Petal Width")
plt.xlabel("Petal Width")
plt.ylabel("Petal Length")
plt.show()

plt.figure(figsize = (10,7))
x = iris["petal_length"]

plt.hist(x, bins = 20, color = "purple")
plt.title("Petal Length")
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.show()







