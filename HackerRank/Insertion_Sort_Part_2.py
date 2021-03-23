#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort2 function below.
def insertionSort2(n, arr):

    for i in range(1, n):
        temp = arr[i]
        for j in range(i,-1,-1):
            if j-1>=0 and temp < arr[j-1]:
                arr[j] = arr[j-1]
            else:
                arr[j] = temp
                break
        print(arr)
        


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
