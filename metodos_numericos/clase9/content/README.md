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

Utilizando el sistema de la [tarea anterior](../../clase7/content/README.md),
se resuelve el sistema de ecuaciones lineales utilizando
el método _Gauss-Seidel_.

$$
A = \begin{bmatrix}
    52 & 20 & 25 \\
    30 & 50 & 20 \\
    18 & 30 & 52
\end{bmatrix}

\quad

B = \begin{bmatrix}
    4800 \\
    5810 \\
    5690
\end{bmatrix}
$$

### Resultado en Excel

<p align="center">
    <img src="./assets/capture_1.png" width="800">
</p>

En la imagen, la solución va convergiendo a medida que se aumenta el número de iteraciones.

### Resultado en Python

<p align='center'>
    <img src='./assets/capture_2.png' width='800'>
</p>