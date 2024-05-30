# -*- coding: utf-8 -*-
"""
Created on Thu May 30 17:00:19 2024

@author: Семья
"""
f = open("input.txt", "r")
line = f.readline().strip()
d, i, r = line.split(" ")
d = int(d)
i = int(i)
r = int(r)
n = int(f.readline().strip())
line = f.readline().strip()
nums_init = line.split(" ")
nums_init = [int(num) for num in nums_init]
m = int(f.readline().strip())
line = f.readline().strip()
nums_fin = line.split(" ")
nums_fin = [int(num) for num in nums_fin]
f.close()
num_erased = len([num for num in nums_init if num not in nums_fin])
num_constructed = len([num for num in nums_fin if num not in nums_init])
res = 0
price = min(d+i, r)
for j in range(min(len(nums_init), len(nums_fin))):
    if nums_init[j] != nums_fin[j]:
        res += price
if m > n:
    res += (m-n)*i
    num_constructed -= m-n
elif m < n:
    res += (n-m)*d
    num_erased -= n-m
if num_erased < num_constructed:
    res += (num_constructed - num_erased)*i
else:
    res += (num_erased - num_constructed)*d
g = open("output.txt", "w")
g.write(str(res))
g.close()
