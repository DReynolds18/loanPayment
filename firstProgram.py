# -*- coding: utf-8 -*-
"""

Dylan Reynolds
CIS 177
First Assignment: find sum of first 100 integers
15 August 2022


"""

import numpy as np
list100 = np.linspace(1, 100, 100, dtype=int)
sum100 = sum(list100)
print('sum of first 100 integers is: {}'.format(sum100))

otherSum=0
for i in range(101):
    otherSum+= i
    
print('otherSum = {}',format(otherSum))