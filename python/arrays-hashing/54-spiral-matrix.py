"""
54. Spiral Matrix

Difficulty: Medium
Topics: Array, Matrix, Simulation

Problem:
Given an m x n matrix, return all elements of the matrix in spiral order.

Approach:
Use four pointers to track the boundaries of the matrix (top, bottom, left, right).
While the pointers do not overlap:
    - Traverse from left to right along the top boundary, then move the top boundary down.
    - Traverse from top to bottom along the right boundary, then move the right boundary left.
    - If there are remaining rows, traverse from right to left along the bottom boundary, then move the bottom boundary up.
    - If there are remaining columns, traverse from bottom to top along the left boundary, then move the left boundary right.

Key Insights:
1. Pay attention to the boundaries to avoid duplicates when the matrix has odd dimensions.
2. Differenciate between boundary and index to prevent overstepping.

Edge Cases:
1. Handle single row or single column matrices correctly.

Complexity:
Time: O(m * n) - We visit each element in the matrix exactly once.
Space: O(1) - We only use a constant amount of extra space (the result list is not counted in space complexity).
"""
from typing import List

def spiralOrder(matrix: List[List[int]]) -> List[int]:
    result = []
    if not matrix: 
        return result
    top, bottom = 0, len(matrix)
    left, right = 0, len(matrix[0])

    while top < bottom and left < right:
        # Traverse from left to right
        for i in range(left, right):
            result.append(matrix[top][i])
        top += 1

        # Traverse from top to bottom
        for i in range(top, bottom):
            result.append(matrix[i][right - 1])
        right -= 1

        if top >= bottom or left >= right:
            break
            
        # Traverse from right to left
        for i in range(right - 1, left - 1, -1):
            result.append(matrix[bottom - 1][i])
        bottom -= 1

        # Traverse from bottom to top
        for i in range(bottom - 1, top - 1, -1):
            result.append(matrix[i][left])
        left += 1

    return result

if "__main__" == __name__:
    # Example usage
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print(spiralOrder(matrix))  # Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]