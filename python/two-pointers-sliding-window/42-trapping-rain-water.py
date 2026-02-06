"""
42. Trapping Rain Water

Difficulty: Hard
Topics: Two Pointers, Dynamic Programming, Stack, Monotonic Stack, Array

Problem:
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Approach:
Simply, we can use two pointers to traverse the elevation map from both ends towards the center. We maintain two variables to keep track of the maximum height encountered from the left and right sides. 
At each step, we calculate the water trapped at the current position based on the minimum of the two maximum heights minus the current height.

Key Insights:
1. The boundaries of the array cannot contain water by default.
2. Water trapped at any position is determined by the difference between the shorter boundary (left max or right max) the current bar's height.

Complexity:
Time: O(n) - We traverse the elevation map once with two pointers, each moving towards the center at most n times.
Space: O(1) - We use a constant amount of extra space for variables.
"""

def trap(height: list[int]) -> int:
    n = len(height)
    left, right = 0, n - 1
    left_max, right_max = height[left], height[right]
    total_water = 0

    while left < right:

        if left_max <= right_max: 
            left += 1
            left_max = max(left_max, height[left])
            total_water += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            total_water += right_max - height[right]

    return total_water


if __name__ == "__main__":
    # Test cases
    assert trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
    assert trap([4,2,0,3,2,5]) == 9
    assert trap([1,0,2,1,0,1,3,2,1,2,1]) == 6
    print("All test cases passed!")
