"""
167. Two Sum II - Input Array Is Sorted

Difficulty: Medium
Topics: Array, Sliding Window, Binary Search

Problem:
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. 
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

Approach:
Binary Search since the array is sorted. 

Complexity:
Time: O(n) - where n is the length of the input array, since we process each element at most once.
Space: O(1) - only using a constant amount of extra space.
"""
from typing import List

def twoSum(numbers: List[int], target: int) -> List[int]:
    left, right = 0, len(numbers) - 1
    # Binary Search on sorted array
    while left < right:
        sum = numbers[left] + numbers[right]
        if sum == target:
            res = [left+1, right+1]
            break
        elif sum > target:
            right -= 1
        else:
            left += 1
    
    return res

if __name__ == "__main__":
    # Test cases
    pass
