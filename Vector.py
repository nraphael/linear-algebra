from __future__ import division
import itertools
import math

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The cordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self,v):
        return self.coordinates == v.coordinates

    def __add__(self,v):
        z = zip(self.coordinates,v.coordinates)
        i = itertools.starmap(lambda x,y: round(x + y,3),z)
        return Vector(list(i))

    def __sub__(self,v):
        z = zip(self.coordinates,v.coordinates)
        i = itertools.starmap(lambda x,y: round(x - y,3),z)
        return Vector(list(i))

    def __rmul__(self,sclr):
        i = [round(sclr * n,3) for n in self.coordinates]
        return Vector(i)

    def __div__(self,sclr):
        i = [sclr / n for n in self.coordinates]
        return Vector(i)

    def magnitude(self):
        v = [n ** 2 for n in self.coordinates]
        s = math.fsum(v)
        r = math.sqrt(s)
        return(round(r,3))
    
    def normalized(self):
        magnitude = self.magnitude()
        try:
            sclr = 1. / math.fabs(magnitude)
        except ZeroDivisionError:
            raise Exceptiom("Cannot normalize the zero vector")

        return(sclr * self)

    def dot(self, v):
        z = zip(self.coordinates,v.coordinates)
        #i = itertools.starmap(lambda x,y: x * y,z)
        i = [ x * y for x,y in z ]
        s = math.fsum(i)
        return(s)

    def angle_with(self,v,inDegrees= False):
        dotproduct = self.dot(v)
        magnitude1 = self.magnitude()
        magnitude2 = v.magnitude()
        try:
            angle = math.acos(dotproduct / (magnitude1 * magnitude2))
        except ZeroDivisionError:
            raise Exception("Cannot computer an angle with the zero vector")
        return(angle if not inDegrees else math.degrees(angle))
      
