# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 11:14:55 2022

@author: Семья
"""

# Слияние отрезков:
#
# Вход: [1, 3] [100, 200] [2, 4]
# Выход: [1, 4] [100, 200]

def merge_intervals(intervals):
    resIntervals = []
    for interval in intervals:
        if len(resIntervals) == 0:
            resIntervals.append(interval)
        else:
            newIntervals = []
            intervalStart = interval[0]
            intervalEnd = interval[1]
            added = False
            for chosenInterval in resIntervals:
                if (chosenInterval[1] < interval[0]):
                    newIntervals.append(chosenInterval)
                elif (chosenInterval[0] > interval[1]):
                    if (not added):
                        newIntervals.append([intervalStart, intervalEnd])
                        added = True
                    else:
                        newIntervals.append(chosenInterval)
                else:
                    if not added:
                        intervalStart = min(intervalStart, chosenInterval[0])
                        intervalEnd = max(intervalEnd, chosenInterval[1])
                if added:
                    newIntervals.append(chosenInterval)
            if not added:
                newIntervals.append([intervalStart, intervalEnd])
            resIntervals = newIntervals
    return(resIntervals)