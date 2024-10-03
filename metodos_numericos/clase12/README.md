<h1 align='center'>🏁 Interpolación</h1>

La interpolación es un método para poder definir
una función general conociendo ciertos valores.
Muy similar a lo que sucede con la regresión lineal.

> [!NOTE]
> La interpolcación requiere de dos conjuntos de valores
> relacionados (x, y) con los que se genera una función

| Variable X | Variable Y |
| ---------- | ---------- |
| 1          | 1          |
| 2          | 3          |
| ...        | ...        |

## 🧪 Método de Lagrange

El método de Lagrange es una forma para generar
una función que interpola a cualquier valor generando
un polinomio a base de Lagrange.

$$
L_i(x) = \prod_{j\neq i} \frac{x - x_j}{x_i - x_j}
$$

Hay que sacar una función de Lagrange por cada valor
$x$ que tengamos en nuestra tabla, luego utilizamos
un polinomio.

$$
P(x) = \sum_{i=0}^{n} L_i(x) \cdot y_i
$$

Esto quiere decir que multiplicamos la función de
Lagrange del $x_i$ por su valor correspondiente
$y_i$, esta sumatoria nos daría un valor
interpolado a un $x_k$.

> [!TIP]
> Este método al ser tan largo y complejo, generalmente
> se toma un valor $x_k$ y se realiza la interpolación
> únicamente con los valores cercanos al que queremos
> obtener.

<h3 align='center'>🎯 Ejemplo</h3>
<p align='center'>
    <a href='./assets/index.xlsx'>
        <img alt='Excel Badge' src='https://img.shields.io/badge/Documento Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white'/>
    </a>
</p>

## 📦 Mathlab u Octave

Para poder realizar una interpolación para cierto
valor $x_k$ con _Mathlab_ u _Octave_ simplemente
debemos hacer lo siguiente:

```octave
% Definir los valores
x = [1,2,3,4,5,6,7];
y = [3,4,5,6,7,8,9];

% Definir la variable a calcular
xk = 3.3;

% Generar la interpolación
yk = interp1(x, y, xk)

% Interpolar un conjunto de valores
xk_2 = 1:0.1:7
yk_2 = interp1(x, y, xk_2)

% Graficar la función
plot(x, y)
```

De esta manera ya tenemos listo la función para cualquier valor, siendo que lo único que debemos cambiar es el valor de $x_k$ para obtener su respectivo $y_k$

> [!TIP]
> La función `interp1` nos permite realizar una
> interpolación, la misma necesita de tres parámetros
> los valores $x$ y $y$, donde $x_k$ puede ser uno
> o varios valores.
