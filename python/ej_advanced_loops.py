# -*- coding: utf-8 -*-
"""
Ejemplos de cómo construir nuestros porpios for loops.


Created on Sun Mar 17 22:13:01 2019

@author: TebaPC
"""

def iter_islast(iterable):
    """ iter_islast(iterable) -> generates (item, islast) pairs

    Generates pairs where the first element is an item from the iterable
    source and the second element is a boolean flag indicating if it is the
    last item in the sequence.
    
    http://code.activestate.com/recipes/392015-finding-the-last-item-in-a-loop/
    """
    it = iter(iterable) # nos aseguramos de que sea un iterable
    prev = it.__next__()
    # Entramos en el bucle. Cuando el iterador llega al final, sale del bucle
    for item in it:
        yield prev, False
        prev = item
    # Y entonces ya tenemos el ultimo elemento, lo devolvemos    
    yield prev, True


def funky_for_loop(iterable, action_to_do):
    """  for loop convertido a while loop.
    https://opensource.com/article/18/3/loop-better-deeper-look-iteration-python
    """
    iterator = iter(iterable)
    done_looping = False
    while not done_looping:
        try:
            item = next(iterator)
        except StopIteration:
            done_looping = True
        else:
            yield action_to_do(item)

def squared(x):
    """ Devuelve el cuadrado de un numero"""
    return x*x

# =============================================================================
# MAIN
# =============================================================================
""" Veamos algunos ejemplos """
ls_numbers = [1,2,3,4]
print(ls_numbers)

""" Ejemplo de uso de la func map"""
gen_map = map( squared, ls_numbers)
ls_squared_1 = list(gen_map) 
print(ls_squared_1)

""" Ejemplo de uso de la func funky_for_loop"""
gen_loop_result = funky_for_loop(ls_numbers, squared) # esto es un generador 
ls_squared_2 = list(gen_loop_result)
print(ls_squared_2)

""" Ejemplo de iter_islast """
for n, islast in iter_islast(range(4)):
    if islast:
        print("And last but not least:", n)
    else: print(n)
    
