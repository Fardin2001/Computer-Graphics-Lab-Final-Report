import matplotlib.pyplot as plt
# Bresenham's Line Drawing Algorithm
def bresenham(x1, y1, x2, y2):
points = []
dx = abs(x2 - x1)
dy = abs(y2 - y1)
sx = 1 if x2 > x1 else -1
sy = 1 if y2 > y1 else -1
err = dx - dy
while True:
points.append((float(f"{x1:.2f}"), float(f"{y1:.2f}"))) # store as float for formatting
if x1 == x2 and y1 == y2:
break
e2 = 2 * err
if e2 > -dy:
err -= dy
x1 += sx
if e2 < dx:
err += dx
y1 += sy
return points
5
# Starting and ending points
x1, y1 = 9, 18
x2, y2 = 14, 22
# Get points
points = bresenham(x1, y1, x2, y2)
print("Calculated Points (Bresenham):")
for p in points:
print(p)
# Plotting
plt.figure(figsize=(6,6))
x_vals = [p[0] for p in points]
y_vals = [p[1] for p in points]
# Draw line
plt.plot(x_vals, y_vals, marker='o', color='green')
# Mark points with labels
for i, (x, y) in enumerate(points):
label = f"P{i}({x},{y})"
plt.text(x + 0.05, y + 0.05, label, fontsize=9)
# Formatting
plt.title("Bresenham's Line Drawing Algorithm")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.axis('equal')
plt.show()