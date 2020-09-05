# Solution to Equalize the Array problem from Hackerrank - https://www.hackerrank.com/challenges/equality-in-a-array/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(n, arr):
    return (n - max([arr.count(i) for i in set(arr)]))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
