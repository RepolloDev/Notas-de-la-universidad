# ERror de maquina
epsilon = 1.0
while 1.0 + epsilon != 1.0:
    epsilon /= 2
    print(epsilon)
epsilon *= 2  # Para obtener el último valor válido de epsilon
print(epsilon)
