import math_mopudle
from math import pi, sin, cos, asin, acos, atan2, sqrt
import numpy

a = [-7.4, -26.75, 5.5]
TM = 1 # chu ki buoc
s = 10 # khoang cach sai buoc chan
h = 6 # do cao nhac chan len
sampling_time  = 0.05 # thoi gian lay mau 



def Di_chuyen(type_move: int, direction : int):
    if type_move == 1:
        math_mopudle.Dangdi_trot(direction, TM, s, h, sampling_time)
    if type_move == 2:
        math_mopudle.Dangdi_crawl(direction, TM, s, h, sampling_time)

