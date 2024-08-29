import matplotlib.pyplot as plt
from math import sqrt, pi, e, factorial
from fractions import Fraction
import numpy as np


def factorial_aprox(n):
    return sqrt((2 * n + Fraction(1, 3)) * pi) * pow(n, n) * pow(e, -n)


def error(real, aprox):
    return abs(real - aprox) / real


values = np.arange(1, 100)
factorial_values = [factorial(n) for n in values]
aprox_values = [factorial_aprox(n) for n in values]
errors = [error(real, aprox) for real, aprox in zip(factorial_values, aprox_values)]

# Comparar los valores reales con los aproximados
plt.plot(values, aprox_values, label="Comparación")
plt.plot(values, factorial_values, label="Real")
plt.xlabel("n")
plt.ylabel("Valor")
plt.title("Comparación de valores reales y aproximados del factorial")
plt.legend()
plt.show()


# Graficar los errrores de la aproximación
plt.plot(values, errors)
plt.xlabel("n")
plt.ylabel("Error")
plt.title("Error de la aproximación de Stirling")
plt.show()
