<h1 align='center'>Clase 4 - Aproximación de Taylor</h1>

> ![NOTE]
> La tarea de la clase se encuentra se describe en el archivo [](./tarea.md)

> _Brook Taylor_ fue un matemático ingles que realizo grandes aportes a las ramas del cálculo diferencial e integral, es más conocido por su **serie de Taylor**

La serie de Taylor es una herramienta poderoza para aproximar valores de una función $f$ que puede ser compleja **conociendo un valor cercano** en terminos del valor de la función y sus derivadas en otro punto.

$$
f(x_{i+1}) = f(x_i) + \frac{f`(x_i)}{1!}\times(x_{i+1}-x_i) + ... + \frac{f^n(x_i)}{n!} \times (x_{i+1}-x_i)^{n}
$$

## 🧠 Entendiendo la serie de Taylor

La serie de Taylor se maneja por _iteraciones_, siendo que entre más iteraciones hagamos, más elementos de la serie de Taylor utilizaremos.

### 📱 Valor aproximado

El resultado es la iteración $n$-ésima del resultado, haciendo uso de $n$ elementos de la serie de Taylos. Por ejemplo, si obtengo la primera iteración, tendré lo siguiente:

$$
f(x_{i+1}) = f(x_i) + f`(x_i)(x_{i+1} - x_i)
$$

> Entre más iteraciones (agregando más elementos de a la serie), entonces mejor será la aproximación al resultado real.

### ❌ Error del resultado

El error del valor aproximado es el último elemento de Taylor de la iteración, por ejemplo, si hago una sola iteración, entonces el error será:

$$
\epsilon = |f`(x_i)(x_{i+1} - x_i)|
$$

> El último elemento de la serie en valor absoluto será el error del valor aproximado.

### 📚 Vocabulario

-  _Truncar_: aproximar o cortar valores, convertir un proceso infinito en finito.

-  _Convergencia_: llegar a una solución mediante una función

-  _Criterio de parada_: condición para terminar de iterar, relacionado con la tolerancia

