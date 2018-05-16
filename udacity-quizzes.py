import math
from Vector import Vector

v1 = Vector([8.218,-9.341])
v2 = Vector([-1.129,2.111])
print(v1 + v2)

v1 = Vector([7.119,8.215])
v2 = Vector([-8.223,0.878])
print(v1 - v2)

v1 = Vector([1.671,-1.012,-0.318])
print(7.41 * v1)

v1 = Vector([3.0,4.0])
print(v1.magnitude())
print(v1.direction())

print("Magnitude and directions")
v1 = Vector([-0.221,7.437])
print(v1.magnitude())

v1 = Vector([8.813,-1.331, -6.247])
print(v1.magnitude())

v1 = Vector([5.581,-2.136])
print(v1.normalized())

v1 = Vector([1.996,3.108,-4.554])
print(v1.normalized())

print("Dot products")
print("Simple test")
v1 = Vector([1,2,3])
v2 = Vector([4,5,6])
print(v1.dot(v2))

print("Quiz")
v1 = Vector([7.887,4.138])
v2 = Vector([-8.802,6.776])
print(v1.dot(v2))

v1 = Vector([-5.955,-4.904,-1.874])
v2 = Vector([-4.496,-8.755,7.103])
print(v1.dot(v2))

print("Angles")
v1 = Vector([1,2,-1])
v2 = Vector([3,1,0])
print(v1.angle(v2))


v1 = Vector([3.183,-7.627])
v2 = Vector([-2.668,5.319])
print(v1.angle(v2))

v1 = Vector([7.35,0.221,5.188])
v2 = Vector([2.751,8.259,3.985])
print(v1.angle(v2,inDegrees=True)))
