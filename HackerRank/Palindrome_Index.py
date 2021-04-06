import math
import os
import random
import re
import sys

# Complete the palindromeIndex function below.
def palindromeIndex(s):
    d, t = 0, 0
    j = len(s) - 1
    i = 0
    if s ==s[::-1]:return -1
    while i < j:
        if s[i] != s[j]:
            if d : return t
            d = j
            t = i
        else: i+=1
        j -= 1
    return d

if __name__ == '__main__':
    fptr = sys.stdout

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()