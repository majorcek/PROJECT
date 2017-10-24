import math
import random
import numpy as np
import scipy.spatial


class annulus:
    """ A new object, annulus. Its outer radius is always 1."""
    def __init__(self, radius, number_of_points = 5, method = "polar"):
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

        assert method in ["polar", "planar"], \
            "Method must be either 'polar' or 'planar'"

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
        else:
            return self.__create_points_planar()

    def __create_points_polar(self):
        """ Creates n points within the annulus using polar coordinates and uniform distribution.
        theta~U(0,2*pi)
        R~sqrt((1-r^2)*X+r^2), where x~U(0,1)
        Points are then transformed into cartesian coordinates using:
        x = R*cos(theta)
        y = R*sin(theta)

        It returns a numpy array of two element arrays i.e. array([[x1,y1],[x2,y2], ...])
        """

        # Initializes random variables, that are to be used for computation of random points
        X = np.random.uniform(0, 1, self.n)
        theta = np.random.uniform(0, 2 * math.pi, self.n)

        R = np.sqrt((1-self.r**2)*X + self.r**2)         # Calculates truly randomly distributed radius

        x = R*np.cos(theta)
        y = R*np.sin(theta)

        return np.column_stack((x, y))

    def __create_points_planar(self):
        """ Creates n points using the planar method"""
        #TODO
        return None


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

    def includes_circle(self):
        """ Checks if the smaller circle is included inside the convex hull.
        Returns True if yes, otherwise returns False"""
        #TODO
        return None

    def __array_to_list(self):
        """"""
        #TODO
        return None

