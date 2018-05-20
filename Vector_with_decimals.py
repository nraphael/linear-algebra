from __future__ import division
import itertools
import math
from decimal import Decimal, getcontext
from fractions import gcd 

getcontext().prec = 30

DEBUG = False

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
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
        i = itertools.starmap(lambda x,y: x + y,z)
        return Vector(list(i))

    def __sub__(self,v):
        z = zip(self.coordinates,v.coordinates)
        i = itertools.starmap(lambda x,y: x - y,z)
        return Vector(list(i))

    def __rmul__(self,sclr):
        i = [Decimal(sclr) * n for n in self.coordinates]
        return Vector(i)

    def __div__(self,sclr):
        i = [sclr / n for n in self.coordinates]
        return Vector(i)

    def magnitude(self):
        v = [n ** 2 for n in self.coordinates]
        s = sum(v)
        r = Decimal(math.sqrt(s))
        return(r)
    
    def normalized(self):
        magnitude = self.magnitude()
        try:
            sclr = Decimal('1.0') / abs(magnitude)
        except ZeroDivisionError:
            raise Exceptiom("Cannot normalize the zero vector")

        return(sclr * self)

    # v dot u = v.magnitude() * u.magnitude() * cos th
    # => cos th = v dot u / (v.m() * u.m() 
    # =>  = arcos( ") = arccos( (1     * v dot 1     * w)
    #                             -----          -----
    #                             v.m()          u.m()
    def dot(self, v):
        z = zip(self.coordinates,v.coordinates)
        #i = itertools.starmap(lambda x,y: x * y,z)
        i = [ x * y for x,y in z ]
        s = sum(i)
        return(s)

    def angle_with(self,v,inDegrees= False):
        dotproduct = self.dot(v)
        magnitude1 = self.magnitude()
        magnitude2 = v.magnitude()
        try:
            prec = getcontext().prec
            getcontext().prec = 10
            angle_in_radians = math.acos(dotproduct / (magnitude1 * magnitude2))
            getcontext().prec = prec
        except Exception as e:
            print(e)
            raise Exception("Cannot computer an angle with the zero vector")
        return(angle_in_radians if not inDegrees else math.degrees(angle_in_radians))
      
    def is_parallel_to(self,v):
        if self.is_zero() or v.is_zero():
            return True
        # instructor then has
        return (self.angle_with(v) == 0 or self.angle_with(v) == Decimal(math.pi))
#        try:
#            lcms = [m/n for m,n in zip(self.coordinates,v.coordinates)]
#            s = set(lcms)
#            if DEBUG:
#                print("lcms = %s" % lcms)
#            # Do vectors have the same lowest common multiplier?
#            return len(s) == 1
#        except Exception as e:
#            print(str(e))
#            raise e

    def is_zero(self,tolerance=1e-10):
            return self.magnitude() < tolerance

    def is_orthogonal_to(self,v, tolerance=1e-10):
        if self.is_zero() or v.is_zero():
            return True
        if DEBUG:
            print("Ortho testing: %s" % self.dot(v))
        if abs(self.dot(v)) < tolerance:
        #if self.dot(v) == 0:
            return True
        else:
            return False
