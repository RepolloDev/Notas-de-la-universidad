<h1 align='center'>Propagación de errores</h1>

Si se tiene una función $y=f(x_1, x_2, ..., x_n)$ donde cada
cada variable es un valor _aproximado_ $x_i$ con su
respectivo error $\Delta x_i$.

Si obtenemos un valor para $y$ es claro que también
tendremos un error asociado $\Delta y$. Este error
se puede calcular a partir de los errores de las
variable independientes.

$$
\Delta y = \left|\frac{\partial y}{\partial x_1}\Delta x_1\right| + \left|\frac{\partial y}{\partial x_2}\Delta x_2\right| + ... + \left|\frac{\partial y}{\partial x_n}\Delta x_n\right|
$$

> Dar con las derivadas parciales de la función $y=f(x_1, x_2, ..., x_n)$

### 🎯 Ejemplo

![image](./assets/capture_one.png)

$$
H = A \cdot e \cdot \sigma \cdot T^4
$$

Considerando los datos como:

- A = 0.15 $\pm$ 0.1
- e = 0.9 $\pm$ 0.01
- $\sigma = 5.67 \times 10^{-8}$
- T = 650 $\pm$ 40

$$
\Delta H = \left|\frac{\partial H}{\partial A}\Delta A\right| + \left|\frac{\partial H}{\partial e}\Delta e\right|  \left|\frac{\partial H}{\partial T}\Delta T\right|
$$

$$
\Delta H = \left|e \cdot \sigma \cdot T^4 \Delta A\right| + \left|A \cdot \sigma \cdot T^4 \Delta e\right| + \left|A \cdot e \cdot \sigma \cdot 4T^3 \Delta T\right|
$$

Con esos datos y sabiendo que $H = 1366.376091$ simplemente remplazando los valores, obtenemos el error.

$$
\Delta H = 274.443061
$$