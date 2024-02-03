#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)

        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1



#====================================================================
# 1） read data from file : numbers-4.txt
with open('numbers-4.txt', 'r') as file:
    sorted_data = list(map(int, file.read().split()))

# 2）quick sort
quick_sort(sorted_data, 0, len(sorted_data) - 1)
print("sort result：", sorted_data)

# 3）search number, print number position:
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
