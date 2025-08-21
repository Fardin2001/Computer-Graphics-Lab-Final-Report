import matplotlib.pyplot as plt
# Original triangle points
A = (3, 4)
B = (6, 4)
C = (5, 6)
# Reflection formulas
def reflect_x(x, y):
return x, -y
def reflect_y(x, y):
return -x, y
# Apply reflections
A_x = reflect_x(*A)
B_x = reflect_x(*B)
C_x = reflect_x(*C)
A_y = reflect_y(*A)
B_y = reflect_y(*B)
C_y = reflect_y(*C)
# Prepare coordinates for plotting
orig_x = [A[0], B[0], C[0], A[0]]
orig_y = [A[1], B[1], C[1], A[1]]
xaxis_x = [A_x[0], B_x[0], C_x[0], A_x[0]]
xaxis_y = [A_x[1], B_x[1], C_x[1], A_x[1]]
30
yaxis_x = [A_y[0], B_y[0], C_y[0], A_y[0]]
yaxis_y = [A_y[1], B_y[1], C_y[1], A_y[1]]
# Plotting
plt.figure(figsize=(7,7))
# Original triangle
plt.plot(orig_x, orig_y, 'b-o', label='Original Triangle')
plt.text(A[0], A[1], f"A{A}", fontsize=9, ha='right')
plt.text(B[0], B[1], f"B{B}", fontsize=9, ha='right')
plt.text(C[0], C[1], f"C{C}", fontsize=9, ha='right')
# Reflection along X-axis
plt.plot(xaxis_x, xaxis_y, 'r-o', label="Reflected along X-axis")
plt.text(A_x[0], A_x[1], f"A'({A_x[0]}, {A_x[1]})", fontsize=9, ha='right')
plt.text(B_x[0], B_x[1], f"B'({B_x[0]}, {B_x[1]})", fontsize=9, ha='right')
plt.text(C_x[0], C_x[1], f"C'({C_x[0]}, {C_x[1]})", fontsize=9, ha='right')
# Reflection along Y-axis
plt.plot(yaxis_x, yaxis_y, 'g-o', label="Reflected along Y-axis")
plt.text(A_y[0], A_y[1], f"A''({A_y[0]}, {A_y[1]})", fontsize=9, ha='right')
plt.text(B_y[0], B_y[1], f"B''({B_y[0]}, {B_y[1]})", fontsize=9, ha='right')
plt.text(C_y[0], C_y[1], f"C''({C_y[0]}, {C_y[1]})", fontsize=9, ha='right')
# Axes and grid
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.title('Reflection of a Triangle along X-axis and Y-axis')
plt.axis('equal')
plt.show()
31
# Output new coordinates
print("Reflection along X-axis:")
print(f"A' = {A_x}")
print(f"B' = {B_x}")
print(f"C' = {C_x}")
print("\nReflection along Y-axis:")
print(f"A'' = {A_y}")
print(f"B'' = {B_y}")
print(f"C'' = {C_y}")