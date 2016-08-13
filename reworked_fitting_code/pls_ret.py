import numpy as np

def j_ab(per, dist):
    return 18.2026702188 + -1.573203478 * (per + 0.26) + dist 
def j_c(per, dist):
    return 18.33925 + -1.60331591825 * (per + 0.4894) + dist 
def h_ab(per, dist):
    return 17.992368477 + -1.96326168955 * (per + 0.26) + dist 
def h_c(per, dist):
    return 18.209 + -1.43178728314 * (per + 0.4894) + dist 
def k_ab(per, dist):
    return 17.8896311889 + -1.97918482052 * (per + 0.26) + dist 
def k_c(per, dist):
    return 18.126 + -2.40568395772 * (per + 0.4894) + dist 
def t_ab(per, dist):
    return 17.8696264419 + -2.34573793028 * (per + 0.26) + dist 
def t_c(per, dist):
    return 18.10225 + -0.449012238418 * (per + 0.4894) + dist 
def f_ab(per, dist):
    return 17.8242500243 + -2.62589061231 * (per + 0.26) + dist 
def f_c(per, dist):
    return 18.11275 + -2.71786291369 * (per + 0.4894) + dist 
