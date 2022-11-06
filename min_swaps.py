#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    s=0
    while(arr!=sorted(arr)):
        for i in range(len(arr)):
            if(i+1 != arr[i]):
                j=arr[i]
                arr[j-1],arr[i]=arr[i],arr[j-1]
                s+=1
    return(s)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
