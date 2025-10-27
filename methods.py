from function import Function
import numpy as np
from decimal import Decimal


def eulers(dydt: Function, t, y, tn, *, step=Decimal(.1)):
    """
    Approximates a ODE of f(t, y) starting at (t0, y0) and going till tn.
    Uses a default step size of .1 unless step is specified
    :param dydt: ODE function in terms of f(t, y)
    :param t: initial time
    :param y: initial u
    :param tn: point in time to calculate up to
    :param step: step size, with default value of .1
    :return:
    """
    t, y, tn, step = Decimal(t), Decimal(y), Decimal(tn), Decimal(step)

    overflow = 0
    while t < tn:
        y += dydt(t, y) * ((t + step) - t)
        t += step

        overflow += 1
        if overflow > 2 ** 16:
            raise(IndexError("Overflow limit exceeded"))

    return y

    pass


def taylors(f: Function, dfdy: Function, dfdt: Function, t, y, tn, *, step=Decimal(.1)):

    t, y, tn, step = Decimal(t), Decimal(y), Decimal(tn), Decimal(step)

    while( t < tn):
        y += (step * f(t, y)) + (((step ** 2) / 2) * (dfdy(t, y) * f(t, y) + dfdt(t, y)))

        t += step

    return y


def rk4(dydt: Function):
    pass
