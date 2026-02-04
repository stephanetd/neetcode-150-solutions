/**
 * 15. 3Sum
 * Difficulty: Medium
 * Topics: Two Pointers, Array, Sorting
 * 
 * Problem:
 * Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
 * Notice that the solution set must not contain duplicate triplets.
 * 
 * Approach:
 * Sort the array to facilitate the two-pointer technique and duplicate handling.
 * Use a loop to fix one element and apply the two-pointer technique to find pairs that sum to the negative of the fixed element.
 * 
 * Key Insights:
 * 1. After sorting, we can use a fixed pointer and two pointers (left and right) to find triplets efficiently.
 * 2. Skip duplicates to avoid duplicate triplets in the result.
 * 
 * Edge Cases:
 * 1. Empty array or less than three elements.
 * 2. All elements are the same.

 * Complexity:
 * Time: O(n) - where n is the length of the input array, since we have a nested loop structure.
 * Space: O(1) - only using a constant amount of extra space.
 */

import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;

public class ThreeSum {
    public static void main(String[] args) {
        // Test cases
        int[] nums1 = {-1, 0, 1, 2, -1, -4};
        int[] nums2 = {};
        System.out.println(threeSum(nums1)); // Expected: [[-1, -1, 2], [-1, 0, 1]]
        System.out.println(threeSum(nums2)); // Expected: []
    }

    public static List<List<Integer>> threeSum(int[] nums) {
        int n = nums.length;
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            // Skip conditions
            if (nums[i] > 0) break;
            if (i != 0 && nums[i] == nums[i-1]) continue;

            int j = i + 1; int k = n-1;
            while (j < k) {
                int sum = nums[i] + nums[j] + nums[k];
                if (sum > 0) k -= 1;
                else if (sum < 0) j += 1;
                else {
                    result.add(Arrays.asList(nums[i], nums[j], nums[k]));
                    j += 1; k -= 1;
                    // Skip duplicates for j and k
                    while (j < k && nums[j] == nums[j-1]) j += 1;
                    while (j < k && nums[k] == nums[k+1]) k -= 1;
                }
            }
        }
        return result;
    }
}



