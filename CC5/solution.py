"""
CC5 Student Submission
Name: Sid Amarnath
"""

from typing import List, Tuple
import heapq


def scooter_rentals(times: List[Tuple[int, int]]) -> int:
    """
    Calculates the minimum number of scooters needed to satisfy all rental demands
    given a list of rental time intervals. The intervals are half-open, meaning 
    [t_start, t_end) does not overlap with [t_end, t_next_end).

    :param times: A list of tuples where each tuple contains two integers representing 
                  the start and end times of a rental in the form (t_start, t_end).
    :return: The minimum number of scooters needed to satisfy all rentals.
    """
    if len(times) == 0:
        return 0
    
    times.sort(key=lambda x: x[0])

    min_heap = []

    for start_time, end_time in times:
        if min_heap and min_heap[0] <= start_time:
            heapq.heappop(min_heap)
        
        heapq.heappush(min_heap, end_time)

    return len(min_heap)
