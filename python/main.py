# -*- coding: utf-8 -*-
"""

Antes que nada lo que necesito es obtener todaslas posibles combinaciones en 
una fila|columna de longitud l, dado una tupla (i1, i2, ...,, i_k) 
donde i es la longitud/tamaño del grupo, y k el numero de grupos.   

reated on Sun Mar 17 04:17:17 2019

@author: TebaPC
"""

from itertools import combinations_with_replacement, permutations
import numpy as np
import pandas as pd
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
print(list(permutations( [0,0,1]) ))
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
print(list(permutations( [0,1,1]) ))
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

def gen_per( n, length ):
    """ Imprime en CommandWindow las permutaciones posibles dado un grupo de 
    longitud n, en una fil, col de long lengyh
    
    Devuelve el generador permutations"""
    
    rango = list(np.ones(n, dtype = bool)) + list(np.zeros(length-n, dtype = bool) )
#    for per in permutations( rango ):
#        print(list(per))
        
    return permutations( rango )
    
permu = gen_per(2, 4) 
ls_permu = list( permu ) # if you consume the generator, you can use it again... can you?
    
"""
Para poder descartar permutaciones, vamos a traducirlas a la notacion de 
grupos [True False True ] -> (1,1)
"""

def trad_per( permu ):
    cnt =  0
    ls = []
    for i in permu:
        if i:
            cnt = cnt + 1
        else:
            ls.append(cnt)
            cnt = 0
    ls.append(cnt)
             
    return list(filter((0).__ne__, ls))

grup = trad_per([0,0,1,1,0,1,0,1,1,1])
print(grup)
 
""" 
Utilizaremos la funcion map para poder pasar a esta funcion traductora 
todo el iterador permutations.
"""
permu = gen_per(2, 4) 
ls_grup = list(map(trad_per, permu))

# En el entorno de spyder, podemos verlo con más claridad de esta forma.
df = pd.DataFrame(ls_permu).astype(int)

""" TODO: llamar de forma recursiva a gen_per para poder darle como argumento 
varios grupos, tal que (2,3,1)
"""

""" Vamos a calular la long minima que puede tener un grupo dado """
def gr_long_min( grup ):
    """ calular la long minima que puede tener un grupo dado """
    return np.sum( grup ) + len( grup ) -1 

""" Dado un grupo de n_elementos >1, llamamos recursivamente a gen_per hasta 
que el gr_long_min sea mayor o igual que las celdas vacias. """

"""
grup = (4,1)
length = 6
 
def gen_multi_grup_permu( grup, lenght ): 
    
    if length > gr_long_min(grup):
        raise ValueError(' EL grupo no es compatible con la longitud' )
    else:
        for i in grup:
            while length > i + 1:
                # no tengo nada claro como montar este bucle
             
"""



