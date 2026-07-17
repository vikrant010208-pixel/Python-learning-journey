import pandas as pd

data = {
    'Name' : ['Amit', 'Rahul', 'Priya', 'Vikash'],
    'Age' : [24, 23, 22, 21],
    'City' : ['Mumbai', 'Delhi', 'Pune', 'Mumbai'],
    'Salary' : [35000, 40000, 50000, 55000]
}

df = pd.DataFrame(data)

# Make a group according to the city and find average salary
city_salary = df.groupby('City')['Salary'].mean()
print(city_salary)

# Do multiple calculation at a time
summary = df.groupby('City').agg({
    'Salary': ['mean', 'max'],
    'Age': 'count'  
})
print(summary)
