#start

#Import library of PANDAS
import pandas as pd

#Load csv file into a data frame named cars using pandas
df_cars = pd.read_csv('cars.csv')

# The condition :5 inside the square bracket selects the first 5 rows of the DataFrame but does not include the upper range, 5th row, to be printed

df_cars.iloc[:5,::2]

# The double colon ::2 slices every two steps of the column

#Uses .loc to locate and print the row that has the key value : 'Model' is equal to 'Mazda RX4'
df_cars.loc[df_cars['Model']=='Mazda RX4'] 

#Uses .loc to locate and print information that has the key value : 'Model' is equal to 'Mazda RX4'
#This time the syntax next to locating the model is the specified info/column to be printed
df_cars.loc[(df_cars['Model']=='Camaro Z28'), ['cyl']]

#Create list of car models needed for information
car_models = ['Mazda RX4','Ford Pantera L','Honda Civic']

#Uses .loc to locate the key values of the model of a car and prints specified information
#Uses .isin to check if any 'Model' in the dataframe is in the created list of car models
df_cars.loc[df_cars['Model'].isin(car_models),['Model','cyl','gear']]

#end