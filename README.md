# glowing-up
# General Information about Iris Dataset

The Iris flower data set or Fisher’s Iris data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis.

It is sometimes called Anderson’s Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species.Two of the three species were collected in the Gaspé Peninsula “all from the same pasture, and picked on the same day and measured at the same time by the same person with the same apparatus”.

The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). Four features were measured from each sample: the length and the width of the sepals and petals, in centimeters. Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other.

# The Program
 This program is called analysis.py. To run this file, make sure it is in your current directory and type python filename at the command prompt:

$ python analysis.py

 Once you execute the program, it will:
- outputs a summary of each variable to a single text file;
- saves a histogram of each variable to png files, and
- outputs a scatter plot of each pair of variables.

# The process
To start creating my program I have downloaded the iris Dataset in csv format from: https://tableconvert.com/?output=csv. I have also imported pandas, matplotlib, seaborn, numpy and sys libraries into Visual Studio Code.


from the analysis of data domension and categorization we canobserve...
Data Dimension and Categorization####

The dataset contains 150 observations with 5 attributes named as Sepal width, Sepal length, Petal width, Petal length and flower type.
 [1] "Number of Rows"
 [1] 150
 [1] "Number of Column"
 [1] 5
Out of which 4 are quantitative variables which are Sepal width, Sepal length, Petal width and Petal length and 1 is categorical variable which is flower type or species having 3 values of Virginica, Versicolour and Setosa.
 'data.frame':    150 obs. of  5 variables:
  $ Sepal.Length: num  5.1 4.9 4.7 4.6 5 5.4 4.6 5 4.4 4.9 ...
  $ Sepal.Width : num  3.5 3 3.2 3.1 3.6 3.9 3.4 3.4 2.9 3.1 ...
  $ Petal.Length: num  1.4 1.4 1.3 1.5 1.4 1.7 1.4 1.5 1.4 1.5 ...
  $ Petal.Width : num  0.2 0.2 0.2 0.2 0.2 0.4 0.3 0.2 0.2 0.1 ...
  $ Species     : Factor w/ 3 levels "setosa","versicolor",..: 1 1 1 1 1 1 1 1 1 1 ...
Observing the data, we realize that every species of flower have 50 observations each.
  Min.   :4.300   Min.   :2.000   Min.   :1.000   Min.   :0.100  
  1st Qu.:5.100   1st Qu.:2.800   1st Qu.:1.600   1st Qu.:0.300  
  Median :5.800   Median :3.000   Median :4.350   Median :1.300  
  Mean   :5.843   Mean   :3.057   Mean   :3.758   Mean   :1.199  
  3rd Qu.:6.400   3rd Qu.:3.300   3rd Qu.:5.100   3rd Qu.:1.800  
  Max.   :7.900   Max.   :4.400   Max.   :6.900   Max.   :2.500  
        Species  
  setosa    :50  
  versicolor:50  
  virginica :50 

Source:
- https://stackoverflow.com/questions/25023233/how-to-save-python-screen-output-to-a-text-file

- https://stackoverflow.com/questions/37039685/hide-axis-values-but-keep-axis-tick-labels-in-matplotlib

*Notes:


# Data Visualization

In order to proceed with the visualization of the data contained in the Iris Dataset I have created 2 different types of plots: Histograms and Pairplots.

Histogram: A visual representation of how the data points are distributed with respect to the frequency(count).
This program will save a histogram of each variable to png files contained in the repository. For a better visualization the Histogram of each variable have been represented using different colours.

$plt.figure(figsize = (12.0,10.0))
$x = iris["sepal_width"]
$plt.hist(x, bins = 20, color = "green")
$plt.title("Sepal Width in cm")
$plt.xlabel("Sepal Width")
$plt.ylabel("Count")
$plt.savefig("Sepal Width Histogram.png")

From the visualizations of this hstograms we can say that:
 - The distribution of Iris-Setosa petal is completely different from the other 2 species
 - Using sepal length and sepal width, we can’t separate one species from another as the distribution is overlapping
 - Iris-Setosa is not normally distributed by sepal length and petal width
 - Petal length can be used as a differentiating factor in terms of the distribution of the 3 flower species.

Scatter Plot: Scatter plots are used to plot data points on a horizontal and a vertical axis in the attempt to show how much one variable is affected by another. The relationship between two variables is called their correlation.

$sns.pairplot(iris, hue='species')
$plt.show()

From the observation of this plot, there seems to be a positive correlation between the length and width of all the species, however there is a distinguishing strong correlation and relationship between petal length and petal width.


**Notes: 
- Unfortunatly I could not solve visualization issue that ocurred once I added the pairplot to the program. The Histograms were saving as .png files to the main folder, but once I have added $plt.show() at the end of the program to output the pairplot, all the plots output with the ation.
- Another issue I came accross with and i couldt not solve yet was delete the reference from the  x axis. I have tried few methods bt none of them worked out for me.

Source:
- https://www.oreilly.com/programming/free/files/a-whirlwind-tour-of-python.pdf
- https://realpython.com/lessons/python-histogram-plotting-numpy-matplotlib-pandas-seaborn-conclusion/
- https://realpython.com/lessons/numpy-histograms/
- https://realpython.com/python-matplotlib-guide/
- https://realpython.com/run-python-scripts/
- https://matplotlib.org/tutorials/introductory/pyplot.html
- https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/
- https://seaborn.pydata.org/generated/seaborn.pairplot.html
- https://github.com/mwaskom/seaborn/issues/1347
- https://www.gitmemory.com/issue/matthewearl/faceswap/20/494413525
