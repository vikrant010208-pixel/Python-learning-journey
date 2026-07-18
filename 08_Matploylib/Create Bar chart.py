import matplotlib.pyplot as plt

cities = ['Delhi', 'Mumbai', 'Pune', 'Bangalore']
population = [30, 30, 10, 15] # In millions

# Replace plot() from bar()
plt.bar(cities, population, color = ['red', 'blue', 'green', 'yellow'])
plt.title("City population (In millions)")
plt.show()