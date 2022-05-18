#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    maxcount = 0
    mincount= 0
    maximo =scores[0]
    minimo = scores[0]
    for i in scores:
        if i > maximo:
            maximo = i
            maxcount+=1
        if i < minimo:
            minimo = i
            mincount+=1

    return maxcount,mincount
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
