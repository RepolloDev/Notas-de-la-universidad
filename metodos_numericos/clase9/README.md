<h1 align='center'>Método Gauss-Siedel</h1>

El método _Gauss-Seidel_ es método iterativo para
resolver sistemas de ecuaciones lineales. Este método
es una variante del método de _Jacobi_.

> El creador de este método fue asistente del
> creador del método de _Jacobi_, por lo que
> se ve la similitud entre ambos métodos.

> [!NOTE]
> Este método es mucho más rápido que el
> método de _Jacobi_ ya que converge más rápido.

## 🧐 Funcionamiento ☝️

Este método es literalmente muy similar a
lo realizado con el [método Jacobi](../clase8/README.md),
pero con una pequeña diferencia.

- Se despeja la variable de la diagonal
- Se sustituyen los valores de las variables
  ya calculadas en la ecuación, (**los últimos valores**)

## 🎯 Ejemplo

Si tenemos el siguiente sistema de ecuaciones $A \cdot x = B$

$$
\left[
\begin{align*}
3 & -0.1 & -0.2 \\
0.1 & 7 & -0.3 \\
0.3 & -0.2 & 10
\end{align*}
\right]

\times

\left[
\begin{align*}
x_1 \\
x_2 \\
x_3
\end{align*}
\right]

=

\left[
\begin{align*}
7.85 \\
-19.3 \\
71.4
\end{align*}
\right]
$$

Despejamos las variables de la diagonal
y generamos el sistema $x = M \cdot x + c$

$$
M = \left[
\begin{align*}
0 && 0.0333 && 0.0667 \\
0.0143 && 0 && 0.0429 \\
0.03 && 0.02 && 0
\end{align*}
\right]

+ c = \left[
\begin{align*}
0.2617 \\
2.7571 \\
7.14
\end{align*}
\right]
$$

Ahora es iterar remplazando los valores
de las variables por las últimas variables
calculadas en vez de los valores
de la última iteración.
