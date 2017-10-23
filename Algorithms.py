import math

def distance_from_point(start, end, p = (0, 0)):
    """ Calculates distance between a line segment, starting in start and ending in end, and point p.
    start, end and p are stored in (x, y) form.
    We use techniques from linear algebra in two dimensional euclidean plane

    t is a coefficient in the algebraic equation. If t>1, it means that the perpendicular projection
    of p to the line, that goes through our start and stop point, is not on our segment, but exceeds it.
    If t<0, then the projection precedes our segment. In the first case, the smallest distance is the distance
    from p to end, in second from p to start. If t is between 0 and 1, we calculate the distance from p
    to its perpendicular projection"""

    def dot_prod(x, y):
        """ Dot product of two two dimensional vectors"""
        prod = x[0]*y[0] + x[1]*y[1]
        return prod

    # point (vector) start
    x1, y1 = start[0], start[1]

    # point (vector) end
    x2, y2 = end[0], end[1]

    # point (vector) point
    x0, y0 = p[0], p[1]

    # q is a vector (line) AB, where A = start and B = end
    q1, q2 = x2-x1, y2-y1
    q = (q1, q2)

    # Calculate t
    t = (dot_prod(q, p) - dot_prod(q, start))/(dot_prod(q, q))

    # See, from where will we measure our distance
    if t < 0:   point = start
    elif 0 < t < 1: point = (x1 + t*q1 + x0, y1 + t*q2 + y0)
    else: point = end

    distance = math.sqrt(dot_prod(point, point))

    return distance

def convex_hull_circle_inclusion(points, r, center = (0, 0)):
    """ This function checks whether or not the inner boundary (smaller circle) of the annulus with radius r is
    fully included inside the convex hull, defined (bounded) by the points in the list points.
    Points are given in an ordered (if we connect the points from first to last, we get the convex hull) list
    of points, each represented with a tuple (x, y)
    In the unlikely event where the convex hull is tangential to the smaller circle (distance to the convex hull is
    the same as r), we define that as inclusion.
    If the smaller circle is included, we return True, otherwise we return False"""
    points = list(points)

    end = points[0]
    while len(points):
        start = points.pop()
        if r > distance_from_point(start, end, center):
            return False
        end = start

    return True




