# feh = -1.58404580153
import numpy as np

m4_dist = 11.399
feh_ab = -1.67662162162 # -1.49561947117 #-1.5188905482 # 
feh_c = -1.67662162162 # -1.71499214554 #-1.33141497694 # 

# def b_ab(per, dist):
#     return v_ab(per, dist)
# def b_c(per, dist):
#     return v_ab(per, dist)
# def v_ab(per, dist):
#     mh = get_mh(feh_ab)
#     return 1.067 + 0 * per + 0.502 * mh + 0.108 * mh**2 + dist
# def v_c(per, dist):
#     return v_ab(per, dist)
def j_ab(per, dist):
    zpt = -0.506 + 0.175 * feh_ab # -0.7994
    return zpt + -1.981 * per + dist
def j_c(per, dist):
    zpt = -1.069 + 0.148 * feh_c # -1.31714
    return zpt + -2.461 * per + dist
def h_ab(per, dist):
    zpt = -0.755 + 0.186 * feh_ab # -1.067
    return  zpt + -2.239 * per + dist
def h_c(per, dist):
    zpt = -1.312 + 0.155 * feh_c # -1.572
    return zpt + -2.696 * per + dist
def k_ab(per, dist):
    zpt = -0.818 + 0.184 * feh_ab # -1.126
    return zpt + -2.274 * per + dist
def k_c(per, dist):
    zpt = -1.371 + 0.153 * feh_c # -1.628
    return zpt + -2.716 * per + dist
def t_ab(per, dist):
    return -0.558 + -2.370 * (per + 0.26) + dist 
def t_c(per, dist):
    return -0.192 + -2.658 * (per + 0.55) + dist 
def f_ab(per, dist):
    return -0.593 + -2.355 * (per + 0.26) + dist 
def f_c(per, dist):
    return -0.240 + -2.979 * (per + 0.55) + dist 

# def get_mh(feh):
#     alpha = 0.3
#     f = 10**alpha
#     mh = feh + np.log10(0.638*f + 0.362)
#     return mh