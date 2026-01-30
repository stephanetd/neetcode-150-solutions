/**
 * 238. Product of Array Except Self
 * 
 * Difficulty: Medium
 * Topics: Array, Prefix Sum
 * 
 * Problem:
 * Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
 * You must write an algorithm that runs in O(n) time and without using the division operation.
 * 
 * Approach:
 * Use the prefix sum pattern to calculate the product of all elements to the left and right of each index. It can be done in-place with O(1) extra space (excluding the output array).
 * 
 * Key Insights:
 * 1. Prefix Products: Traverse the array from left to right, maintaining a running product of all elements to the left of the current index. Store this product in the output array.
 * 2. Suffix Products: Traverse the array from right to left, maintaining a running product of all elements to the right of the current index. Multiply this product with the corresponding value in the output array.
 * 
 * Edge Cases:
 * 1. Negative numbers in the array.
 * 2. Zeros in the array.
 * 
 * Complexity:
 * Time: O(n) - Two passes through the array.
 * Space: O(1) - Output array is not counted as extra space.
 */

public class ProductofArrayExceptSelf {
    // Implementation
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] output = new int[n];

        // Step 1: Calculate prefix products
        int prefixProduct = 1;
        for (int i = 0; i < n; i++) {
            output[i] = prefixProduct;
            prefixProduct *= nums[i];
        }

        // Step 2: Calculate suffix products and multiply with prefix products
        int suffixProduct = 1;
        for (int i = n - 1; i >= 0; i--) {
            output[i] *= suffixProduct;
            suffixProduct *= nums[i];
        }

        return output;
    }

    public static void main(String[] args) {
        ProductofArrayExceptSelf solution = new ProductofArrayExceptSelf();
        int[] nums = {1, 2, 3, 4};
        int[] result = solution.productExceptSelf(nums);
        // Print the result
        for (int val : result) {
            System.out.print(val + " ");
        }
        System.out.println(); // New line for readability
        
    }
}
