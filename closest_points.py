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
    if closest != ():
        print("CLOSEST -> (", closest[0].x, ",", closest[0].y, ") - (", closest[1].x, ",", closest[1].y, ")")
    else:
        print("CLOSEST -> ", closest)
    plot_points(points, divisions=closest,
        current_points=[mid_point], current_quadrant=(points[0], points[-1]))
    points_by_y = merge_by_y(left_part, right_part)
    
    strip_points = [point for point in points_by_y if abs(point.x - points_by_y[mid].x) < closest_d]
    current_closest_distance = closest_d
    if left_closest != ():
        print("LEFT -> (", left_closest[0].x, ",", left_closest[0].y, ") - (", left_closest[1].x, ",", left_closest[1].y, ")")
    else:
        print("LEFT -> ", left_closest)
    if right_closest != ():
        print("RIGHT -> (", right_closest[0].x, ",", right_closest[0].y, ") - (", right_closest[1].x, ",", right_closest[1].y, ")")
    else:
        print("RIGHT -> ", right_closest)
    current_closest_pair = (left_closest, right_closest)[right_distance < left_distance]

    for i in range(len(strip_points)):
        for j in range(i + 1, min(i + 8, len(strip_points))):
            distance = euclidean_distance(strip_points[i], strip_points[j])
            if distance < current_closest_distance:
                current_closest_distance = distance
                current_closest_pair = (strip_points[i], strip_points[j])

    return current_closest_distance, current_closest_pair
    
while len(total_points) < 50:
    x = np.random.randint(1, 51)
    y = np.random.randint(1, 51)
    
    if ((x, y) not in total_points):
        total_points.append(Point(x, y))

total_points = sorted(total_points, key=lambda x: x.x)
plot_graph(total_points)
distance, closest = closest_pair(total_points)
print(distance, "(", closest[0].x, ",", closest[0].y, ") - (", closest[1].x, ",", closest[1].y, ")")
input()

