import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


from sklearn.dataset import load_iris

dataset=pd.DataFrame(dataset['data],columns=["Petal Length","Petal Width","Sepal Length","Sepal Width"])
data['Species']=dataset['target']
data['Species']=data['Species'].apply(lambda x: dataset['target_names'][x])
data.head()

df = pd.read_csv ("iris.csv")

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

