import matplotlib.pyplot as plt
import numpy as np

# Generate some data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a scatter plot
fig, ax = plt.subplots()
ax.scatter(x, y)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Scatter Plot of Sine Wave')

# Save the plot as a PNG file
fig.savefig('plot.png')
