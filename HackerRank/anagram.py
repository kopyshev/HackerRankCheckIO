#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the anagram function below.
def anagram(s):
    l = len(s)
    if l%2:return -1
    half = Counter(s[l//2:])
    exchange = 0
    for v,k in Counter(s[:l//2]).items():
        if k != half[v]: exchange+=max(0, k-half[v])
    return exchange
    
if __name__ == '__main__':
    fptr = sys.stdout

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()