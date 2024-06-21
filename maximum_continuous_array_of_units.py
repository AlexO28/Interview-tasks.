# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 12:31:30 2024

@author: Семья
"""
#array 0 и 1, non empty
#delete one element
#maximium continuous array of units
def find_max_cont_array(arr):
    if len(arr) == 1:
        return 0
    blocks_of_ones = []
    good_blocks = []
    block_size = 0
    num_zeros = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            block_size += 1
            if i > 0:
                if arr[i] != arr[i-1]:
                    good_blocks.append(num_zeros > 0)
            num_zeros = 0
        else:
            num_zeros += 1
            if i > 0:
                if arr[i] != arr[i-1]:
                   blocks_of_ones.append(block_size)
            block_size = 0
    if arr[-1] == 1:
        blocks_of_ones.append(block_size)
    else:
        good_blocks.append(num_zeros > 0)
    if len(good_blocks) == 0:
        return blocks_of_ones[0]-1
    if arr[0] == 0:
        del good_blocks[0]
    max_size = 0
    for i in range(1, len(blocks_of_ones)):
        if good_blocks[i]:
            max_size = max(max_size, blocks_of_ones[i]+blocks_of_ones[i-1])
        else:
            max_size = max(max_size, blocks_of_ones[i], blocks_of_ones[i-1])
    return max_size
