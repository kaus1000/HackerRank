#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    result = []
    result2 = []
    d1 =0 
    d2 = 0
    k = 0
    o = 0
    for x in arr:
        if k <= len(x):
            result.append(x[k])
            k+=1
            continue
    for x in arr:
        if o <= len(x):
            i = len(x) -1
            result2.append(x[i-o])
            o+=1
            continue
    for i in result:
        d1 +=i
    for i in result2:
        d2 +=i
    dresult= d1 - d2
    return abs(dresult)
    
            
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
