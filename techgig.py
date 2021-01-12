#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 11:15:28 2020

@author: roott
"""

def main(R, C, arr):
    max_counter = 0
    reg_count = 0
    for i in range(R):
        for j in range(C):
            if(arr[i][j] == 1):
                reg_count = count_cells(arr, i, j)
                max_counter = max(max_counter, reg_count)
    return (max_counter)

def count_cells(arr, i, j):
    if any([i<0, j<0, i>= len(arr), j >= len(arr[0])]):
        return 0
    if (arr[i][j] == 0):
        return 0
    
    cell_count = 1
    arr[i][j] = 0
    for r in range(i-1, i+2):
        for c in range(j-1, j+2):
            if any([r!=i, c!=j]):
                cell_count +=count_cells(arr,r,c)
    return cell_count      


coders_info = [[1, 1, 1, 0, 0], 
             [1, 1, 1, 1, 0],
             [0, 0, 0, 1, 1], 
             [1, 0, 0, 1, 1],
             [1, 1, 1, 1, 1]] 
R = 5
C = 5
print(main(R,C, coders_info))