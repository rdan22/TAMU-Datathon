# -*- coding: utf-8 -*-
"""1. Data Wrangling

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16i6DAc9j6hGbl9vfJrAx0LNXguL2sEEm

Before we start, we need to import all the libraries we need. It's best practice to do this in the beginning. We'll be importing:

* [Pandas](https://pandas.pydata.org/pandas-docs/stable/): Library that will be used to load and manipulate the data
* [Matplotlib](https://matplotlib.org): Used to visualize our data

Some other libraries might be imported for administrative reasons, but they won't be related to what we'd be learning in this lesson.

# Lesson 1: The Data Science Process

What question are you trying to answer? Once you have that, your data science adventure begins. You must go out and find your data. More often than not, the data you have will not be in the form you want it to be in. You'll need to load, clean, transform and, most importantly, understand it (the top part of this diagram). Let's begin!

![alt text](https://revsearch-assets.s3.amazonaws.com/images/ds_process1.png)

## Learning Objectives:

* Learn the data science enviroment:
  * Python
  * Jupyter Notebook
  * Pandas
* Learn the vocabularly of data: 
  * Table Data (versus unstructured data)
  * Features and target (columns)
  * Observations (rows)
* Learn the basics of reading/loading data using Pandas
* Learn how to clean data and deal with missing values
* Learn how to visualize data and understand data better
* Communicate effectively through data


### Definitions
  * **Jupyter Notebook:** The Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text. You type the code in *cells* here in your browser. When you run a cell, your code runs on the cloud and the results are shown in your browser.
  * **Target Column:** This is the variable that you're trying to predict given other values. This is also called the _response_ / _predicted_ / _dependent_ / _label_ variable.
  * **Feature Columns:** These are the variables that we use to calculate/predict the value of the target. These are also called _explanatory_ / _predictor_ / _feature_ / _signal_ variables. 
  * **Observations:** We have one observation per row. A observation is one instance of our data. In the below, a observation is a basketball player.
  * **Tablular Data:** Data that has been organized into a matrix or table, i.e. into columns and rows. Unstructured data may be speech recordings or pictures. We will be dealing with tabular data. Note, we often interchange the words columns<>variables and rows<>observations.

<img src="https://media.geeksforgeeks.org/wp-content/uploads/finallpandas.png" alt="alt" width="500"/>
"""

# We import the required libraries before using them
# In a single Jupyter Notebook, libraries should be imported once and can be 
# used throughout the notebook

# The 'as' keyword just renames the library, making it easier for us to access it
import pandas as pd
from matplotlib import pyplot as plt

"""## Pandas

Pandas is one of the top (if not the top) data manipulation and analysis libraries for Python right now. It loads data into these easy to access and manipulate structures called _DataFrames_. Data in these is 'arranged' similar to what you might have seen in a spreasheet, with rows specifying data points and columns specifying certain categories/features/variables.

In the following cell we're just setting up some configurations for the library. This will change how the library outputs the data for us to see.
"""

pd.options.display.float_format = "{:.2f}".format # This will make pandas output fractions up to 2 decimal places
pd.options.display.max_rows = 10 # Pandas will output at max 10 rows from the data

"""## Research Question

We'll be using the a dataset from Kaggle which contains nutritional data and customer ratings for 77 different cereals. You can find more information about it [here](https://www.kaggle.com/crawford/80-cereals). 

Our question is "*Can we predict the consumer **cereal rating** using the other features supplied in the dataset*?"

## Data Collection

The dataset we're going to used is stored on Kaggle, not locally on our machine. However, we can just supply the link to the file to Pandas and it will take care of the loading for us.
"""

# Here we load a dataset from a url. You can check out the raw dataset by copying the url into your browser!
cereal_data = pd.read_csv("https://cosmos-api-prod-datasetsbucket-iuph41amgzfj.s3.amazonaws.com/cereal.csv", sep=",")

# This will give us the first few rows of the data that was loaded
cereal_data.head()

"""## Data Cleaning

You loaded your data. How do you get a quick look at it? One of the simple and effective ways to sanity check your data is to check the descriptive statistics for it. We look at the mean, median, max, min and see if they make sense.
"""

# This will give us descriptive statistics (such as count, mean, min/max, 
# standard deviation) for each column in out dataset
descriptive_stats = cereal_data.describe()

# Just having a variable name on a the last line of a cell outputs the value of
# that variable
descriptive_stats

"""**Note:** You can see that the _count_ for some of the columns is less than 77. This is so because these columns have some missing values. 

### Handling Missing Values (Imputation)

Most datasets you encounter will not be perfect and will require some cleaning and processing before you can use them. An important part of the cleaning process is dealing with missing values. There are multiple ways of doing this, and we'll discuss a few of them.

#### Replace missing values with zero

Missing values or a value of "NaN" don't agree with most models, and you'd end up getting errors when trying to train one on a dataset with missing data. One way to fix this is to replace all missing values with zero.
"""

# The function will create a copy of the data with the missing values filled in
cereal_data_missing_to_zero = cereal_data.fillna(0)

# Note that all columns have a count of 77 now
cereal_data_missing_to_zero.describe()

"""#### Replace missing values with mean values for that column

Another method of dealing with missing values is replacing them with the mean value for that column/feature.
"""

cereal_data_missing_to_mean = cereal_data.fillna(cereal_data.mean())

# We'll use this data as our main dataset
cereal_data = cereal_data_missing_to_mean 

cereal_data_missing_to_mean.describe()

"""#### Picking which type of imputation
You can see the difference in mean, standard deviation and other metrics between the two methods for the columns with missing values (carbo, potass, and sugars). Note, for example in potass, that the mean is lower when imputing with 0's. Why is that? We have to be careful when imputing! But imputing with the mean is normally a good starting point. (Median is better when our data has outliers or a non-normal distribution.) Whatever you do, make sure to document it.

## Exploration & Visualization

Matplotlib is a widely used library for visualizing data. We'll start off with basic scatter plots to check *correlation* between the **rating** and other features.

Looking at how your data is correlated with what your trying to predict is an important step. It helps you choose predictors to use and what kind of a model to consider.
"""

cereal_data = pd.read_csv("https://cosmos-api-prod-datasetsbucket-iuph41amgzfj.s3.amazonaws.com/cereal.csv", sep=",")
cereal_target_name = "rating"
cereal_target = cereal_data[cereal_target_name]
fig = plt.figure(figsize=(15, 15))

# The enumerate function will give us the index as well as the value
for (i, column) in enumerate(list(cereal_data.columns)):
  if(column == cereal_target_name) or (column == "name"):
    continue
  plt.subplot(5,3,i)
  plt.scatter(cereal_data[column], cereal_data[cereal_target_name])
  plt.xlabel(column)
  plt.ylabel(cereal_target_name)
  
plt.show()

"""**Note:** From the plots, we can see:
* A weak negative linear relationship between the rating and sugar 
* A positive linear relationship between rating and fiber.

#### Pearson’s Product-Moment Correlation
The most common measure of correlation is Pearson’s product-moment correlation, which is commonly referred to simply as the correlation, the correlation coefficient, or just the letter r (you can ignore the p for now)
:

- A correlation of 1 indicates a perfect positive correlation.
- A correlation of -1 indicates a perfect negative correlation.
- A correlation of 0 indicates that there is no relationship between the different variables.
- Values between -1 and 1 denote the strength of the correlation, as shown in the example below.

<img src="https://46gyn61z4i0t1u1pnq2bbk2e-wpengine.netdna-ssl.com/wp-content/uploads/2018/05/Pearson%E2%80%99s-Product-Moment-Correlation.png" alt="alt" width="500"/>

[source](https://www.displayr.com/what-is-correlation/)


#### Heatmap
Another way to view correlation between all variables in your dataset is a heatmap. If we denote the heatmap as $A$, then each $A_{ij}$ entry/box in the heatmap corresponds to the correlation between variables $i$ and $j$. Note that $-1<A_{ij}<1$. Also, note that $A_{ii}=1$, meaning that each variable is perfectly correlated with itself!
"""

# seaborn is another plotting library, like matplotlib
import seaborn as sns
corrmat = cereal_data.corr()
f, ax = plt.subplots(figsize=(9, 9))
f = sns.heatmap(corrmat, vmax=.8, square=True, annot=True, cbar=False)

"""# Challenges - Data Wrangling

For this lesson's challenge, we'll be using the dataset from 1985 Ward's Automotive Yearbook that is part of the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets) under [Automobile Data Set](https://archive.ics.uci.edu/ml/datasets/automobile).  You can find a description of the data at [https://archive.ics.uci.edu/ml/datasets/automobile](https://archive.ics.uci.edu/ml/datasets/automobile). 

### Getting Points:

Each section of the challenge will have some instructions, please **carefully read these**. They will instruct you on how to 'submit' your answers. This will usually involve setting a variable to a specific value / DataFrame. 

The cell that follows the one that you edit will contain code that will submit your answer. **DO NOT CHANGE THIS CODE**. If you end up altering it, please seek out one of the volunteers and they'll help you out. 

## Set the 'email' variable below to the email you used to sign up for Cosmos (and run the cell)
"""

# These are internal libraries used to manage your submissions to the challenges
# You won't have to install / import these in your normal usage
!pip install pycosmos --upgrade --quiet
from pycosmos import CosmosProject
tamu_datathon = CosmosProject('tamu_datathon')

email = "" # Enter your email here

"""## Loading & Describing Data - 10 Points

You can find the dataset we'll be loading at this link: https://cosmos-api-prod-datasetsbucket-iuph41amgzfj.s3.amazonaws.com/cars_data.csv

Load this data into pandas and calculate the descriptive statistics for it.

### Tasks to get points
* Set a variable named '*symboling_descriptive*' equal to the descriptive statistics for the column 'symboling'. You can get a column from a dataframe with square brackets. For example, if you have a dataframe named df and a column in df named col, df["col"] will get that column.
* Run the cell that follows this one
* Check the output of that cell to see whether you suceeded or whether any changes to your code are needed
"""

# ENTER YOUR CODE HERE
import pandas as pd

cars_data = pd.read_csv("https://cosmos-api-prod-datasetsbucket-iuph41amgzfj.s3.amazonaws.com/cars_data.csv", sep=",")

# Set this variable equal to your answer
symboling_descriptive = cars_data["symboling"].describe()

#@title Run to get points for: Loading & Describing Data (10 Points)
tamu_datathon.judge_attempt('load_describe_data', email, list(symboling_descriptive))

"""## Dealing with Missing Data - 10 Points

The data we previously loaded contains missing values. Now we need to deal with them. Replacing missing values with zeroes is trivial, so let's try something a little bit more difficult.

### Tasks to get points
* Replace the missing values in the data previously loaded with the **mean** of that column/feature
* After doing the step above, set the variable *losses_descriptive* to the descriptive statistics of the 'losses' column **after replacing the missing values**
* Run the cell that follows this one
* Check the output of that cell to see whether you suceeded or whether any changes to your code are needed
"""

# ENTER YOUR CODE HERE
import pandas as pd

cars_data = pd.read_csv("https://cosmos-api-prod-datasetsbucket-iuph41amgzfj.s3.amazonaws.com/cars_data.csv", sep=",")

cars_data_missing_to_mean = cars_data.fillna(cars_data.mean())

cars_data = cars_data_missing_to_mean 

# Set this variable equal to your answer
losses_descriptive = cars_data_missing_to_mean["losses"].describe()

#@title Run to get points for: Dealing with Missing Data (10 Points)
tamu_datathon.judge_attempt('deal_with_missing_data', email, list(losses_descriptive))

"""## Visualizing Data - 10 Points

Now that we have the data ready, we can start looking at it. We'll be visualizing some features/columns and looking at their relationships.

### Tasks to get points
* Create a plot with the _price_ column on the y-axis and the _weight_ column on the x-axis
* Check the relationship between these variables, and store it in the *price_weight_relationship* variable
* Run the cell that follows this one
* Check the output of that cell to see whether you suceeded or whether any changes to your code are needed

## Note:

The values of the relationship can be 'Positive', 'Negative' or 'No Relationship'.
"""

# ENTER YOUR CODE HERE
cars_data = pd.read_csv("https://cosmos-api-prod-datasetsbucket-iuph41amgzfj.s3.amazonaws.com/cars_data.csv", sep=",")

cars_target_name = "price"
fig = plt.figure(figsize=(15, 15))

for(i, column) in enumerate(list(cars_data.columns)):
  if(column == cars_target_name) or (column == "weight"):
    continue
  plt.scatter(cars_data[cars_target_name], cars_data["weight"])
  plt.xlabel("weight")
  plt.ylabel(cars_target_name)
  
plt.show()

price_weight_relationship = "Positive"

#@title Run to get points for: Visualizing Data (10 Points)
tamu_datathon.judge_attempt('visualize_data', email, [price_weight_relationship])
