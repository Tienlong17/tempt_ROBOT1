import math_mopudle
from math import pi, sin, cos, asin, acos, atan2, sqrt
import numpy
a = [7.4, -26.75, 5.5]

math_mopudle.xinchao()
c = math_mopudle.IK(a[0], a[1], a[2])
print('goc 1 =',c[0], ',goc 2 =',c[1], ',goc 3 =',c[2])

t =input("Nhap 1: crwal \ Nhap 2: trot")
math_mopudle.Dangdi(int(t))