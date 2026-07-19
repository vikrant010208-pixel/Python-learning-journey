import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Salary Dataset
data = {
    'Experience_Years': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Salary_Thousand': [15, 25, 35, 45, 55, 65, 75, 85, 95, 105]
}
df = pd.DataFrame(data)


X = df[['Experience_Years']]
y = df['Salary_Thousand']


X_train, X_test, y_train, y_test = (train_test_split(X, y, test_size=0.2, random_state=42))

# Challenge 3: Model ko Train (fit) karo
model = LinearRegression()
model.fit(X_train, y_train)


predictions = model.predict(X_test)


try:
    result = pd.DataFrame({
        'Real Salary': y_test,
        'Model Guesses': predictions
    })
    print("\n--- AI HR Salary Guesses ---")
    print(result)
except Exception as e:
    print("\nOops! Something Wrong here:", e)