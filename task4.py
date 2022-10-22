# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 21:29:45 2022

@author: Семья
"""

# Дан массив из нулей и единиц. Нужно определить, какой максимальный по длине подинтервал единиц можно получить, удалив ровно один элемент массива.
# [1, 1, 0]

def get_max_subinterval_size_for_perturbed_array(arr):
    maxSize = 0
    for i in range(len(arr)):
        if i == 0:
            arrTemp = arr[1:]
        elif i == len(arr)-1:
            arrTemp = arr[:(len(arr)-1)]
        else:
            arrTemp = arr[0:i].copy()
            arrTemp.extend(arr[i+1:len(arr)])
        curSize = get_max_subininterval_size(arrTemp)
        maxSize = max(maxSize, curSize)
    return(maxSize)


def get_max_subininterval_size(arr):
    maxSize = 0
    curSize = 0
    for elem in arr:
        if (elem == 1):
            curSize += 1
        else:
            maxSize = max(maxSize, curSize)
            curSize = 0
    maxSize = max(maxSize, curSize)
    return(maxSize)