# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 22:49:53 2022

@author: Семья
"""

# Даны две строки.
#
# Написать функцию, которая вернёт True, если из первой строки можно получить вторую, совершив не более 1 изменения (== удаление / замена символа).

def check_that_strings_are_almost_equal(str1, str2):
    if (len(str1) == len(str2)):
        numberOfChanges = 0
        for i in range(len(str1)):
            if (str1[i] != str2[i]):
                numberOfChanges += 1
                if numberOfChanges > 1:
                    return(False)
        return(True)
    else:
        if (abs(len(str2) - len(str1)) > 1):
            return(False)
        if (len(str2)>len(str1)):
            greater = str2
            less = str1
        else:
            greater = str1
            less = str2
        if greater[1:] == less:
            return(True)
        if greater[0:len(less)] == less:
            return(True)
        return(False)
