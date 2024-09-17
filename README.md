# PA3 - Python Data Analysis
Programming Assignment 3 - Bon-ao, Angelo B. - ECE2112 - Adv. Computer Programming

This repository contains 3 files, which are Bon-ao_Pandas-P1.py, Bon-ao_Pandas-P2.py, and a README File. Bon-ao_Pandas-P1.py and Bon-ao_Pandas-P2.py both contain the solutions for the two part-problems in Programming Assignment 3.

---

## GIVEN 

For this programming assignment, download the following file and save to your default user folder: http://bit.ly/Cars_file

### PROBLEM 1️⃣

Using knowledge obtained from the experiment and demonstrations:

a. Load the corresponding .csv file into a data frame named cars using pandas

b. Display the first five and last five rows of the resulting cars.

### PROBLEM 2️⃣

Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and
indexing operations.

a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.

b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.

c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?

d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

---
## SOLUTIONS

### PROBLEM 1️⃣

The first problem is divided into two tasks, the first of which is to load the .csv file that we have downloaded from http://bit.ly/Cars_file into dataframe named cars using pandas, and secondly, displaying the first five and last five rows of the data frame.

For the first task, we must use ``` pd.read_csv() ``` to load and read the cars csv file as a dataframe. I stored the csv file to 'df_cars' to highlight that it is a dataframe due to 'df' and the information inside is about cars. For the second task, we must use ``` .head() and .tail() ```. The .head() command prints out the first five rows by default and the .tail() command prints out the last five rows by default, so no need to input a number for the condition.

### CODE
``` python

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
```

### OUTPUT

``` python
df_cars.head()
```

|   | Model              | mpg  | cyl | disp  | hp   | drat | wt    | qsec  | vs | am | gear | carb |
|----|--------------------|------|-----|-------|------|------|-------|-------|----|----|------|------|
|  0 | Mazda RX4          | 21.0 |  6  | 160.0 | 110  | 3.90 | 2.620 | 16.46 |  0 |  1 |  4   |  4   |
|  1 | Mazda RX4 Wag      | 21.0 |  6  | 160.0 | 110  | 3.90 | 2.875 | 17.02 |  0 |  1 |  4   |  4   |
|  2 | Datsun 710         | 22.8 |  4  | 108.0 |  93  | 3.85 | 2.320 | 18.61 |  1 |  1 |  4   |  1   |
|  3 | Hornet 4 Drive     | 21.4 |  6  | 258.0 | 110  | 3.08 | 3.215 | 19.44 |  1 |  0 |  3   |  1   |
|  4 | Hornet Sportabout  | 18.7 |  8  | 360.0 | 175  | 3.15 | 3.440 | 17.02 |  0 |  0 |  3   |  2   |

``` python
df_cars.tail()
```

|  | Model             | mpg  | cyl | disp  | hp   | drat | wt    | qsec  | vs | am | gear | carb |
|----|-------------------|------|-----|-------|------|------|-------|-------|----|----|------|------|
| 27 | Lotus Europa      | 30.4 |  4  | 95.1  | 113  | 3.77 | 1.513 | 16.90 |  1 |  1 |  5   |  2   |
| 28 | Ford Pantera L    | 15.8 |  8  | 351.0 | 264  | 4.22 | 3.170 | 14.50 |  0 |  1 |  5   |  4   |
| 29 | Ferrari Dino      | 19.7 |  6  | 145.0 | 175  | 3.62 | 2.770 | 15.50 |  0 |  1 |  5   |  6   |
| 30 | Maserati Bora     | 15.0 |  8  | 301.0 | 335  | 3.54 | 3.570 | 14.60 |  0 |  1 |  5   |  8   |
| 31 | Volvo 142E        | 21.4 |  4  | 121.0 | 109  | 4.11 | 2.780 | 18.60 |  1 |  1 |  4   |  2   |

---

### PROBLEM 2️⃣

Problem 2 has four parts in total, the first being to display the first five rows. To be able to do this, we to have to use the ``` .iloc[] ``` command and input the right conditions for the given problem. 

In python, : represents rows and :: represents columns, setting the range to be :5 makes it so that the range of rows to be printed are the first four rows of the cars data frame. Inputting the 2nd condition to be ::2 represents that starting from the first column, it will get the info from the first column and every column of 2 steps from the first column. ``` df_cars.iloc[:5,::2] ```

For the 2nd part of problem 2, we have to use ``` .loc[] ``` command and input the right conditions to display the row that contains the ‘Model’ of ‘Mazda RX4’. The conditions can be set as ``` df_cars['Model']=='Mazda RX4' ``` wherein the data frame of cars finds the row and only that row that has the car Mazda RX4.

For the 3rd part of problem 2, we have to use the same syntax as before in the 2nd part, only this time, we have to set a 2nd condition to only print out the 'cyl' information of the car 'Camaro Z28'.
We can do that by adding ``` [cyl] ``` at the end of the condition, the resulting code would be ``` df_cars.loc[(df_cars['Model']=='Camaro Z28'), ['cyl']] ```

For the last part of problem 2, to determine the 'cyl' information of the different cars, I created a list of the cars needed for the problem and used ``` .loc[] ``` and ``` .isin() ```commands. The right conditions can now be set for the given problem using these commands and the curated list of select cars. The ``` .isin() ``` serves to check if the car is on the list and the ``` .loc[] ``` serves to locate the information about the cars in the data frame. Finally placing ``` ['Model','cyl','gear'] ``` at the end of the condition, same as what we did for 3rd part, it prints out those columns only.

The resulting code will look like this ``` df_cars.loc[df_cars['Model'].isin(car_models),['Model','cyl','gear']] ``` 

### CODE

``` python

#start

# For part a.

# The condition :5 inside the square bracket selects the first 5 rows of the data frame but does not include the upper range, 5th row, to be printed
df_cars.iloc[:5,::2]

# The double colon ::2 slices every two steps of the column

# For part b.

# Uses .loc to locate and print the row that has the key value : 'Model' is equal to 'Mazda RX4'
df_cars.loc[df_cars['Model']=='Mazda RX4']


# Uses .loc to locate and print information that has the key value: 'Model' is equal to 'Mazda RX4'
# This time the syntax next to locating the model is the specified info/column to be printed
df_cars.loc[(df_cars['Model']=='Camaro Z28'), ['cyl']]

#Create list of car models needed for information
car_models = ['Mazda RX4','Ford Pantera L','Honda Civic']

#Uses .loc to locate the key values of the model of a car and prints specified information
#Uses .isin to check if any 'Model' in the data frame is in the created list of car models
df_cars.loc[df_cars['Model'].isin(car_models),['Model','cyl','gear']]

#end
```

### OUTPUT

for ``` For part a. ```

``` python
df_cars.iloc[:5,::2]

|     | Model            | cyl | hp  | wt    | vs | gear |
|-----|------------------|-----|-----|-------|----|------|
| 0   | Mazda RX4        | 6   | 110 | 2.620 | 0  | 4    |
| 1   | Mazda RX4 Wag    | 6   | 110 | 2.875 | 0  | 4    |
| 2   | Datsun 710       | 4   | 93  | 2.320 | 1  | 4    |
| 3   | Hornet 4 Drive   | 6   | 110 | 3.215 | 1  | 3    |
| 4   | Hornet Sportabout| 8   | 175 | 3.440 | 0  | 3    |
```

for ``` For part b. ```

``` python
df_cars.loc[df_cars['Model']=='Mazda RX4']

## Car Specifications

|     | Model     | mpg | cyl | disp | hp  | drat | wt   | qsec | vs | am | gear | carb |
|-----|-----------|-----|-----|------|-----|------|------|------|----|----|------|------|
| 0   | Mazda RX4 | 21  | 6   | 160  | 110 | 3.9  | 2.62 | 16.46| 0  | 1  | 4    | 4    |
