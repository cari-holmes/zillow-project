# Estimate Home Values on Zillow

### Setup:

Create env.py file with the following contents:
  - host = "Database IP Address"
  - user = "Your Username"
  - password = "Your Password"
  
Replace with your specific information.

You will find the necessary functions for this project in the .py files located within this repository. 

## Goal:

We want to be able to predict the values of single unit properties that the tax district assesses using the property data from those whose last transaction was during the "hot months" (in terms of real estate demand) of May and June in 2017. We also need to find the distribution of tax rates for each county in the data.

Work through each step of the Data Science Pipeline using Linear Regression.
- Acquire
- Prep
- Split and Scale Data
- Exploration
- Feature Selection
- Modeling and Evaluation

### Acquisition
I gathered the data from a SQL database, joining tables as needed to meet all of the requirements necessary to answer my question and to have a dataframe ready to prepare.

### Preparation
I handled missing values, changed variables to the appropriate data type and more in a reproducible manner.

### Exploration
I ran statistical testing to find any correlation between my features and my target variable.

### Feature Selection
Based off of the statistical testing, I chose what features I wanted to add into my model.

### Modeling
I developed several sklearn linear regression models to find the one that best predicted home value.
