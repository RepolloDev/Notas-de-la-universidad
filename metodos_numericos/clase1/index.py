# CONDICIONES DE CONVERGENCIA
# Un método es convergente cuando encuentro la solución exacta

# ? Para este método tenemos que x === P, porque es el caso más común
# ! En caso de que x != P y sea un valor arbitrario, entonces tomara más iteraciones hasta encontrar el resultado
# * En simples palabras, el valor de x es el que define la convergencia del método y la velocidad de convergencia, (lenta o rápida) y así el método SIRVE PARA CUALQUIER CASO, pero puede ser lento para ciertos casos


# Modelo matemático
def x_i_more_1(x_i, P):
    return x_i * (pow(x_i, 3) + 2 * P) / (2 * pow(x_i, 3) + P)


# Error aproximado
def E(x_i, x_i1):
    return abs((x_i1 - x_i) / x_i)


P = float(input("Ingrese un número: "))  # Valor actual
x1 = P  # Primer valor
x2 = x_i_more_1(x1, P)  # Segundo valor basado en el primero
E1 = E(x1, x2)  # Error aproximado de la primera iteración
tolerance = 0.00001  # Tolerancia o calidad de datos
n = 1

current_error = E1  # Error actual
x_i = x2  # Valor actual
n += 1

while current_error > tolerance:
    x_i1 = x_i_more_1(x_i, P)
    current_error = E(x_i, x_i1)
    x_i = x_i1
    n += 1

print(f"Valor obtenido {x_i}")
print(f"Error actual {current_error}")
print(f"Número de iteraciones {n}")
