import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y1 = [10, 20, 30, 40]
y2 = [40, 30, 20, 10]

# Create chart 1 row and 2 columns and fig size = (width, height) in inches
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize = (10,4))

# First chart
ax1.plot(x, y1, color = 'blue', marker = 'x')
ax1.set_title("Sales Growth") #Here use ste_title for title
ax1.set_label("Quarter")

# 2nd chart
ax2.bar(x, y2, color = 'green')
ax2.set_title("Expenses")

# For Clean layout to avoid overlap
plt.tight_layout()
plt.show()