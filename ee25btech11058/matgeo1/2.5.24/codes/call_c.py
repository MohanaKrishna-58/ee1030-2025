import subprocess

# 1. Compile the C program
subprocess.run(["gcc", "Angle between two vectors.c", "-o", "Angle between two vectors"])

# 2. Run the compiled C program
result = subprocess.run(["./Angle between two vectors"], capture_output=True, text=True)

# 3. Print the output from the C program
print(result.stdout)
