from math import exp, factorial


# Función a aproximar
def f(x):
    return exp(2 * x)


# Derivada de orden n de la función
def df(x, order=1):
    return 2**order * exp(2 * x)


# Función generadora de aproximaciones con serie de Taylor
def aprox(x_0, x_1):
    iteration = 1
    distance = abs(x_1 - x_0)
    error = df(x_0) * distance
    value = f(x_0) + error
    yield iteration, value, error
    while True:
        iteration += 1
        error = (df(x_0, iteration) * pow(distance, iteration)) / factorial(iteration)
        value += error
        yield iteration, value, error


tolerance = 0.001
x_0 = 1
print(f"Se conoce el valor x_0 = {x_0} | f(x_0) = {f(x_0)}")
x_1 = float(input("Ingrese el valor de x_1: "))

# Iterar en el generador hasta que el error sea menor a la tolerancia
for iteration, value, error in aprox(x_0, x_1):
    if error < tolerance:
        break
    print(f"Iteración: {iteration}, Valor: {value:4f}, Error: {error:4f}")

print(f"Valor real de x_1 | {f(x_1)}")
