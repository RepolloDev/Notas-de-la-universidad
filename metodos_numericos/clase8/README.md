<h1 align='center'>🐫 Método Jacobi</h1>

El método Jacobi es un algoritmo iterativo
para resolver sistemas de ecuaciones lineales.
Este método se basa en realizar una serie
de pasos para encontrar la solución de un sistema
mediante la iteración de una matriz diagonal.

## 📝 ¿Cómo funciona?

Primero, debemos tener un sistema de ecuaciones lineales
expresadas en forma matricial:

$$
A \cdot x = b
$$

Entonces, realizamos una serie de comprobaciones
para asegurarnos que la matriz tiene una solución con
este método.

1. Verificamos que la matriz sea diagonalmente dominante.

$$
|a_{ii}| > \sum_{j=1, j \neq i}^{n} |a_{ij}|
$$

2. Reescribimos el sistema de ecuaciones en función
   de cada variable, según su elemento en la diagonal.

$$
x = M \cdot x + c
$$

3. Damos con los elementos alfas de la matriz para
   saber si el sistema converge, esto con la condición
   de que el máximo de los elementos alfas sea menor a 1.

## 🎯 Ejemplo

Supongamos que tenemos el siguiente sistema de ecuaciones:

$$
\begin{align*}
3x_1 - x_2 + x_3 &= 1 \\
3x_1 + 6x_2 + 2x_3 &= 0 \\
3x_1 + 3x_2 + 7x_3 &= 4
\end{align*}
$$

Para resolver este sistema, primero debemos
convertirlo en una matriz:

$$
\begin{bmatrix}
3 & -1 & 1 \\
3 & 6 & 2 \\
3 & 3 & 7
\end{bmatrix}

\times

\begin{bmatrix}
x_1 \\
x_2 \\
x_3
\end{bmatrix}

=

\begin{bmatrix}
1 \\
0 \\
4
\end{bmatrix}
$$

Ahora, con la matriz de coeficientes, podemos
ver si es diagonalmente dominante:

$$
\begin{bmatrix}
\color{red}{3} & -1 & 1 \\
3 & \color{red}{6} & 2 \\
3 & 3 & \color{red}{7}
\end{bmatrix}
$$

$$
\begin{align*}
|3| &> |-1| + |1|  \\
|6| &> |3| + |2| \\
|7| &> |3| + |3|
\end{align*}
$$

De aquí podemos ver que todos los elementos de la
diagonal son mayores a la suma de los elementos de
la fila, por lo que la matriz es diagonalmente dominante.

Ahora, reescribimos el sistema de ecuaciones en función
de cada variable, despejando cada una de ellas:

$$
\begin{align*}
x_1 &= \frac{1}{3} + \frac{1}{3}x_2 - \frac{1}{3}x_3 \\
x_2 &= 0 -\frac{1}{6}x_1 - \frac{1}{3}x_3 \\
x_3 &= \frac{4}{7} - \frac{3}{7}x_1 - \frac{3}{7}x_2
\end{align*}
$$

Ahora reescribmos el sistema en función de la matriz
de coeficientes:

$$
\begin{bmatrix}
x_1 \\
x_2 \\
x_3
\end{bmatrix}

=

\begin{bmatrix}
0 & \frac{1}{3} & -\frac{1}{3} \\
-\frac{1}{6} & 0 & -\frac{1}{3} \\
-\frac{3}{7} & -\frac{3}{7} & 0
\end{bmatrix}

\times

\begin{bmatrix}
x_1 \\
x_2 \\
x_3
\end{bmatrix}

+

\begin{bmatrix}
\frac{1}{3} \\
0 \\
\frac{4}{7}
\end{bmatrix}
$$

Ahora, sacamos los elementos alfas de la matriz $M$:

$$
\begin{align*}
\alpha_1 &= \left|\frac{1}{3}\right| - \left|-\frac{1}{3}\right| = \frac{2}{3} \\
\alpha_2 &= \left|-\frac{1}{6}\right| - \left|-\frac{1}{3}\right| = \frac{1}{6} \\
\alpha_3 &= \left|-\frac{3}{7}\right| - \left|-\frac{3}{7}\right| = \frac{3}{7}
\end{align*}
$$

Dado que todos los elementos alfas son menores a 1,
podemos asegurar que el sistema converge.

### 📦 Iteraciones

Para encontrar la solución del sistema, debemos
realizar una serie de iteraciones hasta que
la solución converja.

1. Inicializamos los valores de $x_1$, $x_2$ y $x_3$,
para este caso estos valores pueden ser 0.

2. Sustituimos los valores en el sistema $x = M \cdot x + c$

3. Repetimos el paso 2 hasta que la solución converja.

