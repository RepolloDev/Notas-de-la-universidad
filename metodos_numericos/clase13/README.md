<h1 align='center'>🚀 Polinomio de Newton</h1>

Supongamos que tenemos una serie de valores
relacionados entre sí, y queremos encontrar una
función que pase por todos esos puntos.

| x   | y   |
| --- | --- |
| x1  | x2  |
| x2  | y2  |
| x3  | y3  |
| ... | ... |
| xn  | yn  |

El polinomio de Newton es una forma de interpolar
o hacer una aproximación de una función que pase
por todos esos puntos.

$$
P_n(x) = \sum_{i=0}^{n} f[x_0, x_1, ..., x_i] \prod_{j=0}^{i-1} (x - x_j)
$$

Donde $f[x_0, x_1, ..., x_i]$ es la diferencia dividida
de orden $i$, esta diferencia dividida representa
la aproximación de la derivada de orden $i$ de la función
que pasa por los puntos dados.

> [!TIP]
> Para una serie de datos pueden existir varios
> diferencias divididas por nivel.

## 🔍 Encontrando las diferencias divididas

El proceso para encontrar las diferencias divididas
es un proceso _recursivo_, pues para encontrar la
diferencia dividida de orden $i$ necesitamos de la
diferencia dividida de orden $i-1$.

$$
f[x_0, x_1, ..., x_i] = \frac{f[x_1, x_2, ..., x_i] - f[x_0, x_1, ..., x_{i-1}]}{x_i - x_0}
$$

## 📚 Ejemplo

Supongamos que tenemos los siguientes puntos:

| Nro. | x   | y    |
| ---- | --- | ---- |
| 0    | 2   | 4.5  |
| 1    | 5   | 8.7  |
| 2    | 8   | 10.4 |
| 3    | 10  | 12.9 |

Donde queremos encontrar un valor aproximado
para un $x=6$