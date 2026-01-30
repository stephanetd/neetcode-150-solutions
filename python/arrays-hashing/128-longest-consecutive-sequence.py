"""
128. Longest Consecutive Sequence

Difficulty: Medium
Topics: Arrays, Hash Table, Union Find

Problem:
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence. Algorithm must run in O(n) time.

Approach:
Only start counting at the beginning of a sequence (i.e., when num - 1 is not in the set).

Key Insights:
1. O(1) Membership Check: Using a set allows for O(1) average time complexity for membership checks.
2. Sequence Start Identification: By only starting to count a sequence from numbers that are the beginning of a sequence 
(i.e., num - 1 not in set), we avoid redundant work and ensure each sequence is counted only once.

Edge Cases:
1. Array is sorted in descending order.

Complexity:
Time: O(n) - We iterate through the array twice, and each operation in the set is O(1) on average.
Space: O(n) - The set stores all elements of the input array.

"""

from typing import List

def longest_consecutive(nums: List[int]) -> int:
    num_set = set(nums)
    longest = 0

    for num in num_set:
        if num - 1 not in num_set: # Start of a sequence
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
            longest = max(longest, current_streak)

    return longest


if __name__ == "__main__":
    # Example test cases
    print(longest_consecutive([100, 4, 200, 1, 3, 2]))  # Output: 4
    print(longest_consecutive([0, -1]))                  # Output: 2
    print(longest_consecutive([9,1,4,7,3,-1,0,5,8,-1,6])) # Output: 7
