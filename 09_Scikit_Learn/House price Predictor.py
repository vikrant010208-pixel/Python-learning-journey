import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Dataset: Kamre (Rooms) vs Ghar ki Keemat (Price in Lakhs)
data = {
    'Rooms': [1, 2, 3, 4, 5, 6, 7, 8],
    'Price_Lakhs': [12, 24, 36, 48, 60, 72, 84, 96]
}
df = pd.DataFrame(data)

# ---------------------------------------------------------
# Start code here
# ---------------------------------------------------------

X = df[['Rooms']]
y = df['Price_Lakhs']


X_train,  X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = LinearRegression()
model.fit(X_train, y_train)

prediction = model.predict(X_test)

try:
    result = pd.DataFrame({
        'Real price': y_test,
        'Model Ka Guess': prediction
    })
    print("\n--- AI Property Dealer ---")
    print(result)
except Exception as e:
    print("\nOops! Error aa gaya:", e)