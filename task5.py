# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 22:16:36 2022

@author: Семья
"""

# Даны даты заезда и отъезда каждого гостя. Для каждого гостя дата заезда строго раньше даты отъезда (то есть каждый гость останавливается хотя бы на одну ночь). В пределах одного дня считается, что сначала старые гости выезжают, а затем въезжают новые. Найти максимальное число постояльцев, которые одновременно проживали в гостинице (считаем, что измерение количества постояльцев происходит в конце дня).
#
# sample = [ (1, 2), (1, 3), (2, 4), (2, 3), ]

import collections

def get_maximal_number_of_guests(guests):
    guest_statistics = collections.defaultdict(int)
    for guest in guests:
        guest_statistics[guest[0]] += 1
        guest_statistics[guest[1]] -= 1
    # cumsum = []
    value = 0
    maxval = 0
    for key in guest_statistics.keys():
        value += guest_statistics[key]
        # cumsum.append(value)
        maxval = max(maxval, value)
    return(maxval)

