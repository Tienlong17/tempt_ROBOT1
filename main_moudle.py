import math_mopudle
from math import pi, sin, cos, asin, acos, atan2, sqrt
import numpy

a = [-7.4, -26.75, 5.5]
TM = 2 # chu ki buoc
s = 6 # khoang cach sai buoc chan
h = 4 # do cao nhac chan len
sampling_time  = 0.1 # thoi gian lay mau 

math_mopudle.xinchao(a)
print("a = ",a)


def Di_chuyen(type_move: int):
    math_mopudle.Dangdi_trot(type_move, TM, s, h, sampling_time)


