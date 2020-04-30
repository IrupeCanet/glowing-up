
# Loading dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import sys

col=['sepal_length','sepal_width','petal_length','petal_width','type']
iris = pd.read_csv ("iris.csv",names=col)


#****************************************************************

#Outputs of Shape and Size
stdoutOrigin=sys.stdout 
sys.stdout = open("analysis.txt", "w")
print ("First five rows")
print(iris.head())
print("***********************************")
print("columns", iris.columns)
print("***********************************")
print("shape:", iris.shape)
print("***********************************")
print("Size:",iris.size)
print("***********************************")
print("no of  samples available for each type")
print(iris["type"].value_counts())
print("***********************************")
print(iris.describe())
#Observations: each type of iris flowers(3) it is = 50

# Divide data
iris_setosa=iris.loc[iris["type"]=="Iris-setosa"]
iris_virginica=iris.loc[iris["type"]=="Iris-virginica"]
iris_versicolor=iris.loc[iris["type"]=="Iris-versicolor"]

sys.stdout.close()
sys.stdout=stdoutOrigin

#**************************************************************

# Histograms:
plt.figure(figsize = (12.0,10.0))
x = iris["sepal_width"]
plt.hist(x, bins = 20, color = "green")
plt.title("Sepal Width in cm")
plt.xlabel("Sepal Width")
plt.ylabel("Count")
plt.savefig("Sepal Width Histogram.png")

plt.figure(figsize = (15.0,10.0))
x = iris["sepal_length"]
plt.hist(x, bins = 30, color = "orange")
plt.title("Sepal Length in cm")
plt.xlabel("Sepal Length")
plt.ylabel("Count")
plt.savefig("Sepal Length Histogram.png")

plt.figure(figsize = (12.0,10.0))
x = iris["petal_width"]
plt.hist(x, bins = 20, color = "blue")
plt.title("Petal Width in cm")
plt.xlabel("Petal Width")
plt.ylabel("Count")
plt.savefig("Petal Width Histogram.png")

plt.figure(figsize = (20.0,15.0))
x = iris["petal_length"]
plt.hist(x, bins = 30, color = "red")
plt.title("Petal Length in cm")
plt.xlabel("Petal Length")
plt.ylabel("Count")
plt.savefig("Petal Length Histogram.png")


#***************************************************
# Scatter plots of each pair of variables:

iris = pd.read_csv("iris.csv")
sns.pairplot(iris, hue='species')
plt.show()
