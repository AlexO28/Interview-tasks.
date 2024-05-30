# -*- coding: utf-8 -*-
"""
Created on Thu May 30 12:44:39 2024

@author: Семья
"""
def turn_to_int(elem):
    if elem == "00":
        return 0
    elif elem[0] == "0":
        return int(elem[1])
    else:
        return int(elem)


def line_to_secs(line):
    hours, minutes, seconds = line.split(":")
    return turn_to_int(hours)*3600 + turn_to_int(minutes)*60 + turn_to_int(seconds)

f = open("input.txt", "r")
line = f.readline()
n = int(line)
if n == 1:
   f.close()
   g = open("output.txt", "w")
   g.write("1")
   g.close()   
times = []
for j in range(n):
    line_start, line_end = f.readline().strip().split("-")
    date_start = line_to_secs(line_start)
    date_end = line_to_secs(line_end)
    if date_end == 0:
        if date_start == 0:
            times.append([86400, 86400])
        else:
            times.append([date_start, 86400])
    else:
       if date_end < date_start:
          times.append([date_start, 86400])
          times.append([0, date_end])
       else:
          times.append([date_start, date_end])
times.sort()
max_res = 0
res = 1
start = 0
end = 1
while start < len(times):
    if times[end][0] <= times[start][1]:
        res += 1
        end += 1
        if end == len(times):
            break
    else:
        max_res = max(max_res, res)
        found = False
        for j in range(start+1, len(times)):
            if times[j][1] != times[start][1]:
                start = j
                end = start + 1
                res = 1
                found = True
                break
        if not found:
            break
        if end == len(times):
            break
max_res = max(max_res, res)
f.close()
g = open("output.txt", "w")
g.write(str(max_res))
g.close()
