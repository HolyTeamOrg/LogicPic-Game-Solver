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

class Permu():
    def __init__(self, bool_info):
        """ tuple or list as boolean info
        :example: (1,0,0,1)
        """
        self.bool_info = bool_info

    def translate_per(self):
        """ Given bool notation (1,0,0,1,1) --> [1,2]

          :type permu: list or tuple of integers
          :param permu: the permutation in boolean notation
          :return: list

          :example:
          >>> translate_per([0, 0, 1, 1, 0, 1, 0, 1, 1, 1])
          >>> [2,1,3]
          """
        cnt = 0
        ls = []
        for i in self.bool_info:
            if i:
                cnt = cnt + 1
            else:
                ls.append(cnt)
                cnt = 0
        ls.append(cnt)
        return list(filter((0).__ne__, ls))

# FUNCTIONS DEFINITION
def translate_per(permu):
    """ Given bool notation (1,0,0,1,1) --> [1,2]

      :type permu: list or tuple of integers
      :param permu: the permutation in boolean notation
      :return: list

      :example:
      >>> translate_per([0, 0, 1, 1, 0, 1, 0, 1, 1, 1])
      >>> [2,1,3]
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

def gen_elem_per(n, s):
    """ Calculates the permutations for a element of size 'n' in a space of length space 's'

    :param: n
    :param: s
    :return: lst
    """
    rang = list(np.ones(n, dtype=bool)) + list(np.zeros(s - n, dtype=bool))
    ls_permu_bad = list(permutations(rang))
    # ls_permu_bad return permutations that not contains element of size n. Lets filter them, translating it to
    # group notation
    ls_permu = [i for i in ls_permu_bad if len(translate_per(i)) == 1]
    df = pd.DataFrame(ls_permu).drop_duplicates()
    #todo: it generates equivalent permutations
    return df

def space_needs(group):
    """ Calculates de min space needed for a given group
    :param: list , group notation
    :rtype: integer

    :example:
    Let be [2,3,1] --> 2 + space + 3 + space + 1 == 8
    """
    return np.sum(group) + len(group) - 1

def gen_group_per(group):
    """ Given a group of k elements (ei,..., ek), generate possible permutations"""
    for e in group:
        ls_ele = gen_elem_per(e, e+1)
        #todo: ni idea de como generarlo

def get_invariables(n, s):
    """ Calculates the invariables for a elem(n) and space(s)

    :param n: int
    :param s: integer
    """
    # ToDo: lets generate the obvious values in a possible group permutation

    df_permu = gen_elem_per(n,s)
    sr_inv = df_permu.all(axis = 0)
    return sr_inv

def main():
    """
    Given a row/col of length l, the number of possible combinations of 0 and 1,
    is a combination with replacement.
    >>> list(combinations_with_replacement([0, 1], 3))
    >>> [(0, 0, 0),
    >>>  (0, 0, 1),
    >>>  (0, 1, 1),
    >>>  (1, 1, 1)]
    
    Remark here that the order doesn't matter, so the combination (1,0,1) is not shown,
    thus is equivalent as (0,1,1)

    What we need is the list of all permutations.
    Example, given row/col like (0,0,1)
    >>> list( permutations([0, 0, 1]) )
    >>> [(0, 0, 1),
    >>>  (0, 1, 0),
    >>>  (0, 0, 1),
    >>>  (0, 1, 0),
    >>>  (1, 0, 0),
    >>>  (1, 0, 0)]
    
    These are the permutations for an element of size 1 in a space of size 3.
    
    So, if we have a element(2) in space(3)
    >>> list(permutations([0, 1, 1]))

    We use map function to pass the generator to translate_per
    >>> n, s = 2, 4
    >>> ls_permu = gen_elem_per(n, s)

    We can inspect this list of list better if we pass it into pandas
    >>> df_permu = pd.DataFrame(ls_permu).astype(int)
    >>> ar_permu = np.array(ls_permu)

    Let be a group with k element of size n
    *group notation: (n_i, ..., n_k)
    Thus, gen_per(n,s)

    todo : call gen_permutations with group like (2,3,1)
    

    Vamos a calcular la long minima que puede tener un grupo dado

    Dado un grupo de n_elementos >1, llamamos recursivamente a gen_per hasta 
    que el gr_long_min sea mayor o igual que las celdas vacias.


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
    get_invariables(3,5)
    print('end')

if __name__ == '__main__':
    main()

