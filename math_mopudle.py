from array import array
import main_moudle
from math import degrees, pi, sin, cos, sin, asin, acos, atan, atan2, sqrt, radians
import numpy as np
import time
#information detail Robot
L1 = 8
L2 = 18.5
L3 = 21.5
H = 30 #day la chieu cao dat lam gia tri khi dung tinh tu khop 1 den khau cuoi cung



def xinchao(a):
    a[0] = 1
    a[1] = 2
    a[2] = 3
    



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


def Dangdi_trot(type_move, TM, s, h, sampling_time):
    # do phan giai thoi gian 
    '''N/v: goi ham toa do de tra ve cac goc cho canh tay'''

    if type_move == 0:
        print("dung")
    else:
        array =  np.arange(0, 2*TM + sampling_time, sampling_time)
        for t in array:
            time.sleep(sampling_time)
            if (type_move == 1):
                Ditoi(TM, s, h, type_move, t)
            if(type_move == 2):
                DiLui(TM, s, h, type_move, t)

    

def Ditoi(TM, s, h, type_move, t):
    '''Neu a == 1 thi di toi '''
    x1 = -L1
    z1 = round(Congthuc_toado_ditoi_chan_truoc(TM, s, h, t)[0],2)
    y1 = round(Congthuc_toado_ditoi_chan_truoc( TM, s, h, t)[1],2)
    print("     toa do cua khau cuoi 1: x =", x1,", y =", y1,", z =", z1)
    IK(x1, y1, z1)

    x2 = L1
    z2 = round(Congthuc_toado_ditoi_chan_sau(TM, s, h, t)[0],2)
    y2 = round(Congthuc_toado_ditoi_chan_sau(TM, s, h, t)[1],2)
    print("     toa do cua khau cuoi 2: x =", x2,", y =", y2,", z =", z2)
    IK(x2, y2, z2)

def DiLui(TM, s, h, type_move, t):
    '''Neu a == 2 thi di lui '''
    x1 = -L1
    z1 = round(Congthuc_toado_dilui_chan_truoc(TM, s, h, t )[0],2)
    y1 = round(Congthuc_toado_dilui_chan_truoc(TM, s, h, t)[1],2)
    print("     toa do cua khau cuoi 1: x =", x1,", y =", y1,", z =", z1)
    IK(x1, y1, z1)


    x2 = L1
    z2 = round(Congthuc_toado_ditoi_chan_sau(TM, s, h, t )[0],2)
    y2 = round(Congthuc_toado_ditoi_chan_sau(TM, s, h, t)[1],2)
    print("     toa do cua khau cuoi 2: x =", x2,", y =", y2,", z =", z2)


  

def Congthuc_toado_ditoi_chan_truoc(TM, s, h, t):
    '''Ham nay tra toa do tinh ra tu quy dao ve cac bien x,y,z'''    
    if (t < TM/2):
        Ps = s*(t/TM - 1/(4*pi)*sin(4*pi*t/TM)) - s/2
        Ph = - H + 2*h*(t/TM - 1/(4*pi)*sin(4*pi*t/TM))
    if (TM/2 <= t < TM):
        Ps = s*(t/TM - 1/(4*pi)*sin(4*pi*t/TM)) - s/2
        Ph = - H + 2*h*(1 - t/TM + 1/(4*pi)*sin(4*pi*t/TM))
    if (TM <= t < (3*TM/2)):
        Ps = s*((2*TM - t)/TM - 1/(4*pi)*sin(4*pi*(2*TM - t)/TM)) - s/2
        Ph = - H 
    if ((3*TM/2) <= t <= 2*TM ):
        Ps = s*((2*TM - t)/TM - 1/(4*pi)*sin(4*pi*(2*TM - t)/TM)) - s/2
        Ph = - H 
    toa_do = [Ps,Ph]
    return toa_do

def Congthuc_toado_ditoi_chan_sau(TM, s, h, t):
    '''Ham nay tra toa do tinh ra tu quy dao ve cac bien x,y,z'''    
    if (t < TM):
        Ps = -s*(t/TM - 1/(4*pi)*sin(4*pi*t/TM)) + s/2
        Ph = - H 
    if (TM <= t < 3*TM/2 ):
        Ps = s*((t - TM)/TM - 1/(4*pi)*sin(4*pi*(t - TM)/TM)) - s/2
        Ph = - H + 2*h*((t - TM)/TM - 1/(4*pi)*sin(4*pi*(t - TM)/TM))
    if ((3*TM/2) <= t <= 2*TM):
        Ps = s*((t - TM)/TM - 1/(4*pi)*sin(4*pi*(t - TM)/TM)) - s/2
        Ph = - H + 2*h*(1 - (t - TM)/TM + 1/(4*pi)*sin(4*pi*(t - TM)/TM))
    toa_do = [Ps,Ph]
    return toa_do

def Congthuc_toado_dilui_chan_truoc(TM, s, h, t):
    '''Ham nay tra toa do tinh ra tu quy dao ve cac bien x,y,z'''    
    if (t < TM/2):
        Ps = -s*(t/TM - 1/(4*pi)*sin(4*pi*t/TM)) + s/2
        Ph = - H + 2*h*(t/TM - 1/(4*pi)*sin(4*pi*t/TM))
    if (t >= TM/2 and t <= TM ):
        Ps = -s*(t/TM - 1/(4*pi)*sin(4*pi*t/TM)) + s/2
        Ph = - H + 2*h*(1 - t/TM + 1/(4*pi)*sin(4*pi*t/TM))
    if (t  >= TM ):
        Ps = -s*((2*TM - t)/TM - 1/(4*pi)*sin(4*pi*(2*TM - t)/TM)) + s/2
        Ph = - H 
    toa_do = [Ps,Ph]
    return toa_do

def Congthuc_toado_dilui_chan_sau(TM, s, h, t):

    '''Ham nay tra toa do tinh ra tu quy dao ve cac bien x,y,z'''    
    if (t < TM):
        Ps = -s*(t/TM - 1/(4*pi)*sin(4*pi*t/TM)) + s/2
        Ph = - H 
    if (t >= TM and t < 3*TM/2):
        Ps = -s*((t - TM)/TM - 1/(4*pi)*sin(4*pi*(t - TM)/TM)) + s/2
        Ph = - H + 2*h*((t - TM)/TM - 1/(4*pi)*sin(4*pi*(t - TM)/TM))
    if (t  >= 3*TM/2):
        Ps = -s*((t - TM)/TM - 1/(4*pi)*sin(4*pi*(t - TM)/TM)) + s/2
        Ph = - H + 2*h*(1 - (t - TM)/TM + 1/(4*pi)*sin(4*pi*(t - TM)/TM))
    toa_do = [Ps,Ph]
    return toa_do

def Dangdi_crawl(type_move, TM, s, h, sampling_time):
    print("da di toi day")