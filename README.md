# LogicPic-Game-Solver
Dado un puzzle del juego para moviles LogicPic, generar un solucionador

**El desafio consiste en que cada columna y fila, solo pueden estar coloreados ese numero de cuadrados. 

Ejemplos en tablero de 3x3: 

Filas donde solo existe existe 1 posibilidad :
(1,1):  101. 
(3)  :  111

Filas donde hay 2 posibilidades
(2) : En todos esa fila solo puede haber un grupo de 2 cuadrados seguidos coloreados.
  - 110
  - 011
  - *101* no es posible ya que sería (1,1). Los cuadrados deben estar juntos.
Filas donde hay 3 posibilidades
(1) : 
  - 001
  - 010
  - 100

idem para las columnas. 


<img src="./logicPic_example.png" width="500">

~~Para ver solucion ir al [jupyter notebook](./jupyter/SolTebinski.ipynb)~~