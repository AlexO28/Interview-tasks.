# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 22:59:55 2022

@author: Семья
"""

# Дан список интов и число-цель. Нужно найти такой range, чтобы сумма его элементов давала число-цель.

# elements = [1, -3, 4, 5]

# target = 9

# result = range(2, 4) # because elements[2] + elements[3] == target


def find_suitable_range(elements, goal):
    cumsum = []
    value = 0
    cumsum.append(0)
    for i in range(len(elements)):
        value += elements[i]
        cumsum.append(value)
    for i in range(len(elements)):
        for j in range(i, len(elements)+1):
           if check_range(cumsum, i, j, goal):
              return([i, j])
    return None


def check_range(cumsum, i, j, goal):
    return(cumsum[j] - cumsum[i] == goal)
