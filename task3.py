# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 21:18:35 2022

@author: Семья
"""

# Дан список интов, повторяющихся элементов в списке нет. Нужно преобразовать это множество в строку, сворачивая соседние по числовому ряду числа в диапазоны. Примеры:
# [1,4,5,2,3,9,8,11,0] => "0-5,8-9,11"
# [1,4,3,2] => "1-4"
# [1,4] => "1,4"

def transform_arr(arr):
    radixSort(arr)
    resLine = ""
    elemPrev = arr[0]
    minElem = arr[0]
    for elem in arr:
        if (elem - elemPrev > 1):
            if (elemPrev == minElem):
                resLine += str(minElem) + ','
            else:  
                resLine += str(minElem) + "-" + str(elemPrev) + ','
            minElem = elem
        elemPrev = elem
    if (elemPrev == minElem):
        resLine += str(minElem)
    else:  
        resLine += str(minElem) + "-" + str(elemPrev)
    return(resLine)


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
