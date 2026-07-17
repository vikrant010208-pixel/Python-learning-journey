import pandas as pd

# Dictionary to data frame
data = {
    'Name' : ['Amit', 'Rahul', 'Priya', 'Vikash'],
    'Age' : [24, 23, 22, 21],
    'City' : ['Mumbai', 'Delhi', 'Pune', 'Mumbai'],
    'Salary' : [35000, 40000, 50000, 55000]
}

df = pd.DataFrame(data)

# Display data
print(df.head())

# Display specific data
print(df.head(1))

# Data types and summery of missing values
print(df.info())

# Numerical to static data(Mean, min., max.)
print(df.describe())