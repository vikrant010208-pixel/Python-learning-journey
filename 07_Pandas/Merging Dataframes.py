import pandas as pd 

# Two diffrents Data frames
emp_data = pd.DataFrame({'Emp_ID': [1, 2, 3], 'Name': ['Amit', 'Rahul', 'Priya']})
dept_data = pd.DataFrame({'Emp_ID': [1, 2, 4], 'Department': ['IT', 'HR', 'Finance']})

# Merger both as like SQL Inner Join om 'Emp_ID'
merged_df = pd.merge(emp_data, dept_data, on='Emp_ID', how='inner')
print(merged_df)