from math import degrees, pi, sin, cos, sin, asin, acos, atan, atan2, sqrt, radians
import numpy as np
import time

#information detail Robot
L1 = 7
L2 = 20
L3 = 21
H = 15 #day la chieu cao dat lam gia tri khi dung tinh tu khop 1 den khau cuoi cung

_a = [7.4, -26.75, 5.5]
a = np.array(_a)

def xinchao():
    x = -7.4
    y = -26.75
    a = atan(y/x)
    b = atan2(y,x)
    c = radians(90)
    print("a = ",a)
    print("b = ",b)
    print("c = ",c)



def tempt(x, y , z):
    c =x + y + z
    round(c, 2)
    print(c)

def IK(x, y , z):
    try:
        if x > 0:
            f1 = pi - ( - atan(y/x) + atan(sqrt(x**2 + y**2  - L1**2)/L1))
        else:
            f1 = ( atan(y/x) - atan(sqrt(x**2 + y**2  - L1**2)/L1))
        try:
            f3 = acos((x**2 + y**2 + z**2 - L1**2 - L2**2 - L3**2)/(2*L2*L3))       
        except:
            f3 = 0
        theta_1 = degrees(f1)
        theta_3 = degrees(f3)
        f2 = atan(z/(sqrt(x**2 + y**2 + z**2 - L1**2))) - atan((L3*sin(radians(theta_3)))/(L2 + L3*cos(radians(theta_3))))
        theta_2 = degrees(f2)
        theta = [theta_1, theta_2, theta_3]
        print('     goc 1 =',theta[0], ', goc 2 =',theta[1], ',goc 3 =',theta[2])

    except:
        print("Viet ham dua cac chan de robot 4 chan dung im")

    
    return(theta)

def Dangdi(t):
    if t == 1:
        print("ban chon kieu di crawl, chua viet")
    if t == 2:
        print("ban chon kieu di trot")
        Ditoi()
        

def Ditoi():
    # a la bien di toi di lui re trai re phai 
    a = int(input("Nhap 1: Di toi \ Nhap -1: Di lui "))
    TM = float(input("Nhap chu ky TM = "))
    s = float(input("Nhap chu ky s = "))
    h = float(input("Nhap chu ky h = "))
    b = float(input("Nhap do phan giai t = "))
    if a == 1:
        print("Di toi")
        Vantoc_trot(TM, s, h, a, b)
    if a == -1:
        print("Di lui")
        Vantoc_trot(TM, s, h, a, b)

def Vantoc_trot(TM, s, h, a, b):
    # do phan giai thoi gian 
    for t in np.arange(0, 2*TM + b, b):
        if (t < TM/2):
            print("Dang o nua chi ki 1:", t )
            time.sleep(b)
            Quydao_trot(t, TM, s, h, a, b)
        if (t >= TM/2 and t < (TM + b)):
            print("Dang o nua chi ki 2:", t )
            time.sleep(b)
            Quydao_trot(t, TM, s, h, a, b)
        if (t  >= TM + b):
            print("Dang o  chi ki di ve:", t)
            Quydao_trot(t, TM, s, h, a, b)


def Quydao_trot(t, TM, s, h, a, b):
    if (a == 1):
        x = -L1
        z = Congthuc_toado(t, TM, s, h, a, b)[0]
        y = Congthuc_toado(t, TM, s, h, a, b)[1]
        print("     toa do cua khau cuoi: ", x, y, z)
        IK(x, y , z)

def Congthuc_toado(t, TM, s, h, a, b):    
    if (t < TM/2):
        Ps = s*(t/TM - 1/(4*pi)*sin(4*pi*t/TM)) - s/2
        Ph = - H + 2*h*(t/TM - 1/(4*pi)*sin(4*pi*t/TM))
    if (t >= TM/2 and t < TM + b):
        Ps = s*(t/TM - 1/(4*pi)*sin(4*pi*t/TM)) - s/2
        Ph = - H + 2*h*(1 - t/TM + 1/(4*pi)*sin(4*pi*t/TM))
    if (t  >= TM + b):
        Ps = s*((2*TM - t)/TM - 1/(4*pi)*sin(4*pi*(2*TM - t)/TM)) - s/2
        Ph = - H 
    toa_do = [Ps,Ph]
    return toa_do