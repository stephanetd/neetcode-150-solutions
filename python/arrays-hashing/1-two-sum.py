"""
1. Two Sum

Difficulty: Easy
Topics: Array, HashTable

Problem:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

Approach:
Use a hash map to store the complement of each number and its index.

Key Insights:
1. For each number in the array, we check if its complement (target - number) exists in the hash map.
2. If the complement exists, we have found the two numbers that sum to the target.

Edge Cases:
1. No two numbers sum to the target (assumed not to happen as per problem statement).
2. Array with negative numbers and zeros.

Complexity:
Time: O(n) - We traverse the array once.
Space: O(n) - The hashmap can store up to n elements.
"""

def twoSum(nums: list[int], target: int) -> list[int]:
    hashmap = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap.keys():
            return [hashmap[complement], i]
        hashmap[num] = i
    return []

if __name__ == "__main__":
    print("Running tests for ContainsDuplicate...")
    assert twoSum([2,7,11,15], 9) == [0,1]
    assert twoSum([3,2,4], 6) == [1,2]
    assert twoSum([3,3], 6) == [0,1]
    print("All tests passed.")
