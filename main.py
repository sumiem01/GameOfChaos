import numpy as np
import matplotlib.pyplot as plt

triangle = np.array([[1, 1], [2.5, 5], [4, 1]])
square = np.array([[1, 1], [1, 5], [5, 1], [5, 5]])
point_zero = np.array([[3, 3]])


def game_conditions(x, y, point_i, point_j, dist_x, dist_y):
    if x < point_i and y < point_j:
        point_i -= dist_x / 2
        point_j -= dist_y / 2
    elif x < point_i and y > point_j:
        point_i -= dist_x / 2
        point_j += dist_y / 2
    elif x > point_i and y < point_j:
        point_i += dist_x / 2
        point_j -= dist_y / 2
    elif x > point_i and y > point_j:
        point_i += dist_x / 2
        point_j += dist_y / 2
    return point_i, point_j


def simulate_points(figure: np.array, number_iterations: int, vetices: int):
    x = figure[0, 0]
    y = figure[0, 1]

    point_i = point_zero[0, 0]
    point_j = point_zero[0, 1]

    temp = 0
    ran = 0

    display_points = []
    for i in range(number_iterations):
        dist_x = np.linalg.norm(point_i - x)
        dist_y = np.linalg.norm(point_j - y)
        point_i, point_j = game_conditions(x, y, point_i, point_j, dist_x, dist_y)
        display_points.append([point_i, point_j])
        temp = ran
        ran = np.random.randint(vetices)
        if ran == temp:
            ran = np.random.randint(vetices)

        x = figure[ran, 0]
        y = figure[ran, 1]
    return display_points


points = simulate_points(square, 100000, 4)
plt.scatter(square[:, 0], square[:, 1])
plt.scatter(point_zero[0, 0], point_zero[0, 1])
plt.scatter(np.array(points)[:, 0], np.array(points)[:, 1], s=0.2, alpha=0.1)

plt.show()

