
from math import degrees, pi, sin, cos, sin, asin, acos, atan, atan2, sqrt, radians
import numpy as np
import time
import matplotlib.pyplot as plt
#information detail Robot
L1 = 7
L2 = 20
L3 = 21
H = 15 #day la chieu cao dat lam gia tri khi dung tinh tu khop 1 den khau cuoi cung

A =[]
B =[]

C =[]
D =[]

E =[]
F =[]

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

def IK(x: float, y: float , z: float):
    try:
        if x > 0:
            f11 = ( -atan(y/x) - atan(sqrt(x**2 + y**2  - L1**2)/L1))
        else:
            f11 = ( atan(y/x) - atan(sqrt(x**2 + y**2  - L1**2)/L1))
        theta_11 = round(degrees(f11), 2) #lam tron 2 chu so
        theta_31 = round(degrees(f11),2)
        
        try:
            f13 = acos((x**2 + y**2 + z**2 - L1**2 - L2**2 - L3**2)/(2*L2*L3))       
        except:
            f13 = 0
        theta_13 = round(degrees(f13),2)
        theta_33 = round(degrees(f13),2)

        f12 = atan(z/(sqrt(x**2 + y**2 + z**2 - L1**2))) - atan((L3*sin(radians(theta_13)))/(L2 + L3*cos(radians(theta_13))))
        theta_12 = round(degrees(f12),2)
        theta_32 = round(degrees(f12),2)
        theta = [theta_11, theta_12, theta_13, theta_31, theta_32, theta_33]
        print('     Chan truoc: goc 1 =',theta[0], ', goc 2 =',theta[1], ',goc 3 =',theta[2], end ='\n')
        #print('     Chan sau: goc 1 =',theta[3], ', goc 2 =',theta[4], ',goc 3 =',theta[5], end ='\n')

    except:
        print("Viet ham dua cac chan de robot 4 chan dung im")

    
    return(theta)

def Dangdi(t):
    if t == 1:
        print("ban chon kieu di crawl, chua viet")
    if t == 2:
        print("ban chon kieu di trot")
        a = int(input("Nhap 1: Di toi \ Nhap -1: Di lui "))
        Di_chhuyen(a)
        

def Di_chhuyen(a):
    '''Ham nay de di toi'''
    # a la bien di toi di lui re trai re phai 
    
    TM = float(input("Nhap chu ky TM = "))
    s = float(input("Nhap chu ky s = "))
    h = float(input("Nhap chu ky h = "))
    b = float(input("Nhap do phan giai t = "))
    if a == 1:
        print("Di toi")
        Thoi_gian(TM, s, h, a, b)

def Thoi_gian(TM, s, h, a, b):
    # do phan giai thoi gian 
    for t in np.arange(0, 2*TM + b, b):
        if (t < TM/2):
            print("Dang o nua chu ki 1: t =", t )
            time.sleep(b)
            Quydao_trot(t, TM, s, h, a, b)
        if (t >= TM/2 and t < (TM + b)):
            print("Dang o nua chu ki 2: t =", t )
            time.sleep(b)
            Quydao_trot(t, TM, s, h, a, b)
        if (t  >= TM + b):
            print("Dang o  chu ki di ve: t =", t)
            Quydao_trot(t, TM, s, h, a, b)


def Quydao_trot(t, TM, s, h, a, b):
    '''N/v: goi ham toa do de tra ve cac goc cho canh tay'''
    if (a == 1):
        x1 = -L1
        z1 = round(Congthuc_toado_thuan(t, TM, s, h, a, b)[0],2)
        y1 = round(Congthuc_toado_thuan(t, TM, s, h, a, b)[1],2)
        print("     toa do cua khau cuoi 1: x =", x1,", y =", y1,", z =", z1)
        IK(x1, y1, z1)
        if(t < TM + b):
            A.append(y1)
            B.append(z1)
        if(t >= TM + b and t < 2.5*TM/2):
            C.append(y1)
            D.append(z1)

        x2 = L1
        z2 = round(Congthuc_toado_nghich(t, TM, s, h, a, b)[0],2)
        y2 = round(Congthuc_toado_nghich(t, TM, s, h, a, b)[1],2)
        print("     toa do cua khau cuoi 2: x =", x2,", y =", y2,", z =", z2)
        IK(x2, y2, z2)
        if(t < TM + b):
            E.append(y2)
            F.append(z2)

def Congthuc_toado_thuan(t, TM, s, h, a, b):
    '''Ham nay tra toa do tinh ra tu quy dao ve cac bien x,y,z'''    
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

def Congthuc_toado_nghich(t, TM, s, h, a, b):
    '''Ham nay tra toa do tinh ra tu quy dao ve cac bien x,y,z'''    
    if (t < TM):
        Ps = s*(t/TM - 1/(4*pi)*sin(4*pi*t/TM)) - s/2
        Ph = - H 
    if (t >= TM and t < 3*TM/2 + b):
        Ps = s*((t - TM)/TM - 1/(4*pi)*sin(4*pi*(t - TM)/TM)) - s/2
        Ph = - H + 2*h*((t - TM)/TM - 1/(4*pi)*sin(4*pi*(t - TM)/TM))
    if (t  >= 3*TM/2 + b):
        Ps = s*((t - TM)/TM - 1/(4*pi)*sin(4*pi*(t - TM)/TM)) - s/2
        Ph = - H + 2*h*(1 - (t - TM)/TM + 1/(4*pi)*sin(4*pi*(t - TM)/TM))
    toa_do = [Ps,Ph]
    return toa_do

