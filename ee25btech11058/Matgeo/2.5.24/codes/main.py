import ctypes, math
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
lib = ctypes.CDLL("./vector.so")
# Define C function signature
lib.angle_from_cross_c.argtypes = [ctypes.c_double, ctypes.c_double,
                                 ctypes.c_double, ctypes.c_double, ctypes.c_double]
lib.angle_from_cross_c.restype = ctypes.c_double

# Input values
a_mag, b_mag = 2.0, 7.0
cross = np.array([3.0, 2.0, 6.0])

# Call the C function
theta_deg = lib.angle_from_cross_c(a_mag, b_mag, *cross)
theta_rad = math.radians(theta_deg)

# --- Visualization ---
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')
a = np.array([a_mag, 0, 0])
b = np.array([b_mag*math.cos(theta_rad), b_mag*math.sin(theta_rad), 0])
ax.quiver(0,0,0, *a, color='r', label=f'a (|a|={a_mag})')
ax.quiver(0,0,0, *b, color='b', label=f'b (|b|={b_mag})')
ax.quiver(0,0,0, *cross, color='g', label='a x b')
ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
ax.legend()
plt.show()