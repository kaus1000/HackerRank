#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    positive = []
    negative = []
    zeros = []
    for i in arr:
        if i > 0: 
            positive.append(i)
            r1=len(positive)/n
            
        elif i < 0:
            negative.append(i)
            r2=len(negative)/n
        elif i ==0:
            zeros.append(i)
            r3=len(zeros)/n
    try:
        print(r1)
    except:
        r1=0
        print(r1)
    try:
        print(r2)
    except:
        r2=0
        print(r2)
    try:
        print(r3)
    except:
        r3=0
        print(r3)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
