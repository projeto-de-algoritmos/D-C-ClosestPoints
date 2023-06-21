import matplotlib.pyplot as plt
import numpy as np
from total_points import *

def plot_points(points, divisions=None, current_points=None, current_quadrant=None):
    print("QUADRANTE -> (", current_quadrant[0].x, ",", current_quadrant[0].y, ") - (", current_quadrant[1].x, ",", current_quadrant[1].y, ")")
    plt.clf()
    plt.scatter([point.x for point in total_points], [point.y for point in total_points], color='green')
    if current_points is not None and len(current_points) > 0:
        plt.scatter([point.x for point in current_points], [point.y for point in current_points], color='orange', label='Pontos Visitados')
    if current_quadrant is not None:
        y_min, y_max = plt.ylim()
        plt.fill_between([current_quadrant[0].x, current_quadrant[1].x],
            y_min, y_max,
            color='gray', alpha=0.2, label='Quadrante Atual')
    if divisions and len(divisions) > 0:
        print("DIVISIONS -> (", divisions[0].x, ",", divisions[0].y, ") - (", divisions[1].x, ",", divisions[1].y, ")")
        plt.plot([divisions[0].x, divisions[1].x], [divisions[0].y, divisions[1].y], color='blue')
    plt.draw()
    plt.pause(0.5)

def plot_graph(points, divisions=None, current_points=None, current_quadrant=None):
    plt.figure(figsize=(8, 8))
    plt.ion()
    plt.scatter([point.x for point in total_points], [point.y for point in total_points], color='blue')
    if current_points is not None and len(current_points) > 0:
        plt.scatter([point[0] for point in current_points], [point[1] for point in current_points], color='orange', label='Pontos Visitados')
    if divisions:
        for div in divisions:
            plt.plot([div[0][0], div[1][0]], [div[0][1], div[1][1]], color='green')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.suptitle('Divisões e comparações do Par de Pontos Mais Próximos')
    plt.show()
    plt.legend()
    plt.grid(True)
    plt.show()