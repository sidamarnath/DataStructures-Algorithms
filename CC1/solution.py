"""
CC1 Student Submission
Name: Sid Amarnath
"""

from typing import List, Tuple


def farmer_fencing(points: List[Tuple[int, int]]) -> int:
    """
    Calculates the minimum perimeter required to form a rectangle using the
    given points.
    :param points: The fence posts available to use.
    :return: The minimum perimeter of the fence.
    """

    
    #! Runtime Complexity -> O(n^2) - Two nested loops
    #! Spacetime Complexity -> O(n) - points_set set requires space
    points_set = set(points)
    minimum_perimeter = float('inf')

    #? Base case
    if len(points) < 4:
        return 0

    for i in range(len(points)):
        x1, y1 = points[i][0], points[i][1]
        for j in range(i + 1, len(points)):
            x2, y2 = points[j][0], points[j][1]
            if x1 != x2 and y1 != y2:
                if (x1, y2) in points_set and (x2, y1) in points_set:
                    perimeter = (2 * abs(y2 - y1)) + (2 * abs(x2 - x1))
                    minimum_perimeter = min(perimeter, minimum_perimeter)
    
    return minimum_perimeter if minimum_perimeter != float('inf') else 0



