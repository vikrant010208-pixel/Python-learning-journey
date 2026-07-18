import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
views = [100, 250, 200, 400, 500]

plt.plot(days, views)

# Make label or tittle for deigning chart
plt.title("Youtube channel Daily views")
plt.xlabel("Day")
plt.ylabel("Number of views")

# Display chart
plt.show()
