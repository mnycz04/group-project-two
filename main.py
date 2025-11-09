# main.py
from methods import *
import numpy as np
import pandas as pd


def problem_one():
    f = Function(equation=lambda t, y: np.exp(4 * t - y))
    dfdy = Function(equation=lambda t, y: -1 * np.exp(4 * t - y))
    dfdt = Function(equation=lambda t, y: 4 * np.exp(4 * t - y))
    steps_sizes = (.2, .02, .002)

    initial_t = 0
    initial_y = 1
    stop_t = 3

    exact = Decimal(np.log(((1 * np.exp(12)) / 4) + np.exp(1) - (1 / 4)))
    print('Problem One:')
    print(f'The exact value of y(3) = {exact}.')
    table = pd.DataFrame()
    euler = pd.Series({h: eulers(f, initial_t, initial_y, stop_t, step=h) for h in steps_sizes})
    table['Euler'] = euler
    table['Euler Error'] = pd.Series({h: np.abs((euler[h]) - exact) for h in steps_sizes})
    taylor = pd.Series({h: taylors(f, dfdy, dfdt, initial_t, initial_y, stop_t, step=h) for h in steps_sizes})
    table["Taylor's"] = taylor
    table['Taylor\'s Error'] = pd.Series({h: np.abs((taylor[h]) - exact) for h in steps_sizes})
    runge = pd.Series({h: rk4(f, initial_t, initial_y, stop_t, step=h) for h in steps_sizes})
    table['RK-4'] = runge
    table['RK-4 Error'] = pd.Series({h: np.abs((runge[h]) - exact) for h in steps_sizes})

    print(table)


def problem_two():
    f = Function(equation=lambda t, Y: np.concatenate(
        (
            Y[1:], np.array(
            ((t ** 3) - 2 + (Decimal(str(np.log(float(t)))) * Decimal(str(np.cos(float(Y[0] ** 2)))) * Decimal(
                str(np.exp(-1 * Y[1])))),)
        )
        )
    ))
    initial_conditions = (3, -1)
    initial_eulers = np.array([Decimal(i) for i in initial_conditions])
    approx_euler = (eulers(f, 1, initial_eulers, 3, step=10 ** (-3)))

    print("Problem Two:")
    print("\tEuler's Method")
    print(f'\t\tY(3) = [{approx_euler[0]}, {approx_euler[1]}]')
    print(f'\t\ty(3) = {approx_euler[0]}')

    initial_rk4 = np.array([Decimal(i) for i in initial_conditions])
    approx_rk4 = (rk4(f, 1, initial_rk4, 3, step=10 ** (-3)))
    print("\tRK-4")
    print(f'\t\tY(3) = [{approx_rk4[0]}, {approx_rk4[1]}]')
    print(f'\t\ty(3) = {approx_rk4[0]}')


def problem_three():
    f = Function(equation=lambda t, Y: np.concatenate((Y[1:],
                                                       np.array(
                                                           ((-4 * Y[1] - 5 * Y[0]) + Decimal(str(np.sin(float(t)))),))
                                                       )))

    initial_conditions = (0, 1)
    initial_eulers = np.array([Decimal(i) for i in initial_conditions])
    approx_eulers = eulers(f, 0, initial_eulers, 3, step=10 ** (-5))
    print('Problem Three:')
    print("\tEuler's Method")
    print(f'\t\tY(3) = [{approx_eulers[0]}, {approx_eulers[1]}]')
    print(f'\t\ty(3) = {approx_eulers[0]}')

    initial_rk4 = np.array([Decimal(i) for i in initial_conditions])
    approx_rk4 = rk4(f, 0, initial_rk4, 3, step=10 ** (-5))
    print("\tRK-4")
    print(f'\t\tY(3) = [{approx_rk4[0]}, {approx_rk4[1]}]')
    print(f'\t\ty(3) = {approx_rk4[0]}')


def problem_four():
    initial = Function(equation=lambda x: (4 * x - (x ** 2)))
    boundary = Function(equation=lambda t: 5 * (np.sin(np.pi * t)))

    def u(x):
        if 0 <= x < 2.5:
            return 5 * np.sin(np.pi * (9 - (4 * x)))
        else:
            return (4 * (x - 2.25)) - ((x - 2.25) ** 2)

    print("Problem Four:")
    table = pd.DataFrame()
    exact = Function(equation=u)
    table['Exact'] = {i: exact(i) for i in np.linspace(0, 6, int(6 / .3))}
    approx = upwind_scheme(initial, boundary, (0, 6), -.25, .6, .3, 9)[-1]
    table['Approximation'] = approx
    error = np.abs(np.array([exact(i) for i in np.linspace(0, 6, int(6 / .3))]) - approx)
    table['Error'] = error
    print(table)

    average_error = sum(np.abs(error)) / len(error)
    print(f'Average absolute error is {average_error}.')


if __name__ == '__main__':
    pd.set_option('display.max_columns', 5000)
    pd.set_option('display.max_rows', 500)

    problem_one()
    problem_two()
    problem_three()
    problem_four()

    exit(0)
