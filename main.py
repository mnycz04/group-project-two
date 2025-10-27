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

    table = pd.DataFrame()
    table['Euler'] = pd.Series({h: eulers(f, initial_t, initial_y, stop_t, step=h) for h in steps_sizes})
    table["Taylor's"] = pd.Series({h: taylors(f, dfdy, dfdt, initial_t, initial_y, stop_t, step=h) for h in steps_sizes})
    table['RK-4'] = pd.Series({h: rk4(f, initial_t, initial_y, stop_t, step=h) for h in steps_sizes})

    print(table)


if __name__ == '__main__':
    pd.set_option('display.max_columns', 5000)
    pd.set_option('display.max_rows', 500)
    problem_one()

    exit(0)