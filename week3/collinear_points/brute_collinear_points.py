from Point import Point
import matplotlib.pyplot as plt
import random

MAXXY = 100
NUM_POINTS = 50

plane = []
for i in range(MAXXY):
    for j in range(MAXXY):
        plane.append([i,j])
points = []
selection = random.sample(plane, NUM_POINTS)
for coordinates in selection:
    point = Point(coordinates[0], coordinates[1])
    points.append(point)

count = 0
segments = []
for i in range(len(points) - 3):
    for j in range(i + 1, len(points) - 2):
        for k in range(j + 1, len(points) - 1):
            if points[i].slope_to(points[j]) == points[i].slope_to(points[k]):
                for l in range(k + 1, len(points)):
                    if points[i].slope_to(points[j]) == points[i].slope_to(points[l]):
                        count += 1
                        segments.append([i,j,k,l])

print(f"Number of segments: {count}")
for segment in segments:
    print(points[segment[0]].to_string(), points[segment[1]].to_string(), points[segment[2]].to_string(), points[segment[3]].to_string())

plt.scatter([p.x for p in points], [p.y for p in points])
for segment in segments:
    plt.plot([points[segment[0]].x, points[segment[1]].x, points[segment[2]].x, points[segment[3]].x], [points[segment[0]].y, points[segment[1]].y, points[segment[2]].y, points[segment[3]].y])
plt.axis([0, MAXXY, 0, MAXXY])
plt.show()