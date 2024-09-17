{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "5dd6f88d-e9ab-4685-a406-244e613735cb",
   "metadata": {},
   "source": [
    "# Programming Assignment 3 - PYTHON DATA ANALYSIS (PANDAS)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d36d7f9b-e81d-4763-9c1b-062d1c17d6e5",
   "metadata": {},
   "source": [
    "### PROBLEM 2: Save your file as Surname_Pandas-P2.py"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5b89b72a-21d1-40d5-840b-abd9e1cc4ffb",
   "metadata": {},
   "source": [
    "##### Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and \n",
    "##### indexing operations."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "288a5454-07d0-40aa-a51b-abc0b3ef29fd",
   "metadata": {},
   "outputs": [],
   "source": [
    "#start\n",
    "\n",
    "#Import library of PANDAS\n",
    "import pandas as pd\n",
    "\n",
    "#Load csv file into a data frame named cars using pandas\n",
    "df_cars = pd.read_csv('cars.csv')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4cf30c2d-786e-4657-87e3-7ad6bfb0bca4",
   "metadata": {},
   "source": [
    "##### a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7…) of cars."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "d6625282-e697-43c4-9a3e-68c25e2a8d8d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Model</th>\n",
       "      <th>cyl</th>\n",
       "      <th>hp</th>\n",
       "      <th>wt</th>\n",
       "      <th>vs</th>\n",
       "      <th>gear</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Mazda RX4</td>\n",
       "      <td>6</td>\n",
       "      <td>110</td>\n",
       "      <td>2.620</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Mazda RX4 Wag</td>\n",
       "      <td>6</td>\n",
       "      <td>110</td>\n",
       "      <td>2.875</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Datsun 710</td>\n",
       "      <td>4</td>\n",
       "      <td>93</td>\n",
       "      <td>2.320</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Hornet 4 Drive</td>\n",
       "      <td>6</td>\n",
       "      <td>110</td>\n",
       "      <td>3.215</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Hornet Sportabout</td>\n",
       "      <td>8</td>\n",
       "      <td>175</td>\n",
       "      <td>3.440</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               Model  cyl   hp     wt  vs  gear\n",
       "0          Mazda RX4    6  110  2.620   0     4\n",
       "1      Mazda RX4 Wag    6  110  2.875   0     4\n",
       "2         Datsun 710    4   93  2.320   1     4\n",
       "3     Hornet 4 Drive    6  110  3.215   1     3\n",
       "4  Hornet Sportabout    8  175  3.440   0     3"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#start\n",
    "\n",
    "# The condition :5 inside the square bracket selects the first 5 rows of the DataFrame but does not include the upper range, 5th row, to be printed\n",
    "\n",
    "df_cars.iloc[:5,::2]\n",
    "\n",
    "# The double colon ::2 slices every two steps of the column\n",
    "\n",
    "#end"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "73243ba0-df19-48ac-b2d3-9a4a0e3f37b7",
   "metadata": {},
   "source": [
    "##### b. Display the row that contains the ‘Model’ of ‘Mazda RX4’."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "38ecc636-82e2-46f7-bb29-1bfd368e664b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Model</th>\n",
       "      <th>mpg</th>\n",
       "      <th>cyl</th>\n",
       "      <th>disp</th>\n",
       "      <th>hp</th>\n",
       "      <th>drat</th>\n",
       "      <th>wt</th>\n",
       "      <th>qsec</th>\n",
       "      <th>vs</th>\n",
       "      <th>am</th>\n",
       "      <th>gear</th>\n",
       "      <th>carb</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Mazda RX4</td>\n",
       "      <td>21.0</td>\n",
       "      <td>6</td>\n",
       "      <td>160.0</td>\n",
       "      <td>110</td>\n",
       "      <td>3.9</td>\n",
       "      <td>2.62</td>\n",
       "      <td>16.46</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       Model   mpg  cyl   disp   hp  drat    wt   qsec  vs  am  gear  carb\n",
       "0  Mazda RX4  21.0    6  160.0  110   3.9  2.62  16.46   0   1     4     4"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Uses .loc to locate and print the row that has the key value : 'Model' is equal to 'Mazda RX4'\n",
    "df_cars.loc[df_cars['Model']=='Mazda RX4'] "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "724c95ea-06d7-4171-8b5e-05f2947c6ddc",
   "metadata": {},
   "source": [
    "##### c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "62525dd1-43c9-4ce5-8c13-ba3d18f0fe6b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>cyl</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>23</th>\n",
       "      <td>8</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    cyl\n",
       "23    8"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Uses .loc to locate and print information that has the key value : 'Model' is equal to 'Mazda RX4'\n",
    "#This time the syntax next to locating the model is the specified info/column to be printed\n",
    "df_cars.loc[(df_cars['Model']=='Camaro Z28'), ['cyl']]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2c851ce7-0f95-43cb-90cc-92c469d62994",
   "metadata": {},
   "source": [
    "##### d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 \n",
    "##### Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 121,
   "id": "b3ca82bd-0630-4b9b-83ff-480a7c7f4fa0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Model</th>\n",
       "      <th>cyl</th>\n",
       "      <th>gear</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Mazda RX4</td>\n",
       "      <td>6</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>Honda Civic</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>28</th>\n",
       "      <td>Ford Pantera L</td>\n",
       "      <td>8</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             Model  cyl  gear\n",
       "0        Mazda RX4    6     4\n",
       "18     Honda Civic    4     4\n",
       "28  Ford Pantera L    8     5"
      ]
     },
     "execution_count": 121,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Create list of car models needed for information\n",
    "car_models = ['Mazda RX4','Ford Pantera L','Honda Civic']\n",
    "\n",
    "#Uses .loc to locate the key values of the model of a car and prints specified information\n",
    "#Uses .isin to check if any 'Model' in the dataframe is in the created list of car models\n",
    "df_cars.loc[df_cars['Model'].isin(car_models),['Model','cyl','gear']]\n",
    "\n",
    "#end"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
