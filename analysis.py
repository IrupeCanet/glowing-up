import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

 col=['sepal_length','sepal_width','petal_length','petal_width','type']
df = pd.read_csv ("iris.csv",names=col)

plt.scatter (df['sepal_length'], df['sepal_width'])
plt.title("Sepal length versus Sepal width")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.show()

plt.scatter (df['petal_length'], df['petal_width'])
plt.title("Petal length versus Petal width")
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.show()

sns.pairplot(df, hue="species")
plt.show()

