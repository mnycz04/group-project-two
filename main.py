# main.py
from methods import *
import numpy as np
import pandas as pd

def problem_one():
    f = Function(equation=lambda t, y: np.exp(4 * t - y))
    dfdy = Function(equation=lambda t, y: -1 * np.exp(4 * t -y))
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


if __name__ == '__main__':
    pd.set_option('display.max_columns', 5000)
    pd.set_option('display.max_rows', 500)
    problem_one()

    exit(0)