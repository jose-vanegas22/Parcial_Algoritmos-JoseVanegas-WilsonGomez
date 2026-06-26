#!/bin/python3


import math
import os
import random
import re
import sys


#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#


def maximumPerimeterTriangle(sticks):
    sticks.sort()                                        
   
    best = None                                          
   
    for i in range(len(sticks) - 1, 1, -1):              
        a = sticks[i-2]                              
        b = sticks[i-1]                              
        c = sticks[i]                                
       
        if a + b > c:
            best = [a, b, c]                        
            break
   
    if best is None:
        return [-1]                                       
    return best


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')


    n = int(input().strip())


    sticks = list(map(int, input().rstrip().split()))
    result = maximumPerimeterTriangle(sticks)


    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')


    fptr.close()
