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


# FUNCTIOS DEFINITION
def gen_per(n, s):
    """
    Calculates the permutations for a element of size 'n' in a space of length space 's'

    :param: n
    :param: s
    :return: generator
    """
    rang = list(np.ones(n, dtype=bool)) + list(np.zeros(s - n, dtype=bool))
    return permutations(rang)


def trad_per(permu):
    """ Given bool notation (1,0,0,1,1) --> [1,2]

    :type permu: list or tuple of integers
    :param permu: the permutation in boolean notation
    :return: list
    """
    cnt = 0
    ls = []
    for i in permu:
        if i:
            cnt = cnt + 1
        else:
            ls.append(cnt)
            cnt = 0
    ls.append(cnt)

    return list(filter((0).__ne__, ls))


def gr_long_min(n):
    """ Calculates de min space needed for a element of size n
    :param: n , element size
    :rtype: integer
    """
    return np.sum(n) + len(n) - 1

# ToDo: lets generate the obvious values in a possible group permutation
def get_invariables(elem, space):
    """ Calculates the invariables in a given group and space

    :param elem: int
    :param space: integer
    """
    for i in elem:
        pass

def main():
    """
    Given a row/col of length l, the number of possible combinations of 0 and 1,
    is a combination with replacement.
    """
    list(combinations_with_replacement([0, 1], 3))
    """
    Out[]: [(0, 0, 0), 
            (0, 0, 1), 
            (0, 1, 1), 
            (1, 1, 1)]
    
    Remark here that the order doesn't matter, so the combination (1,0,1) is not shown,
    thus is equivalent as (0,1,1) 
    
    What we need is the list of all permutations.
    Example, given a element of size 1 with 3 spaces.
    
    """
    print(list(permutations([0, 0, 1])))
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
    print(list(permutations([0, 1, 1])))
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
    
    Let be a group with k element of size n 
    *group notation: (n_i, ..., n_k)
    
    Thus, gen_per(n,s)
    """
    permu = gen_per(2, 4)
    ls_permu = list(permu)  # if you consume the generator, you can use it again... can you?

    """
    Para poder descartar permutaciones, vamos a traducirlas a la notacion de 
    grupos [True False True ] -> (1,1)
    """

    group = trad_per([0, 0, 1, 1, 0, 1, 0, 1, 1, 1])
    print(group)

    """ 
    Utilizaremos la funcion map para poder pasar a esta funcion traductora 
    todo el iterador permutations.
    """
    i, s = 2, 4
    permu = gen_per(i, s)
    ls_permu = list(permu)
    ls_group = list(map(trad_per, ls_permu))
    ls_group_corrected = [group_k for group_k in ls_group if len(group_k) == 1]

    # We can inspect this list of list better if we pass it into pandas
    df_permu = pd.DataFrame(ls_permu).astype(int)

    """ TODO: llamar de forma recursiva a gen_per para poder darle como argumento 
    varios grupos, tal que (2,3,1)
    """

    """ Vamos a calular la long minima que puede tener un grupo dado """

    """ Dado un grupo de n_elementos >1, llamamos recursivamente a gen_per hasta 
    que el gr_long_min sea mayor o igual que las celdas vacias. """

    """
    group = (4,1)
    length = 6
     
    def gen_multi_grup_permu( group, lenght ): 
        
        if length > gr_long_min(group):
            raise ValueError(' EL grupo no es compatible con la longitud' )
        else:
            for i in group:
                while length > i + 1:
                    # no tengo nada claro como montar este bucle
                 
    """

if __name__ == '__main__':
    main()

