#start

#Import library of PANDAS
import pandas as pd

#For part a.

#Load csv file into a data frame named cars using pandas
df_cars = pd.read_csv('cars.csv')

#For part b.

#use .head() to display the first five rows of the data frame of cars
df_cars.head()

#use .tail() to display the last five rows of the data frame of cars
df_cars.tail()

#end