import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    s = arr[-1]
    arr = arr[:-1]
    print(arr, s)
    for i in range(n-2,-1,-1):
        print(i)
        if arr[i]>s:
            print('tadam!')
            print(' '.join(map(str,(arr[:i+1]+[arr[i]]+arr[i+1:]))))
        else: 
            arr = arr[:i+1] + [s] + arr[i+1:]
            print(' '.join(map(str,arr)))
            break
    else:
        print(s, ' '.join(map(str,arr)))

    pass

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)