# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 20:22:34 2022

@author: Семья
"""

# Даны два массива: [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2]
# Надо вернуть [1, 2, 2, 3] (порядок неважен)

import numpy

arr1 = [1, 2, 3, 2, 0]
arr2 = [5, 1, 2, 7, 3, 2]

def get_common_elements(arr1, arr2):
    arr = []
    radixSort(arr1)
    radixSort(arr2)
    i = 0
    j = 0
    while ((i < len(arr1)) & (j < len(arr2))):
        signCur = numpy.sign(arr1[i] - arr2[j])
        if (signCur == 0):
            arr.append(arr1[i])
            i = i + 1
            j = j + 1
        elif (signCur > 0):
            j = j + 1
        else:
            i = i + 1
    return(arr)


def countingSort(arr, exp1):   
    n = len(arr)   
    output = [0] * (n)
    count = [0] * (10)
   
    for i in range(0, n):
        index = (arr[i]/exp1)
        count[int((index)%10)] += 1
   
    for i in range(1, 10):
        count[i] += count[i-1]
   
    i = n-1
    while i>=0:
        index = (arr[i]/exp1)
        output[count[int((index)%10)] - 1] = arr[i]
        count[int((index)%10)] -= 1
        i -= 1
   
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]
 

def radixSort(arr): 
    max1 = max(arr) 
    exp = 1
    while max1/exp > 0:
        countingSort(arr, exp)
        exp *= 10
