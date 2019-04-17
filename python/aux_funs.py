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


# CLASS DEFINITION

class Bool_Col():
    def __init__(self, bool_notation):
        """ tuple or list as boolean info
        :example: (1,0,0,1)
        """
        self.bool_info = bool_notation

    @property
    def bool_to_group(self):
        """ Given bool_notation (1,0,0,1,1) --> [1,2]

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

    @property
    def space(self):
        return len(self.bool_info)


class Group_Col():
    """The Group_Col class,
    #todo: change class name"""

    def __init__(self, group):
        """ :param: tuple or list, k elements of size i
        :example: (2,3,1) or [2,3,1] """
        self.group = group

    @property
    def min_space(self):
        """ Calculates de min space needed for a given group
        :param: list , group notation
        :rtype: integer

        :example:
        Let be [2,3,1] --> 2 + space + 3 + space + 1 == 8
        >>> space_needs([2,3,1])
        >>> 8
        """
        return np.sum(self.group) + len(self.group) - 1

    @property
    def min_bool(self):
        """For a group (gi,...,gk), generates the  minimum possibility in bool notation
           :arg: list or tuple
           :return: array """
        ar_min_bol = np.hstack([1] * g + [0] for g in self.group)[:-1]
        return ar_min_bol


# FUNCTIONS DEFINITION

def gen_shift(group, s):
    """For a group (gi,...,gk) and a given space s, generates de shift of the group
    :example:
    >>> group, space = (3,1,2), 10
    >>> [ [1,1,1,0,1,0,1,1,0,0],
    >>>   [0,1,1,1,0,1,0,1,1,0],
    >>>   [0,0,1,1,1,0,1,0,1,1] ]"""

    mygroup = Group_Col(group)
    mybool = Group_Col.min_bool
    min_space = len(mybool)
    if s < min_space:

        return group
    else:
        first = np.concatenate((mybool, np.zeros(s - min_space)))
        solution = [first]
        sol = first
        for _ in range(s- min_space):
            sol = np.roll(sol, 1)
            solution = solution + [sol]
        return np.vstack(solution)


def get_invariables(group, s):
    """ Calculates the invariables for a group on a space s

    :param n: int
    :param s: integer
    """
    ar_possibles = gen_shift(group, s)
    return np.all(ar_possibles, axis=0)
