# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 20:59:32 2022

@author: Семья
"""

# Дана строка (возможно, пустая), состоящая из букв A-Z: AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию RLE, которая на выходе даст строку вида: A4B3C2XYZD4E3F3A6B28
# И сгенерирует ошибку, если на вход пришла невалидная строка.
# Пояснения: Если символ встречается 1 раз, он остается без изменений; Если символ повторяется более 1 раза, к нему добавляется количество повторений.

line = "AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB"

def compress_line(line):
    characterCur = line[0]
    quantity = 0
    resLine = ""
    for character in line:
        if character == characterCur:
            quantity += 1
        else:
            if (quantity>1):
                resLine += characterCur + str(quantity)
            else:
                resLine += characterCur
            quantity = 1
            characterCur = character
    resLine += characterCur + str(quantity)
    return(resLine)
