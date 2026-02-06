/**
 * 11. Container With Most Water
 * Difficulty: Hard
 * Topics: Two Pointers, Array, Greedy
 * 
 * Problem:
 * You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
 * Find two lines that together with the x-axis form a container, such that the container contains the most water. Return the maximum amount of water a container can store.
 * 
 * Approach:
 * Simply, we calculate max area of a rectangle then return it. Formula is width * height
 * Each number is height, so we can easily get height and width is just distance between two heights. That's why it's good idea to have two pointers left and right.
 * 
 * Key Insights:
 * 1. For height, we take smaller height between left and right, because if we calculate based on the taller height, the water would overflow from the container.
 * 2. Move the pointer pointing to the shorter line inward, as this may lead to a taller line and potentially a larger area.

 * Edge Cases:
 * 1. If the input array is empty or has less than two lines, the maximum area is 0.
 * 2. If all heights are the same, the maximum area is determined by the distance between the two farthest lines.

 * Complexity:
 * Time: O(n) - We traverse the array with two pointers, each moving towards the center at most n times
 * Space: O(1) - We use a constant amount of extra space for variables
 */

public class ContainerWithMostWater {
    public static void main(String[] args) {
        // Test cases
        System.out.println(maxArea(new int[]{1,8,6,2,5,4,8,3,7}));  // Output: 49
        System.out.println(maxArea(new int[]{1,1}));  // Output:
    }

    public static int maxArea(int[] height) {
        int n = height.length;
        int maxArea = 0;
        int left = 0; int right = n-1;

        while (left < right) {
            int leftVertical = height[left]; int rightVertical = height[right];
            if (leftVertical >= rightVertical) {
                maxArea = Math.max(maxArea, (right - left) * rightVertical);
                right -= 1;
            } else {
                maxArea = Math.max(maxArea, (right - left) * leftVertical);
                left += 1;
            }
        }

        return maxArea;
    }
}
