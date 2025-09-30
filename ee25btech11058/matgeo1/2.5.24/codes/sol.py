import math
import numpy as np
import matplotlib.pyplot as plt

a_norm = 2.0
b_norm = 7.0
cross_ab = np.array([3.0, 2.0, 6.0])

cross_norm = np.linalg.norm(cross_ab)
dot_sq = (a_norm**2) * (b_norm**2) - cross_norm**2
dot_val = math.sqrt(dot_sq)

cos_theta = dot_val / (a_norm * b_norm)
theta_rad = math.acos(cos_theta)
theta_deg = math.degrees(theta_rad)

print(f"Angle between a and b = {theta_deg:.2f} degrees")

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.quiver(0, 0, 0, a_norm, 0, 0, color='r', label='a')
ax.quiver(0, 0, 0, 0, b_norm, 0, color='g', label='b')
ax.quiver(0, 0, 0, cross_ab[0], cross_ab[1], cross_ab[2], color='b', label='a×b')
ax.set_xlim([0, 8])
ax.set_ylim([0, 8])
ax.set_zlim([0, 8])
ax.legend()
plt.show()
