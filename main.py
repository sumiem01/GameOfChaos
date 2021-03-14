import numpy as np
import matplotlib.pyplot as plt

triangle = np.array([[1, 1], [2.5, 5], [4, 1]])
square = np.array([[1, 1], [1, 5], [5, 1], [5, 5]])
point_zero = np.array([[3, 2.5]])


def game_conditions(x, y, point_i, point_j, distX, distY):
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
    return point_i, point_j


def simulate_points(figure: np.array, number_iterations: int, vetices: int):
    x = figure[0, 0]
    y = figure[0, 1]

    point_i = point_zero[0, 0]
    point_j = point_zero[0, 1]

    display_points = []
    for i in range(number_iterations):
        distX = np.linalg.norm(point_i - x)
        distY = np.linalg.norm(point_j - y)
        point_i, point_j = game_conditions(x, y, point_i, point_j, distX, distY)
        display_points.append([point_i, point_j])
        ran = np.random.randint(vetices)
        x = figure[ran, 0]
        y = figure[ran, 1]
    return display_points


points = simulate_points(square, 1000, 4)
plt.scatter(square[:, 0], square[:, 1])
plt.scatter(point_zero[0, 0], point_zero[0, 1])
plt.scatter(np.array(points)[:, 0], np.array(points)[:, 1])

plt.show()

