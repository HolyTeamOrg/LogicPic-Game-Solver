# -*- coding: utf-8 -*-
"""

Antes que nada lo que necesito es obtener todaslas posibles combinaciones en 
una fila|columna de longitud l, dado una tupla (i1, i2, ...,, i_k) 
donde i es la longitud/tamaño del grupo, y k el numero de grupos.   

reated on Sun Mar 17 04:17:17 2019

@author: TebaPC
"""

from itertools import combinations_with_replacement, permutations


""" 
Dado una fil/col de longitud l, el numero de posibles combinaciones de
ceros y unos que puedo conseguir, es una combinacion con reemplazamiento, 
es decir, tengo los numeros 0 y 1, y permito que estos elementos se repitan
todas las veces que sea posibles para formar una combinacion de l elementos.

"""
list(combinations_with_replacement( [0,1], 3) )
"""
Out[]: [(0, 0, 0), 
        (0, 0, 1), 
        (0, 1, 1), 
        (1, 1, 1)]

PERO en las combinaciones el orden de los elementos no influye, por eso no 
nos aparece el (1,0,1).

"""

print(list(permutations( [0,0,1]) ))
"""
Out[]: [ (0, 0, 1),
         (0, 1, 0),
         (0, 0, 1),
         (0, 1, 0),
         (1, 0, 0),
         (1, 0, 0) ]

Este seria el ejemplo para calcular el grupo (1) en una f/c de l=3

el calculo para g(2) en f/c de l=3
"""
print(list(permutations( [0,1,1]) ))
"""
Out[]: [ (0, 1, 1),
         (0, 1, 1),
         (1, 0, 1),
         (1, 1, 0),
         (1, 0, 1), 
         (1, 1, 0)]

Aqui nos aparecen resultados que no corresponden a g(2), que son 
(1,0,1). 

¿Habra otra forma de generar las combinaciones que necesitamos, o necesitamos
generarlas todas y luego descartar?
"""






