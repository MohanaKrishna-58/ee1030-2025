import ctypes
import numpy as np
import matplotlib.pyplot as plt
import math

# --- Load C library ---
lib = ctypes.CDLL("./vector.so")
lib.angle_between.argtypes = [ctypes.c_double, ctypes.c_double,
                              ctypes.c_double, ctypes.c_double, ctypes.c_double]
lib.angle_between.restype = ctypes.c_double

# --- Given values ---
a_mag = 2.0
b_mag = 7.0
cross = np.array([3.0, 2.0, 6.0])

# --- Call C function ---
theta = lib.angle_between(a_mag, b_mag, cross[0], cross[1], cross[2])
print(f"Angle between a and b = {theta:.2f} degrees")

# --- Define vectors for visualization ---
a = np.array([a_mag, 0, 0])  # vector a along x-axis
b = np.array([b_mag*math.cos(math.radians(theta)),
              b_mag*math.sin(math.radians(theta)),
              0])

# --- Plot in 3D ---
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

ax.quiver(0,0,0, *a, color='r', label='a (|a|=2)')
ax.quiver(0,0,0, *b, color='b', label='b (|b|=7)')
ax.quiver(0,0,0, *cross, color='g', label='a × b')

ax.text(*a, "a", color="red")
ax.text(*b, "b", color="blue")
ax.text(*cross, "a×b", color="green")

ax.set_xlim([0,8])
ax.set_ylim([0,8])
ax.set_zlim([0,8])
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("Angle Between a and b with Cross Product")

ax.legend()
plt.show()