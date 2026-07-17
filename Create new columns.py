import pandas as pd

data = {
    'Name' : ['Amit', 'Rahul', 'Priya', 'Vikash'],
    'Age' : [24, 23, 22, 21],
    'City' : ['Mumbai', 'Delhi', 'Pune', 'Mumbai'],
    'Salary' : [35000, 40000, 50000, 55000]
}
df = pd.DataFrame(data)

# Create a new column for Annual Salary.
df['Annual_Salary'] = df['Salary'] * 12
print(df)

# If salary > 60k than 'High' otherwise 'Normal'
df['Salary_Level'] = df['Salary'].apply(lambda x: 'High' if x > 60000 else 'Normal')
print(df)