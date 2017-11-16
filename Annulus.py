import math
import numpy as np
import scipy.spatial


class annulus:
    """ A new object, annulus. Its outer radius is always 1.
    Properties:
        r - radius of the inner bound
        n - number of points
        points - randomly generated points inside the annulus
        convex_hull - convex hull object, created from 'points'
        vertices - vertices representing the convex hull
        area - area of the annulus
        hull_len - length of the convex hull
        hull_area - area of the convex hull
        includes_circle - boolean representing the inclusion of the smaller circle inside the convex hull
        plot_form() - list of: list of points in tuple form, list of vertices (of convex hull) in tuple form
    """
    def __init__(self, radius = 0.5, number_of_points = 5, method = "polar"):
        """ Initializes an annulus with the smaller radius of radius and with number_of_points points, randomly
        uniformly distributed inside of it.

        radius is a percentage value of the outer border radius, must be between 0 and 1
        number_of_points must be >= 3 (default value is 5)
        points is a numpy array of points, uniformly randomly distributed inside the annulus
        method must be either 'polar' or 'planar', depicting the way random points are generated
        """
        assert 0 <= radius <= 1, \
            "Radius must be between 0 and 1"

        assert number_of_points >= 3, \
            "Number of points inside the annulus must be greater or equal than 3"

        assert method in ["polar", "planar", "naive"], \
            "Method must be either 'polar', 'planar' or 'naive' "

        self.r = radius
        self.n = number_of_points

        # Variables regarding points inside the annulus
        self.points = self.__create_points(method)

        # Variables regarding the convex hull
        self.convex_hull = self.__create_convex_hull()
        self.vertices = self.__get_convex_hull_vertices()


    @property
    def area(self):
        """ Calculates the area of the annulus"""
        return math.pi*(1 - self.r ** 2)


    def __create_points(self, method):
        """ Creates n random points using either polar or planar method"""
        if method == "polar":
            return self.__create_points_polar()
        elif method == "planar":
            return self.__create_points_planar()
        else:
            return self.__create_points_naive_polar()


    def __create_points_polar(self):
        """ Creates n points within the annulus using polar coordinates and uniform distribution.
        theta~U(0,2*pi)
        R~sqrt((1-r^2)*X+r^2), where x~U(0,1)
        Points are then transformed into cartesian coordinates using:
        x = R*cos(theta)
        y = R*sin(theta)

        It returns a numpy array of two element arrays i.e. array([[x1,y1],[x2,y2], ...])"""

        # Initializes random variables, that are to be used for computation of random points
        X = np.random.uniform(0, 1, self.n)
        theta = np.random.uniform(0, 2 * math.pi, self.n)

        R = np.sqrt((1-self.r**2)*X + self.r**2)         # Calculates truly randomly distributed radius

        x = R*np.cos(theta)
        y = R*np.sin(theta)

        return np.column_stack((x, y))


    def __create_points_planar(self):
        """ Creates n points using the planar method
        First, the method creates a numpy array with length n and a [0, 0] element
        For each cell in the array, we generate random points, using a two dimensional uniform distribution,
        until a point is inside the annulus (equal or greater distance (from the center of the circle) than r
        and smaller or equal distance than 1)"""
        def dist(x, y = np.zeros(2)):
            """ Calculates the distance between points x and y"""
            return np.sqrt(np.sum((x - y) ** 2))

        points = np.zeros([self.n, 2])      # Creates a numpy array which will hold points
        # Loop for point creation
        for i in range(len(points)):
            point = np.random.uniform(-1,1,2)
            while not(self.r <= dist(point) <= 1):    # If the point is outside the annulus, generate another point
                point = np.random.uniform(-1,1,2)
            points[i] = point

        return points


    def __create_points_naive_polar(self):
        """ Naively creates points using polar coordinates
        Theta is uniformly distributed between 0 and 2*pi
        R is uniformly distributed between r and 1"""

        R = np.random.uniform(self.r, 1, self.n)
        theta = np.random.uniform(0, 2*math.pi, self.n)

        x = R * np.cos(theta)
        y = R * np.sin(theta)

        return np.column_stack((x, y))


    def __create_convex_hull(self):
        """ Calculates the convex hull of the points, that are inside the annulus."""

        c_hull = scipy.spatial.ConvexHull(self.points)
        return c_hull


    def __get_convex_hull_vertices(self):
        """ Gets the points that are used as vertices in a convex hull"""
        vertices_indices = self.convex_hull.vertices
        vertices = self.points[vertices_indices, :]

        return vertices


    @property
    def hull_len(self):
        """ Returns the length of the convex hull
        It uses the area method from scipy.spatial.ConvexHull"""
        return self.convex_hull.area


    @property
    def hull_area(self):
        """ Returns the area of the convex hull
        It uses the volume method from scipy.spatial.ConvexHull"""
        return self.convex_hull.volume


    def __distance_line_point(self, start, end, p=np.zeros(2)):
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
        t = (np.dot(q, p) - np.dot(q, start)) / (np.dot(q, q))

        # See, from where will we measure our distance
        if t < 0:
            point = start
        elif 0 < t < 1:
            point = start + t * q
        else:
            point = end

        distance = math.sqrt(np.dot(point - p, point - p))

        return distance


    @property
    def includes_circle(self):
        """ This function checks whether or not the inner boundary (smaller circle) of the annulus with radius r is
        fully included inside the convex hull, defined (bounded) by the points in the array 'points'.
        Points are given in an ordered (if we connect the points from first to last, we get the convex hull) array
        of points, each represented with a numpy array of two coordinates ([x,y])
        In the unlikely event where the convex hull is tangential to the smaller circle (distance to the convex hull is
        the same as r), we define that as inclusion.
        Simultaneously we check if the vertices of the convex hull really include the circle. This does not only
        rely on the distance but the position of the points. They have to be positioned around the origin point
        in such manner, that the points x, y coordinates cover all of the quadrants, at least one per parameter.
        If the smaller circle is included, we return True, otherwise we return False"""

        # Indicators for points coordinates
        x_left, x_right, y_up, y_down = False, False, False, False
        start = self.vertices[-1]
        for i in range(len(self.vertices)):
            end = self.vertices[i]
            if self.r > self.__distance_line_point(start, end):
                return False

            # Check the coordinates
            if end[0] >= 0:
                x_right = True
            else:
                x_left = True
            if end[1] >=0:
                y_up = True
            else:
                y_down = True

            start = end

        if x_left and x_right and y_up and y_down:
            return True
        else:
            return False


    def __array_to_list_and_tuple(self, points):
        """ Transforms the points from the format used in this class to the format, that will be used in drawing
        """
        points = [tuple(element) for element in points]

        return points


    def plot_form(self):
        """ This method returns the random generated points and the vertices defining the convex hull
        in a pure python format, that will be used for plotting.
        The format of points is: [(x0, y0),(x1, y1),(x2, y2), ...]
        The two sets of points are returned as a list: [points, vertices]"""

        points = self.__array_to_list_and_tuple(self.points)
        vertices = self.__array_to_list_and_tuple(self.vertices)

        return [points, vertices]

