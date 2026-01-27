/**
 * 1. Two Sum
 * 
 * Difficulty: Easy
 * Topics: Arrays, HashTable
 * 
 * Problem:
 * Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
 * 
 * Approach:
 * Use a hash map to store the complement of each number and its index.
 * 
 * Key Insights:
 * 1. For each number in the array, we check if its complement (target - number) exists in the hash map.
 * 2. If the complement exists, we have found the two numbers that sum to the target.
 * 
 * Edge Cases:
 * 1. No two numbers sum to the target (assumed not to happen as per problem statement).
 * 2. Array with negative numbers and zeros.
 * 
 * Complexity:
 * Time: O(n) - We traverse the array once.
 * Space: O(n) - The hash map can store up to n elements.
 */

import java.util.HashMap;

public class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> numToIndex = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (numToIndex.containsKey(complement)) {
                return new int[]{numToIndex.get(complement), i};
            } else {
                numToIndex.put(nums[i], i);
            }
        }
        return new int[]{}; // Should never reach here as per problem statement
    }

    public static void main(String[] args) {
        System.out.println("Running tests for TwoSum...");
        TwoSum solution = new TwoSum();
        int[] result1 = solution.twoSum(new int[]{2, 7, 11, 15}, 9);
        System.out.println("Expected: [0, 1], Got: [" + result1[0] + ", " + result1[1] + "]");

        int[] result2 = solution.twoSum(new int[]{3, 2, 4}, 6);
        System.out.println("Expected: [1, 2], Got: [" + result2[0] + ", " + result2[1] + "]");

        int[] result3 = solution.twoSum(new int[]{3, 3}, 6);
        System.out.println("Expected: [0, 1], Got: [" + result3[0] + ", " + result3[1] + "]");
    }
}
