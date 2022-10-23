# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 21:35:17 2022

@author: Семья
"""

# Дан массив точек с целочисленными координатами (x, y). Определить, существует ли вертикальная прямая, делящая точки на 2 симметричных относительно этой прямой множества. Note: Для удобства точку можно представлять не как массив [x, y], а как объект {x, y}

import pandas

def check_vertical_symmetry(points):
    xCoordinates = []
    yCoordinates = []
    sumOfX = 0
    for point in points:
        xCoordinates.append(point[0])
        yCoordinates.append(point[1])
        sumOfX += point[0]
    symmetryLine = sumOfX/len(xCoordinates)
    points = pandas.DataFrame({"x": xCoordinates, "y": yCoordinates})
    pointsBefore = points.loc[points["x"] < symmetryLine]
    pointsAfter = points.loc[points["x"] > symmetryLine]
    pointsBefore = pointsBefore.sort_values(["x", "y"], ascending = [True, True])
    pointsAfter = pointsAfter.sort_values(["x", "y"], ascending = [False, True])
    pointsBefore = pointsBefore.reset_index()
    pointsAfter = pointsAfter.reset_index()
    if (len(pointsBefore) != len(pointsAfter)):
        return(False)
    else:
        for i in range(len(pointsBefore)):
            if (pointsBefore["y"][i] != pointsAfter["y"][i]):
                return(False)
            elif (pointsBefore["x"][i] + pointsAfter["x"][i] != 2*symmetryLine):
                return(False)
    return(True)