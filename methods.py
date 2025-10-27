from function import Function
import numpy as np
from decimal import *

def eulers(dydt: Function, t0: Decimal, y0: Decimal, tn:Decimal, *, step: Decimal = .1, ):
    """
    Approximates a ODE of f(t, y) starting at (t0, y0) and going till tn.
    Uses a default step size of .1 unless step is specified
    :param dydt: ODE function in terms of f(t, y)
    :param t0: initial time
    :param y0: initial u
    :param tn: point in time to calculate up to
    :param step: step size, with default value of .1
    :return:
    """
    pass

def taylors(dydt: Function):
    pass

def rk4(dydt: Function):
    pass