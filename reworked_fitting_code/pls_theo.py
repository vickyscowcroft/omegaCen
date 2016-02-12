# feh = -1.58404580153
feh = -1.677

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
    return -0.786 + -2.276 * per + 0.184 * feh + dist
def t_c(per, dist):
    return -1.344 + -2.718 * per + 0.152 * feh + dist
def f_ab(per, dist):
    return -0.775 + -2.262 * per + 0.19 * feh + dist
def f_c(per, dist):
    return -1.348 + -2.72 * per + 0.153 * feh + dist
