import matplotlib.pyplot as plt
from math import sqrt, inf
import numpy as np
from total_points import *
from plot import *

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def euclidean_distance(point1, point2):
    return sqrt(((point1.x - point2.x) ** 2) + ((point1.y - point2.y) ** 2))


def merge_by_y(left, right):
    merged = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i].x <= right[j].y:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    while(j<len(right)): 
        merged.append(right[j])
        j += 1
    while(i<len(left)): 
        merged.append(left[i])
        i += 1
    return merged

def closest_pair(points):

    if len(points) <= 1:
        plot_points(points, current_quadrant=(points[0], points[0]))
        return inf, ()
    mid = len(points)//2
    left_part = points[:mid]
    right_part = points[mid:]
    left_distance, left_closest = closest_pair(left_part)
    right_distance, right_closest = closest_pair(right_part)
    
    # elif len(points) == 2:
    #     return points[0], points[1]
    # print("sorted", sorted_points)
    # mid = len(points) // 2
    mid_point = points[mid]
    closest = 0
    
    if left_distance is inf:
        closest = right_closest
        closest_d = right_distance
    elif right_distance is inf:
        closest = left_closest
        closest_d = left_distance
    else:
        if left_distance <= right_distance:
            closest = left_closest
            closest_d = left_distance
        else:
            closest = right_closest
            closest_d = right_distance
    print("CLOSEST", closest)
    plot_points(points, divisions=closest,
        current_points=[mid_point], current_quadrant=(points[0], points[-1]))
    points_by_y = merge_by_y(left_part, right_part)
    
    strip_points = [point for point in points_by_y if abs(point.x - points_by_y[mid].x) < closest_d]
    current_closest_distance = closest_d
    print("LEFT", left_closest)
    print("RIGHT", right_closest)
    current_closest_pair = (left_closest, right_closest)[right_distance < left_distance]

    for i in range(len(strip_points)):
        for j in range(i + 1, min(i + 8, len(strip_points))):
            distance = euclidean_distance(strip_points[i], strip_points[j])
            if distance < current_closest_distance:
                current_closest_distance = distance
                current_closest_pair = (strip_points[i], strip_points[j])

    # merged_points = merge_by_y_coordinate(left_points, right_points)
    # filtered_points = [point for point in merged_points if abs(point[0] - merged_points[mid][0]) < closest_distance]

    return current_closest_distance, current_closest_pair
    # if closest is None:
    #     return None
    
    # closest_pair_points = closest

    # plot_points(points, divisions=[(sorted_points[0], sorted_points[-1])],
    #     current_points=[mid_point], current_quadrant=(sorted_points[0], sorted_points[-1]))

    # closest_distance = euclidean_distance(closest[0], closest[1])
    
    # strip_points = [point for point in sorted_points
    #                 if abs(point[0] - mid_point[0]) < closest_distance]
    
    # strip_closest = None
    # min_distance = closest_distance
    
    # for i in range(len(strip_points)):
    #     for j in range(i+1, min(i+8, len(strip_points))):
    #         distance = euclidean_distance(strip_points[i], strip_points[j])
    #         if distance < min_distance:
    #             min_distance = distance
    #             strip_closest = (strip_points[i], strip_points[j])
    
    # if strip_closest and min_distance < closest_distance:

    #     closest_pair_points = strip_closest
    
    # return closest_pair_points

# Exemplo de uso
# points = np.random.rand(50, 2)  # G
# total_points = [(np.random.randint(1, 51), np.random.randint(1, 51)) for _ in range(50)]
# print(points)
# total_points = [tuple(point) for point in total_points]
# print(points)
while len(total_points) < 50:
    x = np.random.randint(1, 51)
    y = np.random.randint(1, 51)
    
    if ((x, y) not in total_points):
        total_points.append(Point(x, y))

total_points = sorted(total_points, key=lambda x: x.x)
plot_graph(total_points)
distance, closest = closest_pair(total_points)
print(distance, closest)




# import matplotlib.pyplot as plt
# import numpy as np

# # Ativa o modo interativo
# plt.ion()

# # Cria uma figura e um objeto de plotagem
# fig, ax = plt.subplots()

# # Dados iniciais
# x = np.linspace(0, 10, 100)
# y = np.sin(x)

# # Plota os dados iniciais
# line, = ax.plot(x, y)

# # Exibe o gráfico
# plt.show()

# # Atualiza o gráfico dinamicamente
# for i in range(100):
#     # Atualiza os dados
#     y = np.sin(x + i/10)
    
#     # Atualiza a linha do gráfico com os novos dados
#     line.set_ydata(y)
    
#     # Redesenha o gráfico
#     plt.draw()
    
#     # Pausa por 0.1 segundo antes de atualizar novamente
#     plt.pause(0.1)

# # Desativa o modo interativo no final
# plt.ioff()
