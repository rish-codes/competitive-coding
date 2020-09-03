#Staircase problem from HackerRank - https://www.hackerrank.com/challenges/staircase/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for i in range (n-1, 0, -1):
        print(' '*i, end='')
        k = n-i
        print('#'*k)
    print('#'*n)


if __name__ == '__main__':
    n = int(input())

    staircase(n)
