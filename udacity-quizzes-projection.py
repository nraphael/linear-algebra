import math
from Vector_with_decimals import Vector
from decimal import Decimal, getcontext

print("Vector addition")
v1 = Vector([8.218, -9.341])
v2 = Vector([-1.129, 2.111])
print(v1 + v2)

print("Vector projection")
print(v1.projection_onto(v2))

print("Vector projection2")
v1 = Vector([3.039, 1.879])
v2 = Vector([0.825, 2.036])
print(v1.projection_onto(v2))

print("vector_perp")
v1 = Vector([-9.88, -3.264, -8.159])
v2 = Vector([-2.155, -9.353, -9.473])
print(v1.perp_to(v2))

print("\nv_proj + v_perp")
v1 = Vector([3.009, -6.172, 3.692, -2.51])
v2 = Vector([6.404, -9.144, 2.759, 8.718])
v_proj = v1.projection_onto(v2)
v_perp = v1.perp_to(v2)
print("%s + %s" % (v_proj, v_perp))

print("1 -2")
v1 = Vector([-5,-6])
v2 = Vector([-3,-2])
print("%s - %s" % (v1,v2))
print(v1 -v2)
