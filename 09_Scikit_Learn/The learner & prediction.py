import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Dataset
data = {
    'Hours': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Marks': [12, 24, 33, 41, 55, 68, 75, 82, 90, 99]
}

df = pd.DataFrame(data)

# X(Input) and Y(Output) splitting
x = df[['Hours']]
y = df['Marks']

# Split data into 80% train and 20% in test
x_train , x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state=42)

# Initialize the model
modal = LinearRegression()

# Teach the modal(.fit)
modal.fit(x_train, y_train)

print("Total rows:", len(x))
print("Training rows:", len(x_train))
print("Testing rows:", len(x_test))
print("Congratulation ! Your modal successfully trained.")

prediction = modal.predict(x_test)

result = pd.DataFrame({
    'Actual Marks (y_test)': y_test,
    'Modal Guesses (Prediction)': prediction
})

print("\n----Modal result-----")
print(result)