# -*- coding: utf-8 -*-
"""
Vamos a poner unso ejemplos de la funcion map, decoradores y advanced loops

Created on Sun Mar 17 22:02:28 2019

@author: TebaPC
"""

def squared(x):
    """ Devuelve el cuadrado de un numero"""
    return x*x

def mapper(fnc):
    """ https://youtu.be/PJQ5XopgNog """
    
    def inner(list_of_values):
#        it = iter(list_of_values)
        try: return [fnc(value) for value in list_of_values]
        except TypeError: # 'int' object is not iterable
            return fnc(list_of_values)
    
    return inner    
    
@mapper
def cubic(x):
    return x**3

ls_numbers = [1,2,3,4]
print( list(map( squared, ls_numbers)))

print(cubic(3)) # BUG Solved: int is not an iterable
print(cubic(ls_numbers))
