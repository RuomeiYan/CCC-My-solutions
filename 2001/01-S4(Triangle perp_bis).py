from itertools import combinations


def dist_sq(p1,p2):  # (x2-x1)^2 + (y2-y1)^2
    return (sum((x2-x1)**2 for x1,x2 in zip(p1,p2)))


# Perpendicular bisector
def perp_bis(p1, p2):  # p_mid is the midpoint, m is the negative reciprocal of slope(the slope of the perpendicular line!!!)
    p_mid = tuple((x1+x2)/2 for x1,x2 in zip(p1,p2))  # midpoint
    m = -(p2[0]-p1[0])/(p2[1]-p1[1]) if p2[1] != p1[1] else None  # -(x2-x1)/(y2-y1)
    return p_mid, m


# Intersection function!! Input two mid points and two slopes of perpendicular bisectors!
def inter(p1, m1, p2, m2): # Intersection!
    x1, y1 = p1
    x2, y2 = p2
    if m2 == m1:
        return None
    if m2 is None:
        return (x2, m1*(x2-x1) + y1)
    if m1 is None:
        return inter(p2, m2, p1, m1)
    x = (m1*x1 - m2*x2 - y1 + y2)/(m1-m2)
    return (x, m1*(x-x1) + y1)

points = tuple((int(x), int(y)) for x,y in (input().split() for _ in range(int(input()))))

mini = 2000  # Minimum radius

if len(points) == 1:
    mini = 0
else:
    for p1, p2 in combinations(points, 2):  # Pick up any two points
        p_mid = tuple((x1+x2)/2 for x1,x2 in zip(p1,p2))  # Midpoint
        rad_sq = dist_sq(p1, p_mid)  # the square of the distance between point 1 and midpoint
        if all(dist_sq(p, p_mid) <= rad_sq for p in points): # If all the points are in that circle
            mini = min(mini, 2*(rad_sq**0.5))  # Update the minimum radius
if len(points) >= 3:
    for p1, p2, p3 in combinations(points, 3):
        p_mid_1, m1 = perp_bis(p1, p2)
        p_mid_2, m2 = perp_bis(p2, p3)
        center = inter(p_mid_1, m1, p_mid_2, m2)
        print(center)
        if center is None:
            continue
        rad_sq = dist_sq(center, p1)
        if all(dist_sq(center, p) <= rad_sq for p in points):
            mini = min(mini, 2*(rad_sq**0.5))

print("{:.2f}".format(mini))

