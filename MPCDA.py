import matplotlib.pyplot as plt
# Original triangle coordinates
A = (0, 0)
B = (1, 0)
C = (1, 1)
# Rotation 90° anticlockwise: (x', y') = (-y, x)
def rotate_90_ccw(x, y):
return -y, x
# Apply rotation
A_new = rotate_90_ccw(*A)
B_new = rotate_90_ccw(*B)
C_new = rotate_90_ccw(*C)
# Prepare for plotting
orig_x = [A[0], B[0], C[0], A[0]]
orig_y = [A[1], B[1], C[1], A[1]]
rot_x = [A_new[0], B_new[0], C_new[0], A_new[0]]
rot_y = [A_new[1], B_new[1], C_new[1], A_new[1]]
# Plotting
plt.figure(figsize=(6,6))
plt.plot(orig_x, orig_y, 'b-o', label='Original Triangle')
plt.plot(rot_x, rot_y, 'r-o', label="Rotated Triangle (90° CCW)")
27
# Annotating points
plt.text(A[0], A[1], f"A{A}", fontsize=10, color='blue', ha='right')
plt.text(B[0], B[1], f"B{B}", fontsize=10, color='blue', ha='right')
plt.text(C[0], C[1], f"C{C}", fontsize=10, color='blue', ha='right')
plt.text(A_new[0], A_new[1], f"A'{A_new}", fontsize=10, color='red', ha='left')
plt.text(B_new[0], B_new[1], f"B'{B_new}", fontsize=10, color='red', ha='left')
plt.text(C_new[0], C_new[1], f"C'{C_new}", fontsize=10, color='red', ha='left')
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.title('Rotation of a Triangle (90° Anticlockwise)')
plt.axis('equal')
plt.show()
# Print new coordinates
print("New coordinates after rotation:")
print(f"A' = {A_new}")
print(f"B' = {B_new}")
print(f"C' = {C_new}")