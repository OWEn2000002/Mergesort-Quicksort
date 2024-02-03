#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


#====================================================================
# 1) read data from file : numbers-4.txt
with open('numbers-4.txt', 'r') as file:
    sorted_data = list(map(int, file.read().split()))


# 2) Used merge_sort() to sort 
merge_sort(sorted_data)
print("sort result：", sorted_data)

# 3) search number, print number position:
element = 90262
if element in sorted_data:
    position = sorted_data.index(element)
    print("元素", element, "的位置为：", position)
else:
    print("元素", element, "不存在！")

element = 11559
if element in sorted_data:
    position = sorted_data.index(element)
    print("元素", element, "的位置为：", position)
else:
    print("元素", element, "不存在！")