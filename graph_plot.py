import matplotlib.pyplot as plt

# Data for plotting
x1 = [2, 4, 5, 7]
y1 = [2, 3, 6, 10]

x2 = [1, 3, 6, 8]
y2 = [1, 4, 5, 9]

x3 = [0, 2, 4, 6, 8]
y3 = [3, 5, 7, 9, 11]

# Plot multiple lines with different styles
plt.plot(x1, y1, label="Line 1 (Solid)", linestyle='-', color='blue', marker='o')
plt.plot(x2, y2, label="Line 2 (Dashed)", linestyle='--', color='green', marker='s')
plt.plot(x3, y3, label="Line 3 (Dotted)", linestyle=':', color='red', marker='d')

# Adding grid
plt.grid(color='gray', linestyle='--', linewidth=0.5)

# Adding labels and title
plt.xlabel("X Axis", fontsize=12, color='purple')
plt.ylabel("Y Axis", fontsize=12, color='purple')
plt.title("Enhanced Demo Graph", fontsize=14, color='darkblue')

# Adding a legend
plt.legend(loc="upper left")

# Adjusting limits for better view
plt.xlim(0, 9)
plt.ylim(0, 12)

# Show the plot
plt.show()
