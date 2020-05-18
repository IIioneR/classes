import math

from math import pi


class Shape:
    def __init__(self, coordinate_x=0, coordinate_y=0):
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y

    def __str__(self):
        return 'Shape(coordinate_x={}, coordinate_y{})'.format(self.coordinate_x, self.coordinate_y)

    def __repr__(self):
        return self.__str__()


class Point(Shape):
    def __init__(self, coordinate_x=11, coordinate_y=1):
        super().__init__(coordinate_x, coordinate_y)

    def __str__(self):
        return 'Point(coordinate_x={}, coordinate_y={})' \
            .format(self.coordinate_x, self.coordinate_y)

    def __repr__(self):
        return self.__str__()


class Circle(Shape):

    def __init__(self, radius=10):
        super().__init__(point.coordinate_x, point.coordinate_y)
        self.radius = radius

    def __str__(self):
        return 'Point(coordinate_x={}, coordinate_y={}, radius = {})' \
            .format(self.coordinate_x, self.coordinate_y, self.radius)

    def __repr__(self):
        return self.__str__()

    def intersect(self):
        result = (((point.coordinate_x-self.coordinate_x)**2) / self.radius**2)\
                 + (((point.coordinate_y-self.coordinate_y)**2) / self.radius**2)
        if result < 1:
            return True
        else:
            return False


point = Point()
cheking = Circle()

print(cheking.intersect())
