"""
15. 3Sum

Difficulty: Medium
Topics: Two Pointers, Array, Sorting

Problem:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Approach:
Sort the array to facilitate the two-pointer technique and duplicate handling.
Use a loop to fix one element and apply the two-pointer technique to find pairs that sum to the negative of the fixed element.

Key Insights:
1. After sorting, we can use a fixed pointer and two pointers (left and right) to find triplets efficiently.
2. Skip duplicates to avoid duplicate triplets in the result.

Edge Cases:
1. Empty array or less than three elements.
2. All elements are the same.

Complexity:
Time: O(n^2) - where n is the length of the input array, since we have a nested loop structure.
Space: O(1) - only using a constant amount of extra space.
"""

def threeSum(nums: list[int]) -> list[list[int]]:
    n = len(nums)
    nums = sorted(nums) # Sorting the array
    triplets = []

    for i in range(n):
        # Skip conditions
        if nums[i] > 0: # we skip the positive numbers of the array
            break
        if  i!= 0 and nums[i] == nums[i-1]: # we skip duplicate negative numbers
            continue

        j, k = i+1, n-1
        while j < k:
            sum = nums[i] + nums[j] + nums[k]
            if sum > 0:
                k -= 1
            elif sum < 0:
                j += 1
            else: # sum == 0
                triplets.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
                # we continue searching for other triplets
                # skip conditions for duplicates
                while j < k and nums[j] == nums[j-1]: # if the next left border is a duplicate of the previous one
                    j += 1
                while j < k and nums[k] == nums[k+1]: # if the next right border is a duplicate of the previous one
                    k -= 1

    return triplets


    

if __name__ == "__main__":
    # Test cases
    assert threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert threeSum([]) == []
    print('All tests passed!')
