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