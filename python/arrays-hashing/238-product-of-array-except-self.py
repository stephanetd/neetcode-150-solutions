"""
238. Product of Array Except Self

Difficulty: Medium
Topics: Array, Prefix Sum

Problem:
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
You must write an algorithm that runs in O(n) time and without using the division operation.

Approach:
Use the prefix sum pattern to calculate the product of all elements to the left and right of each index. It can be done in-place with O(1) extra space (excluding the output array).

Key Insights:
1. Prefix Products: Traverse the array from left to right, maintaining a running product of all elements to the left of the current index. Store this product in the output array.
2. Suffix Products: Traverse the array from right to left, maintaining a running product of all elements to the right of the current index. Multiply this product with the corresponding value in the output array.

Edge Cases:
1. Negative numbers in the array.
2. Zeros in the array.

Complexity:
Time: O(n) - Two passes through the array.
Space: O(1) - Output array is not counted as extra space.
"""

from typing import List

def product_except_self(nums: List[int]) -> List[int]:
    n = len(nums)
    answer = [1] * n

    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n-1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]
    
    return answer

if __name__ == "__main__":
    # Example test cases
    print(product_except_self([1,2,3,4]))  # Output: [24,12,8,6]
    print(product_except_self([-1,1,0,-3,3]))  # Output: [0,0,9,0,0]
    print(product_except_self([0,0]))  # Output: [0,0]

