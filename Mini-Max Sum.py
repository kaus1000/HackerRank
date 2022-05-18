#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    r = 0
    lista=arr
    resultado=0
    k=0
    for i in range(0,4):
        try:
            arr.sort()
            k=arr[i]+k
        except:
            pass
    for i in range (0,4):
        r=max(lista)
        resultado=r+resultado
        lista.remove(max(lista))
    print(k,resultado)
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
