# -*- coding: utf-8 -*-
"""

Antes que nada lo que necesito es obtener todaslas posibles combinaciones en 
una fila|columna de longitud l, dado una tupla (i1, i2, ...,, i_k) 
donde i es la longitud/tamaño del grupo, y k el numero de grupos.   

reated on Sun Mar 17 04:17:17 2019

@author: Tebinski
"""

from itertools import combinations_with_replacement, permutations
import numpy as np
import pandas as pd

class Permu():
    def __init__(self):
        self.bool_info = []

    def def_bool(self, bool_info):
        """ tuple or list as boolean info
        :example: (1,0,0,1)
        """
        self.bool_info = bool_info

    @property
    def group(self):
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


def trad_min_bool(group):
    """For a group (gi,...,gk), generates the trad to bool notation
    :arg: list or tuple
    :return: array """
    return np.hstack( [1]*g + [0] for g in group )[:-1]

def gen_shift(group, s):
    """For a group (gi,...,gk) and a given space s, generates de shift of the group
    :example:
    >>> group = (3,1,2)
    >>> """

    mybool = trad_min_bool(group)
    min_space = len(mybool)
    if s < min_space:
        return group
    else:
        first = np.concatenate( (mybool, np.zeros(s - min_space) ) )
        solution = [first]
        sol = first
        while sol[-1] != 1:
            sol = np.roll(sol,1)
            solution = solution + [sol]
        return np.vstack(solution)

def space_needs(group):
    """ Calculates de min space needed for a given group
    :param: list , group notation
    :rtype: integer

    :example:
    Let be [2,3,1] --> 2 + space + 3 + space + 1 == 8
    >>> space_needs([2,3,1])
    >>> 8
    """
    return np.sum(group) + len(group) - 1

def get_invariables(group, s):
    """ Calculates the invariables for a group on a space s

    :param n: int
    :param s: integer
    """
    ar_possibles = gen_shift(group, s)
    return np.all(ar_possibles, axis= 0)

