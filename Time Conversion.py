#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    if 'PM' in s:
        h=s[0:2]
        m=s[3:5]
        seg=s[6:8]
        uc= s[8:10]
        if int(h)<12:
            h=int(h)+12
    if 'AM' in s:
        h=s[0:2]
        m=s[3:5]
        seg=s[6:8]
        uc= s[8:10]
        if int(h)>=12:   
            h=int(h)-12
            if int(h) == 0:
                h= "00"
    
    result="{}:{}:{}".format(h,m,seg)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
