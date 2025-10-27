# main.py
from methods import *


if __name__ == '__main__':
    f = Function(equation=lambda t, y:  1 - t + (4 * y))
    dfdy = Function(equation=lambda t, y: 4)
    dfdt = Function(equation=lambda t, y: -1)
    print(eulers(f, 0, 1, 1))
    print(taylors(f, dfdy, dfdt, 0, 1, 1))
    print(rk4(f, 0, 1, 1))

    exit(0)