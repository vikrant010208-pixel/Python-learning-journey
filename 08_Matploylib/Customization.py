import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
views = [100, 250, 200, 400, 500]

# Colour, linestyle and marker for highlighting the points
plt.plot(days, views, color = 'red', linestyle = '--', marker = 'o', linewidth = 2)

plt.title("Customized line plot")
plt.grid(True) # Add grid lines in background.
plt.show()