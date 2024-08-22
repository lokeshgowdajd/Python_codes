import matplotlib.pyplot as plt
import numpy as np
data=[12,455,5555,555,214,45]

plt.hist(data)
plt.title("data for visuvazed")
plt.xlabel("volume")
plt.ylabel("mass")
plt.show()
plt.close()


# Generate some sample data (you can replace this with your own data)
x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)
X, Y = np.meshgrid(x, y)
Z = 3 * (1 - X)**2 * np.exp(-(X**2) - (Y + 1)**2) - 10 * (X/5 - X**3 - Y**5) * np.exp(-X**2 - Y**2) - 1/3 * np.exp(-(X + 1)**2 - Y**2)

# Create a 3D surface plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='red')
ax.set_title('Volcano Crater')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.view_init(60, 35)  # Adjust the view angle

plt.show()
plt.close()
