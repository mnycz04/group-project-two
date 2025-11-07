from function import Function
from decimal import Decimal


def eulers(dydt: Function, t, y, tn, *, step=Decimal(.1)):
    t, tn, step = Decimal(str(t)), Decimal(str(tn)), Decimal(str(step))
    if y is float or y is int:
        y = Decimal(y)


    overflow = 0
    while t < tn:
        y += dydt(t, y) * ((t + step) - t)
        t += step

        overflow += 1
        if overflow > 2 ** 32:
            raise (IndexError("Overflow limit exceeded"))

    return y


def taylors(f: Function, dfdy: Function, dfdt: Function, t, y, tn, *, step=Decimal(.1)):
    t, y, tn, step = Decimal(str(t)), Decimal(str(y)), Decimal(str(tn)), Decimal(str(step))

    while t < tn:
        y += (step * f(t, y)) + (((step ** 2) / 2) * (dfdy(t, y) * f(t, y) + dfdt(t, y)))

        t += step

    return y


def rk4(f: Function, t, y, tn, *, step=Decimal(.1)):
    t, y, tn, step = Decimal(str(t)), Decimal(str(y)), Decimal(str(tn)), Decimal(str(step))

    while t < tn:
        k1 = f(t, y)
        k2 = f(t + (step / 2), y + (step / 2) * k1)
        k3 = f(t + (step / 2), y + (step / 2) * k2)
        k4 = f(t + step, y + step * k3)

        y += (step / 6) * (k1 + 2 * k2 + 2 * k3 + k4)

        t += step

    return y
