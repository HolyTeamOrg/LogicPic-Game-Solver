# -*- coding: utf-8 -*-
"""

Archivo de pruebas

Created on Tue Apr 17 2019

@author: Tebinski
"""

import aux_funs


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
    get_invariables(3, 5)
    print('end')


if __name__ == '__main__':
    print('todo ok')

    # This is nice. Now we can define our data as boolean, and transform into a group
    myBoolCol = aux_funs.Bool_Col([1, 0, 0, 1])
    mygroup2 = myBoolCol.bool_to_group()

    # And viceversa #todo
    myGroup = aux_funs.Group_Col([2, 3])
    my_invariables = myGroup.get_invariables(7)

    print('fin')
