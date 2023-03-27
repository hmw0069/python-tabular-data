#Import your packages - these will need to be installed before running this script.
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

if __name__ == '__main__':

#Need to load the data.
    dataframe = pd.read_csv("iris.csv")

#Going to make a loop so that 3 regressions are made for the 3 dif. species.
    for species in dataframe.species.unique():
    #subsetting the data.
        unique_species = dataframe[dataframe.species == species]

    #Getting petal length and sepal length of the species.
        x = unique_species.petal_length_cm
        y = unique_species.sepal_length_cm

    #Plotting the regression of petal v. sepal length.
        regression = stats.linregress(x, y)
        slope = regression.slope
        intercept = regression.intercept
        plt.scatter(x, y, label = 'Data')
        plt.plot(x, slope * x + intercept, color = "orange", label = 'Fitted line')
        plt.xlabel("Petal length (cm)")
        plt.ylabel("Sepal length (cm)")
        plt.legend()

    #Need to create a variable so that each iteration creates a unique file name and doesn't save it over the same name.
        iris_plots = species + "_regression.png"
        plt.savefig(iris_plots)
        plt.clf()


