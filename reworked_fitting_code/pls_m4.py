# feh = -1.58404580153
feh = -1.56749344383

def b_ab(per, dist):
    return 0.506 + -0.981 * per + 0.175 * feh + dist
def b_c(per, dist):
    return 1.069 + -0.461 * per + 0.148 * feh + dist
def v_ab(per, dist):
    return 0.755 + -1.239 * per + 0.186 * feh + dist
def v_c(per, dist):
    return 1.312 + -0.696 * per + 0.155 * feh + dist
def j_ab(per, dist):
    return -0.506 + -1.981 * per + 0.175 * feh + dist
def j_c(per, dist):
    return -1.069 + -2.461 * per + 0.148 * feh + dist
def h_ab(per, dist):
    return -0.755 + -2.239 * per + 0.186 * feh + dist
def h_c(per, dist):
    return -1.312 + -2.696 * per + 0.155 * feh + dist
def k_ab(per, dist):
    return -0.818 + -2.274 * per + 0.184 * feh + dist
def k_c(per, dist):
    return -1.371 + -2.716 * per + 0.153 * feh + dist
def t_ab(per, dist):
    return -0.558 + -2.370 * (per + 0.26) + dist 
def t_c(per, dist):
    return -0.192 + -2.658 * (per + 0.55) + dist 
def f_ab(per, dist):
    return -0.593 + -2.355 * (per + 0.26) + dist 
def f_c(per, dist):
    return -0.240 + -2.979 * (per + 0.55) + dist 
