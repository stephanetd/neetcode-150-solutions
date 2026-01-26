from typing import List

"""
217. Contains Duplicate

Difficulty: Easy
Topics: Arrays, Hashing, Sorting

Time Complexity: O(n)
Space Complexity: O(n)

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
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
        """
        return len(set(nums)) != len(nums)
        

    def test(self):
        """Test cases"""
        test_cases = [
            ([1,2,3,1], True),
            ([1,1,1,1], True),
            ([1,1,1,3,3,4,3,2,4,2], True),
            ([], False),
            ([1], False),
            ([1,2,3,4,5], False),
        ]
        
        for i, (input_data, expected) in enumerate(test_cases):
            result = self.containsDuplicate(input_data)
            if result == expected:
                print(f"Test case {i+1}: PASSED")
            else:
                print(f"Test case {i+1}: FAILED")
                print(f"  Expected: {expected}")
                print(f"  Got: {result}")
        
if __name__ == "__main__":
    solution = Solution()
    solution.test()
