import numpy as np
import matplotlib.pyplot as plt

points = np.array([[1, 1], [2.5, 5], [4, 1]])
point_zero = np.array([[3, 2.5]])

x = points[0, 0]
y = points[0, 1]

point_i = point_zero[0, 0]
point_j = point_zero[0, 1]

display_points = []
for i in range(1000):
    distX = np.linalg.norm(point_i - x)
    distY = np.linalg.norm(point_j - y)
    if x < point_i and y < point_j:
        point_i -= distX / 2
        point_j -= distY / 2
    elif x < point_i and y > point_j:
        point_i -= distX / 2
        point_j += distY / 2
    elif x > point_i and y < point_j:
        point_i += distX / 2
        point_j -= distY / 2
    elif x > point_i and y > point_j:
        point_i += distX / 2
        point_j += distY / 2
    display_points.append([point_i, point_j])
    ran = np.random.randint(3)
    x = points[ran, 0]
    y = points[ran, 1]

plt.scatter(points[:, 0], points[:, 1])
plt.scatter(point_zero[0, 0], point_zero[0, 1])
plt.scatter(np.array(display_points)[:, 0], np.array(display_points)[:, 1])

plt.show()

