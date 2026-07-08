import math

# 1. The Point class must come first!
class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = float(x)
        self.__y = float(y)
    
    def getx(self):
        return self.__x
    
    def gety(self):
        return self.__y
    
    def distance_from_xy(self, x, y):
        dx = self.__x - x
        dy = self.__y - y
        return math.hypot(dx, dy)
    
    def distance_from_point(self, point):
        return self.distance_from_xy(point.getx(), point.gety())


# 2. Then the Triangle class uses the Point class below it
class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__vertices = [vertice1, vertice2, vertice3]

    def perimeter(self):
        p1 = self.__vertices[0]
        p2 = self.__vertices[1]
        p3 = self.__vertices[2]

        side1 = p1.distance_from_point(p2)
        side2 = p2.distance_from_point(p3)
        side3 = p3.distance_from_point(p1)

        return side1 + side2 + side3


# 3. The test script runs at the very bottom
triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())