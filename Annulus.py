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
        points is a list of points, uniformly randomly distributed inside the annulus
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

        # Methods regarding points inside the annulus
        self.points = self.__create_points_polar()
        self.convex_hull = self.__make_convex_hull()

    def area(self):
        """ Calculates the area of the annulus"""


    def __create_points_polar(self):
        """ Creates n points within the annulus using polar coordinates and uniform distribution.
        theta~U(0,2*pi)
        R~sqrt((1-r^2)*X+r^2), where x~U(0,1)
        Points are then transformed into cartesian coordinates using:
        x = R*cos(theta)
        y = R*sin(theta)
        """

        # Initializes random variables, that are to be used for computation of random points
        X = np.random.uniform(0, 1, self.n)
        theta = np.random.uniform(0, 2 * math.pi, self.n)

        R = np.sqrt((1-self.r**2)*X + self.r**2)         # Calculates truly randomly distributed radius

        x = R*np.cos(theta)
        y = R*np.sin(theta)

        return list(zip(x,y))


    def __make_convex_hull(self):
        """ Calculates the convex hull of the points, that are inside the annulus."""

        c_hull = scipy.spatial.ConvexHull(self.points)
        return c_hull






