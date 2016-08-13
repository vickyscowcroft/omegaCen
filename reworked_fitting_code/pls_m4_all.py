# feh = -1.58404580153
import numpy as np
#feh_ab = -1.67662162162 # -1.49561947117 #-1.5188905482 # 
#feh_c = -1.67662162162 # -1.71499214554 #-1.33141497694 # 

m4_dist = 11.399

def j_ab(per, dist):
    zpt = 10.946 - m4_dist # -0.453
    #return zpt + -1.981 * per + dist
    return zpt + -2.030 * per + dist
def j_c(per, dist):
    zpt = 10.634 - m4_dist # -0.765
    #zpt = -1.31714
    return zpt + -2.02 * per + dist
def h_ab(per, dist):
    zpt = 10.537 - m4_dist # -0.862
    #zpt = -1.067
    #return  zpt + -2.239 * per + dist
    return zpt + -2.215 * per + dist
def h_c(per, dist):
    zpt = 10.232 - m4_dist # -1.167
    #zpt = -1.572
    return zpt + -2.34 * per + dist
def k_ab(per, dist):
    zpt = 10.410 - m4_dist # -0.989
    #zpt = -1.126
    return zpt + -2.372 * per + dist
def k_c(per, dist):
    zpt = 10.058 - m4_dist # -1.341
    #zpt = -1.628
    return zpt + -2.44 * per + dist
def t_ab(per, dist):
    zpt = 10.841 - m4_dist # -0.558
    return zpt + -2.370 * (per + 0.26) + dist 
def t_c(per, dist):
    zpt = 11.207 - m4_dist # -0.192
    return zpt + -2.658 * (per + 0.55) + dist 
def f_ab(per, dist):
    zpt = 10.806 - m4_dist # -0.593
    return zpt + -2.355 * (per + 0.26) + dist 
def f_c(per, dist):
    zpt = 11.159 - m4_dist # -0.240
    return zpt + -2.979 * (per + 0.55) + dist 
