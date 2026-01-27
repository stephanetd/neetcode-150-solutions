"""
217. Contains Duplicate

Difficulty: Easy
Topics: Arrays, Hashing, Sorting

Problem: 
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Approach:
Use a set to track seen numbers as we iterate through the list. 
If we encounter a number that is already in the set, we return True. 
If we finish iterating without finding duplicates, we return False.

Key Insights:
1. Sets provide O(1) average time complexity for lookups, making them ideal for this problem.
2. Early exit upon finding a duplicate improves efficiency.

Edge Cases:
1. Empty list should return False.
2. List with one element should return False.

Complexity:
Time: O(n) - Single pass through array
Space: O(n) - Worst case stores all n elements
"""
from typing import List

def containsDuplicate(nums: List[int]) -> bool:
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
        """
        return len(set(nums)) != len(nums)
        
if __name__ == "__main__":
    print("Running tests for ContainsDuplicate...")
    assert containsDuplicate([1,2,3,1]) == True
    assert containsDuplicate([1,2,3,4]) == False
    assert containsDuplicate([]) == False
    assert containsDuplicate([1]) == False
    print("All tests passed.")
