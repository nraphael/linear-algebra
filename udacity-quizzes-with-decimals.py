import math
from Vector_with_decimals import Vector
from decimal import Decimal, getcontext

print("Vector addition")
v1 = Vector([8.218,-9.341])
v2 = Vector([-1.129,2.111])
print(v1 + v2)

print("Vector subtraction")
v1 = Vector([7.119,8.215])
v2 = Vector([-8.223,0.878])
print(v1 - v2)

print("Vector multiply by a scalar")
v1 = Vector([1.671,-1.012,-0.318])
print(7.41 * v1)

print("Vector magnitude")
v1 = Vector([3.0,4.0])
print(v1.magnitude())
print("Vector normalized (unit vector)")
print(v1.normalized())

print("Magnitude")
v1 = Vector([-0.221,7.437])
print(v1.magnitude())

v1 = Vector([8.813,-1.331, -6.247])
print(v1.magnitude())

print("Vector direction")
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

print("Compare dots with other formula")
v1 = Vector([-5.955,-4.904,-1.874])
v2 = Vector([-4.496,-8.755,7.103])
print(v1.dot(v2))
v1 = Vector([3.183,-7.627])
v2 = Vector([-2.668,5.319])
print(v1.angle_with(v2))
print("%s == %s * %s * %s" % (v1.dot(v2),v1.magnitude(), v2.magnitude(), Decimal(math.cos(v1.angle_with(v2)))))

print("Angles")
v1 = Vector([1,2,-1])
v2 = Vector([3,1,0])
print(v1.angle_with(v2))


v1 = Vector([3.183,-7.627])
v2 = Vector([-2.668,5.319])
print(v1.angle_with(v2))

v1 = Vector([7.35,0.221,5.188])
v2 = Vector([2.751,8.259,3.985])
print(v1.angle_with(v2,inDegrees=True))

#print("Are the 2 vectors parallel?")
#v1 = Vector([2,3,5])
#v2 = Vector([6,9,15])
#print(v1.is_parallel_to(v2))

v1 = Vector([-7.579,-7.88])
v2 = Vector([22.737,23.64])
print("v1: %s, v2: %s" % (v1,v2))
print("Are the 2 vectors parallel?")
print(v1.is_parallel_to(v2))
print("Are the 2 vectors orthogonal?")
print(v1.is_orthogonal_to(v2))
print() 

v1 = Vector([-2.029,9.97,4.172])
v2 = Vector([-9.231,-6.639,-7.245])
print("v1: %s, v2: %s" % (v1,v2))
print("Are the 2 vectors parallel?")
print(v1.is_parallel_to(v2))
print("Are the 2 vectors orthogonal?")
print(v1.is_orthogonal_to(v2))
print() 

v1 = Vector([-2.328,-7.284,-1.214])
v2 = Vector([-1.821,1.072,-2.94])
print("v1: %s, v2: %s" % (v1,v2))
print("Are the 2 vectors parallel?")
print(v1.is_parallel_to(v2))
print("Are the 2 vectors orthogonal?")
print(v1.is_orthogonal_to(v2))
print() 

v1 = Vector([2.118,4.827])
v2 = Vector([0,0])
print("v1: %s, v2: %s" % (v1,v2))
print("Are the 2 vectors parallel?")
print(v1.is_parallel_to(v2))
print("Are the 2 vectors orthogonal?")
print(v1.is_orthogonal_to(v2))
print() 
#v1 = Vector([])
