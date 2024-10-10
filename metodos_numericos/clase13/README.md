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
para un $x=6$, entonces el polinomio de Newton
sería:

$$
P(x) = a_0 + a_1(x - x_0) + a_2(x - x_0)(x - x_1) + a_3(x - x_0)(x - x_1)(x - x_2)
$$

Donde los coeficientes $a_i$ son las diferencias
divididas de orden $i$, solo se puso así por
estética.

Calculando las diferencias divididas:

| 1er nivel   | 2do nivel    | 3er nivel   |
| ----------- | ------------ | ----------- |
| 1.4         | -0.138888889 | 0.034444444 |
| 0.566666667 | 0.136666667  | ---         |
| 1.25        | ---          | ---         |

> [!TIP]
> Notar que a medida que se sube de nivel, se
> va calculando la diferencia dividida de orden
> superior, tenemos menos datos para calcular

Entonces remplazando los datos en el polinomio
para $P(x=6)$

$$
\begin{align*}
P(6) &= 4.5 + 1.4(6 - 2) - 0.138888889(6 - 2)(6 - 5) + 0.034444444(6 - 2)(6 - 5)(6 - 8) \\
& = 9.268888889
\end{align*}
$$

> [!NOTE]
> Para el caso se utilizan los valores de la primera fila
> esto se denomina como _diferencias divididas hacia adelante_.
