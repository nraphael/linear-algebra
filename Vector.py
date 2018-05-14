import itertools

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