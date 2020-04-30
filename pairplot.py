import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

iris = pd.read_csv("iris.csv")

sns.pairplot(iris, hue='species')
plt.show()
