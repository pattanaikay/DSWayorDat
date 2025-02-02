"""
Given an integer array, return the maximum product of any three numbers in the array?

"""

import heapq

def maxThreeProduct(num:list)->int:
    num.sort()
    n = len(num)
    return max(num[n-1] * num[n-2] *num[n-3], num[n-1]* num[0] * num[1])


# using heapq

def maxThreeProduct(num:list):
    a = heapq.nlargest(3, num)
    b = heapq.nsmallest(2, num)
    return max(a[2] * a[1] *a[0], a[0] * b[0] * b[1])