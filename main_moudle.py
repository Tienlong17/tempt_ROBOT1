import math_mopudle
from math import pi, sin, cos, asin, acos, atan2, sqrt
import numpy
import matplotlib.pyplot as plt
a = [-7.4, -26.75, 5.5]

math_mopudle.xinchao()
math_mopudle.IK(a[0], a[1], a[2])


math_mopudle.Dangdi()

fig, (ax1, ax2, ax3) = plt.subplots(1,3, figsize=(10,4), sharey=True, dpi=120)

#plt.plot(math_mopudle.B,math_mopudle.A)
#plt.plot(math_mopudle.D,math_mopudle.C)

ax1.plot(math_mopudle.B,math_mopudle.A,'go',label='Chan le' )
ax2.plot(math_mopudle.D,math_mopudle.C,'go',label='Chan le' )
ax3.plot(math_mopudle.F,math_mopudle.E,label='Chan le' )
plt.show()