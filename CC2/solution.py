"""
CC2
Name: Sid Amarnath
"""

from typing import List


def solar_power(heights: List[int]) -> int:
    """
    Calculates the maximum area from a histogram.
    :param heights: List of heights.
    :return: The max area rectangle that can be formed from histogram.
    """
    max_area = 0
    stack = [] #! (index, height)

    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            area = height * (i - index)
            max_area = max(max_area, area)
            start = index
        stack.append((start, h))
        
    
    for idx, ht in stack:
        a = ht * (len(heights) - idx)
        max_area = max(max_area, a)
    
    return max_area





            
