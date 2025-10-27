# function.py
import matplotlib.pyplot as plt
import numpy as np



class Function:
    def __init__(self, *coefficients, equation=None, name: str = None, domain=(-(2 ** 10), (2 ** 10))):
        if equation is not None:
            self.equation = equation
        elif len(coefficients) > 0:
            self.equation = np.polynomial.Polynomial(coefficients)
        else:
            self.equation = np.polynomial.Polynomial.identity()

        self.name = name
        if domain[0] < domain[1]:
            self.domain = domain
        else:
            self.domain = (domain[1], domain[0])

    @property
    def domain(self):
        return self._domain

    @domain.setter
    def domain(self, new_domain: tuple[float, float]):
        if new_domain[0] < new_domain[1]:
            self._domain = new_domain
        else:
            self._domain = (new_domain[1], new_domain[0])

    def __eq__(self, other):
        if type(other) is Function:
            return np.polynomial.Polynomial.__eq__(self.equation, other.equation)
        else:
            return NotImplemented

    def __add__(self, other):
        if type(other) is Function:
            return self.equation.__add__(other.equation)
        else:
            return NotImplemented

    def __radd__(self, other):
        if type(other) is Function:
            return self.equation.__radd__(other.equation)
        else:
            return NotImplemented

    def __sub__(self, other):
        if type(other) is Function:
            return self.equation.__sub__(other.equation)
        else:
            return NotImplemented

    def __mul__(self, other):
        if type(other) is Function:
            return self.equation.__mul__(other.equation)
        else:
            return NotImplemented

    def __rmul__(self, other):
        if type(other) is Function:
            return self.equation.__rmul__(other.equation)
        else:
            return NotImplemented

    def __divmod__(self, other):
        if type(other) is Function:
            return self.equation.__divmod__(other.equation)
        else:
            return NotImplemented

    def __call__(self, *args):
        return self.equation.__call__(*args)

    def __str__(self):
        if self.name is None:
            return self.equation.__str__()
        else:
            return self.name

    def plot(self, *, domain: tuple[float, float] = None):
        if domain is None:
            x_vals = np.linspace(self.domain[0], self.domain[1], int(10 * (self.domain[1] - self.domain[0])))
        else:
            x_vals = np.linspace(domain[0], domain[1], int(10 * (domain[1] - domain[0])))
        y_vals = self(x_vals)

        plt.plot(x_vals, y_vals)
        plt.title(f"{str(self)}, on {domain if domain is not None else self.domain}")
        plt.xlim(self.domain[0], self.domain[1])
        plt.axhline(linewidth=4, color='k')
        plt.axvline(linewidth=4, color='k')
        plt.grid(True)
        plt.show()
        return

    def derivative(self, n: int = 1):
        if type(self.equation) is not np.polynomial.polynomial.Polynomial:
            return NotImplemented
        if type(n) is not int or n < 0:
            return TypeError("n must be a positive integer")
        else:
            return Function(equation=self.equation.deriv(n))
