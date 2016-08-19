import numpy as np

dist_ret = 18.48 # https://arxiv.org/pdf/1112.3171v1.pdf

def j_ab(per, dist):
    zpt = 18.2026702188 - dist_ret
    return zpt + -1.573203478 * (per + 0.26) + dist 
def j_c(per, dist):
    zpt = 18.33925 - dist_ret
    return zpt + -1.60331591825 * (per + 0.4894) + dist 
def h_ab(per, dist):
    zpt = 17.992368477 - dist_ret
    return zpt + -1.96326168955 * (per + 0.26) + dist 
def h_c(per, dist):
    zpt = 18.209 - dist_ret
    return zpt + -1.43178728314 * (per + 0.4894) + dist 
def k_ab(per, dist):
    zpt = 17.8896311889 - dist_ret
    return zpt + -1.97918482052 * (per + 0.26) + dist 
def k_c(per, dist):
    zpt = 18.126 - dist_ret
    return zpt + -2.40568395772 * (per + 0.4894) + dist 
def t_ab(per, dist):
    zpt = 17.8696264419 - dist_ret
    return zpt + -2.34573793028 * (per + 0.26) + dist 
def t_c(per, dist):
    zpt = 18.10225 - dist_ret
    return zpt + -0.449012238418 * (per + 0.4894) + dist 
def f_ab(per, dist):
    zpt = 17.8242500243 - dist_ret
    return zpt + -2.62589061231 * (per + 0.26) + dist 
def f_c(per, dist):
    zpt = 18.11275 - dist_ret
    return zpt + -2.71786291369 * (per + 0.4894) + dist 
