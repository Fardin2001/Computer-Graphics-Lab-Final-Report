import matplotlib.pyplot as plt
# Original triangle coordinates
O = (0, 0)
B = (1, 0)
A = (1, 1)
# Shearing functions
def shear_x(point, shx):
x, y = point
return x + shx * y, y
def shear_y(point, shy):
x, y = point
return x, y + shy * x
# Shearing factors
Shx = 2
Shy = 2
# Apply X-axis shearing
O_x = shear_x(O, Shx)
B_x = shear_x(B, Shx)
A_x = shear_x(A, Shx)
# Apply Y-axis shearing
O_y = shear_y(O, Shy)
B_y = shear_y(B, Shy)
34
A_y = shear_y(A, Shy)
# Coordinates for plotting
orig_x = [O[0], B[0], A[0], O[0]]
orig_y = [O[1], B[1], A[1], O[1]]
shear_x_x = [O_x[0], B_x[0], A_x[0], O_x[0]]
shear_x_y = [O_x[1], B_x[1], A_x[1], O_x[1]]
shear_y_x = [O_y[0], B_y[0], A_y[0], O_y[0]]
shear_y_y = [O_y[1], B_y[1], A_y[1], O_y[1]]
# Function to annotate points
def annotate_points(points, names, ax):
for (x, y), name in zip(points, names):
ax.text(x + 0.05, y + 0.05, f"{name}({x}, {y})", fontsize=8)
# Plotting
plt.figure(figsize=(10, 4))
# X-axis shearing plot
ax1 = plt.subplot(1, 2, 1)
ax1.plot(orig_x, orig_y, 'bo-', label='Original')
ax1.plot(shear_x_x, shear_x_y, 'ro-', label=f'Sheared in X-axis (Shx={Shx})')
ax1.axhline(0, color='gray', linewidth=0.5)
ax1.axvline(0, color='gray', linewidth=0.5)
ax1.set_title("Shearing in X-axis")
ax1.axis('equal')
ax1.grid(True)
ax1.legend()
# Annotating original & sheared points for X-axis shear
annotate_points([O, B, A], ["O", "B", "A"], ax1)
annotate_points([O_x, B_x, A_x], ["O'", "B'", "A'"], ax1)
35
# Y-axis shearing plot
ax2 = plt.subplot(1, 2, 2)
ax2.plot(orig_x, orig_y, 'bo-', label='Original')
ax2.plot(shear_y_x, shear_y_y, 'ro-', label=f'Sheared in Y-axis (Shy={Shy})')
ax2.axhline(0, color='gray', linewidth=0.5)
ax2.axvline(0, color='gray', linewidth=0.5)
ax2.set_title("Shearing in Y-axis")
ax2.axis('equal')
ax2.grid(True)
ax2.legend()
# Annotating original & sheared points for Y-axis shear
annotate_points([O, B, A], ["O", "B", "A"], ax2)
annotate_points([O_y, B_y, A_y], ["O'", "B'", "A'"], ax2)
plt.show()
# Print new coordinates
print("Shearing in X-axis:")
print(f"O' = {O_x}")
print(f"B' = {B_x}")
print(f"A' = {A_x}")
print("\nShearing in Y-axis:")
print(f"O' = {O_y}")
print(f"B' = {B_y}")
print(f"A' = {A_y}")