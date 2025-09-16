import numpy as np
import matplotlib.pyplot as plt

# Define vectors
vec_a = np.array([2, 0, 0])
vec_b = np.array([0, 6, -2])
cross_vec = np.array([3, 2, 6])

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

origin = np.zeros(3)

# Plot vectors
ax.quiver(*origin, *vec_a, color='r', label=r'$\vec{a}$', linewidth=2)
ax.quiver(*origin, *vec_b, color='b', label=r'$\vec{b}$', linewidth=2)
ax.quiver(*origin, *cross_vec, color='g', label=r'$\vec{a} \times \vec{b}$', linewidth=2)

# Label vectors
ax.text(*(vec_a * 1.1), r'$\vec{a}$', color='r', fontsize=12)
ax.text(*(vec_b * 1.1), r'$\vec{b}$', color='b', fontsize=12)
ax.text(*(cross_vec * 1.1), r'$\vec{a} \times \vec{b}$', color='g', fontsize=12)

# Axes settings
ax.set_xlim([-1, 8])
ax.set_ylim([-4, 8])
ax.set_zlim([-4, 8])
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('Vectors $\\vec{a}$, $\\vec{b}$, and $\\vec{a} \\times \\vec{b}$ with angle = 30°')

ax.grid(True)
ax.legend()

plt.show()
