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

```

### OUTPUT

| --- | Model |
| --- | --- |
| 0 | Mazda RX4 |
| 1 | Mazda RX4 Wag |
| 2 | Datsun 710 |






