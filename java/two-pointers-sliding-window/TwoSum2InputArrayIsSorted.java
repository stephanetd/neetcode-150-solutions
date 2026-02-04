/**
 * 167. Two Sum II - Input Array Is Sorted
 * Difficulty: Medium
 * Topics: Two Pointers, Sliding Window
 * 
 * Problem:
 * Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. 
 * Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
 * Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
 * 
 * Approach:
 * Binary Search since the array is sorted.
 * 
 * Complexity:
 * Time: O(n) - where n is the length of the input array, since we process each element at most once.
 * Space: O(1) - only using a constant amount of extra space.
 */

public class TwoSum2InputArrayIsSorted {
    public static void main(String[] args) {
        // Test cases
    }

    public static int[] twoSum(int[] numbers, int target) {
        int left = 0;
        int right = numbers.length-1;

        while (left < right) {
            int sum = numbers[left] + numbers[right];
            if (sum > target) right -= 1;
            else if (sum < target) left += 1;
            else return new int[]{left+1, right+1};
        }
        return new int[]{-1,-1};
    }
}
