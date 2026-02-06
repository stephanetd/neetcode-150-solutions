/**
 * 42. Trapping Rain Water
 * Difficulty: Medium
 * Topics: Array, Two Pointers, Stack, Dynamic Programming, Monotonic Stack
 * 
 * Problem:
 * Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
 * 
 * Approach:
 * Simply, we can use two pointers to traverse the elevation map from both ends towards the center. We maintain two variables to keep track of the maximum height encountered from the left and right sides. 
 * At each step, we calculate the water trapped at the current position based on the minimum of the two maximum heights minus the current height.
 * 
 * Key Insights:
 * 1. The boundaries of the array cannot contain water by default.
 * 2. Water trapped at any position is determined by the difference between the shorter boundary (left max or right max) the current bar's height.
 * 
 * Complexity:
 * Time: O(n) - We traverse the elevation map once with two pointers, each moving towards the center at most n times.
 * Space: O() - We use a constant amount of extra space for variables.
 */

public class TrappingRainWater {
    public static void main(String[] args) {
        // Test cases
        System.out.println(trap(new int[]{0,1,0,2,1,0,1,3,2,1,2,1}));  // Output: 6
        System.out.println(trap(new int[]{4,2,0,3,2,5}));  // Output: 9
        System.out.println(trap(new int[]{1,0,2,1,0,1,3,2,1,2,1}));  // Output: 6
    }

    public static int trap(int[] height) {
        int left = 0; int right = height.length - 1;
        int leftMax = height[left]; int rightMax = height[right];
        int totalWater = 0;

        while (left < right) {
            if (height[left] <= height[right]) {
                left += 1;
                leftMax = Math.max(leftMax, height[left]);
                totalWater += leftMax - height[left];
            } else {
                right -= 1;
                rightMax = Math.max(rightMax, height[right]);
                totalWater += rightMax - height[right];
            }
        }

        return totalWater;
    }
}
