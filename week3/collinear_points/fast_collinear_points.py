from Point import Point
import matplotlib.pyplot as plt
import random

MAXXY = 10
NUM_POINTS = 20

# choose unique random points
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
slopes = {}
for i in range(len(points) - 3):
    slopes[i] = []
    for j in range(len(points)):
        slopes[i].append(points[i].slope_to(points[j]))
    sorted_slopes = sorted(slopes[i])
    for k in range(len(slopes[i]) - 3):
        if sorted_slopes[k] == sorted_slopes[k+3]:
            segment = []
            for l in range(len(sorted_slopes)):
                if slopes[i][l] == sorted_slopes[k]:
                    segment.append(l)
            if segment not in segments:
                segments.append(segment)
                count += 1


print(f"Number of segments: {count}")
for segment in segments:
    print(points[segment[0]].to_string(), points[segment[1]].to_string(), points[segment[2]].to_string(), points[segment[3]].to_string())

plt.scatter([p.x for p in points], [p.y for p in points])
for segment in segments:
    plt.plot([points[segment[0]].x, points[segment[1]].x, points[segment[2]].x, points[segment[3]].x], [points[segment[0]].y, points[segment[1]].y, points[segment[2]].y, points[segment[3]].y])
plt.axis([0, MAXXY, 0, MAXXY])
plt.show()