#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#
def fizzBuzz(n):
    for x in range(1,n+1):
        if (x%3==0 and x%5==0):
            print('FizzBuzz')
        else:
            print(x)
           
n=int(input())
fizzBuzz(n)
