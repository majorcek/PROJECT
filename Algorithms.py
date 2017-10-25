import math
import numpy as np

def distance_line_point(start, end, p = (0, 0)):
    """ Calculates distance between a line segment, starting in start and ending in end, and point p.
    start, end and p are stored in a numpy array array([x, y]).
    We use techniques from linear algebra in two dimensional euclidean plane

    t is a coefficient in the algebraic equation. If t>1, it means that the perpendicular projection
    of p to the line, that goes through our start and stop point, is not on our segment, but exceeds it.
    If t<0, then the projection precedes our segment. In the first case, the smallest distance is the distance
    from p to end, in second from p to start. If t is between 0 and 1, we calculate the distance from p
    to its perpendicular projection"""

    # q is a vector (line) AB, where A = start and B = end
    q = end - start

    # Calculate t
    t = (np.dot(q, p) - np.dot(q, start))/(np.dot(q, q))

    # See, from where will we measure our distance
    if t < 0:   point = start
    elif 0 < t < 1:
        point = start + t*q
    else: point = end

    distance = math.sqrt(np.dot(point - p, point - p))

    return distance

def convex_hull_circle_inclusion(points, r, center = (0, 0)):
    """ This function checks whether or not the inner boundary (smaller circle) of the annulus with radius r is
    fully included inside the convex hull, defined (bounded) by the points in the array 'points'.
    Points are given in an ordered (if we connect the points from first to last, we get the convex hull) array
    of points, each represented with a numpy array of two coordinates ([x,y])
    In the unlikely event where the convex hull is tangential to the smaller circle (distance to the convex hull is
    the same as r), we define that as inclusion.
    If the smaller circle is included, we return True, otherwise we return False"""

    for i in range(len(points)):
        end = points[i]
        if r > distance_line_point(start, end, center):
            return False
        start = end
    return True




