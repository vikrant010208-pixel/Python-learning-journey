import pandas as pd
data = {
    'Name': ['Amit', 'Rahul', 'Priya', 'Neha', 'Vikash'],
    'Age': [24, 27, 22, 32, 29],
    'City': ['Delhi', 'Mumbai', 'Delhi', 'Pune', 'Mumbai'],
    'Salary': [50000, 65000, 45000, 80000, 70000]
}

df = pd.DataFrame(data)

# Data whose age is greater than 25.
old_peeps = df[df['Age'] > 25]
print(old_peeps)

# Data people from delhi and salary is grater than 45 thousand
rich_delhiites = df[(df['City'] == 'Delhi') & (df['Salary'] > 45000)]
print(rich_delhiites)