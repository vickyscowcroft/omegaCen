# feh = -1.58404580153
import numpy as np
feh_ab = -1.67662162162 # -1.49561947117 #-1.5188905482 # 
feh_c = -1.67662162162 # -1.71499214554 #-1.33141497694 # 

def b_ab(per, dist):
    return v_ab(per, dist)
def b_c(per, dist):
    return v_ab(per, dist)
def v_ab(per, dist):
    mh = get_mh(feh_ab)
    return 1.067 + 0 * per + 0.502 * mh + 0.108 * mh**2 + dist
def v_c(per, dist):
    return v_ab(per, dist)
def j_ab(per, dist):
    return -0.506 + -1.981 * per + 0.175 * feh_ab + dist
def j_c(per, dist):
    return -1.069 + -2.461 * per + 0.148 * feh_c + dist
def h_ab(per, dist):
    return -0.755 + -2.239 * per + 0.186 * feh_ab + dist
def h_c(per, dist):
    return -1.312 + -2.696 * per + 0.155 * feh_c + dist
def k_ab(per, dist):
    return -0.818 + -2.274 * per + 0.184 * feh_ab + dist
def k_c(per, dist):
    return -1.371 + -2.716 * per + 0.153 * feh_c + dist
def t_ab(per, dist):
    return -0.558 + -2.370 * (per + 0.26) + dist 
def t_c(per, dist):
    return -0.192 + -2.658 * (per + 0.55) + dist 
def f_ab(per, dist):
    return -0.593 + -2.355 * (per + 0.26) + dist 
def f_c(per, dist):
    return -0.240 + -2.979 * (per + 0.55) + dist 

def get_mh(feh):
    alpha = 0.3
    f = 10**alpha
    mh = feh + np.log10(0.638*f + 0.362)
    return mh