import matplotlib.pyplot as plt
import numpy as np

# Generate some data
x = np.linspace(-np.pi, np.pi, 100)
y = np.sin(x)

# Create a plot
fig, ax = plt.subplots()
ax.plot(x, y)

# Customize the plot
ax.set_title("Sine Wave")
ax.set_xlabel("x")
ax.set_ylabel("sin(x)")
ax.grid(True)

# Save the plot as a PNG image
fig.savefig("sine_wave.png")

# Display the plot
plt.show()
