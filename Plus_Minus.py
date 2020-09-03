Plus Minus problem in HackerRank - https://www.hackerrank.com/challenges/plus-minus/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    positive_count = 0
    negative_count = 0
    zero_count = 0
    n = len(arr)
    for i in arr:
        if i > 0:
            positive_count += 1
        elif i < 0:
            negative_count += 1
        else:
            zero_count += 1
    print("{:.6f}".format(positive_count/n, 6))
    print("{:.6f}".format(negative_count/n, 6))
    print("{:.6f}".format(zero_count/n, 6))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
