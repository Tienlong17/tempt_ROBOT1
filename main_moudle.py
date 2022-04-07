import math_mopudle
from math import pi, sin, cos, asin, acos, atan2, sqrt
import numpy
from matplotlib import pyplot as plt
a = [-7.4, -26.75, 5.5]

math_mopudle.xinchao()
math_mopudle.IK(a[0], a[1], a[2])

t =input("Nhap 1: crwal \ Nhap 2: trot  Ban chon: ")
math_mopudle.Dangdi(int(t))

plt.plot(math_mopudle.B,math_mopudle.A, linestyle = "--", marker = '.')
plt.show()