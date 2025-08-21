import matplotlib.pyplot as plt
# DDA Line Drawing Function with integer rounding
def dda(x1, y1, x2, y2):
points = []
dx = x2 - x1
dy = y2 - y1
steps = int(max(abs(dx), abs(dy)))
x_inc = dx / steps
y_inc = dy / steps
x, y = x1, y1
for _ in range(steps + 1):
# Round to nearest integer and format as 2 decimal places
px = round(x)
py = round(y)
points.append((float(f"{px:.2f}"), float(f"{py:.2f}")))
x += x_inc
y += y_inc
return points
# Starting and ending points
x1, y1 = 1, 1
x2, y2 = 4, 3
2
# Get points
points = dda(x1, y1, x2, y2)
print("Calculated Points (Rounded to Integer):")
for p in points:
print(p)
# Plotting
plt.figure(figsize=(6,6))
x_vals = [p[0] for p in points]
y_vals = [p[1] for p in points]
# Draw line
plt.plot(x_vals, y_vals, marker='o', color='blue')
# Mark points with labels
for i, (x, y) in enumerate(points):
label = f"P{i}({x},{y})"
plt.text(x + 0.05, y + 0.05, label, fontsize=9)
# Formatting
plt.title("DDA Line Drawing (Rounded to Integer Points)")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.axis('equal')
plt.show()