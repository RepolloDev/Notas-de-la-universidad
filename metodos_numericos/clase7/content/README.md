<h1 align='center'>📒 Tarea</h1>

<p align='center'>
    <a href='../README.md'>
        <img alt='Markdown' src='https://img.shields.io/badge/Nota de clase-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white'/>
    </a>
    <a href='./index.xlsx'>
        <img alt='Excel' src='https://img.shields.io/badge/Documento Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white'/>
    </a>
    <a href='./index.py'>
        <img alt='Python' src='https://img.shields.io/badge/Código python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54'/>
    </a>
</p>

![alt text](./assets/capture_1.png)

Dando como resultado final lo siguiente:

- $40.11628 [m^3]$ para la cantera 1
- $71.62791 [m^3]$ para la cantera 2
- $51.25581 [m^3]$ para la cantera 3

## Programa en Python

```python
import numpy as np

A = [[52, 20, 25], [30, 50, 20], [18, 30, 55]]
B = [[4800], [5810], [5690]]

# invierte la matriz A
A_inv = np.linalg.inv(A)
# multiplica la matriz inversa por la matriz B
X = np.dot(A_inv, B)
# muestra el resultado
print(X)
```

![alt text](./assets/capture_2.png)