# -*- coding: utf-8 -*-
"""

Test, from py create ipynt. TODO: not working

Created on Sun Mar 17 22:30:36 2019

@author: TebaPC
"""

import nbformat.current as nbf
nb = nbf.read(open('ej_advanced_loops.py', 'r'), 'py')
nbf.write(nb, open('test.ipynb', 'w'), 'ipynb')