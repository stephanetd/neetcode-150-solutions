/**
 * 54. Spiral Matrix
 * 
 * Difficulty: Medium
 * Topics: Array, Matrix, Simulation
 * 
 * Problem:
 * Given an m x n matrix, return all elements of the matrix in spiral order.
 * 
 * Approach:
 * Use four pointers to track the boundaries of the matrix (top, bottom, left, right).
 * While the pointers do not overlap:
    - Traverse from left to right along the top boundary, then move the top boundary down.
    - Traverse from top to bottom along the right boundary, then move the right boundary left.
    - If there are remaining rows, traverse from right to left along the bottom boundary, then move the bottom boundary up.
    - If there are remaining columns, traverse from bottom to top along the left boundary, then move the left boundary right.
 * 
 * Key Insights:
 * 1. Pay attention to the boundaries to avoid duplicates when the matrix has odd dimensions.
 * 2. Differenciate between boundary and index to prevent overstepping.
 * 
 * Edge Cases:
 * 1. Handle empty matrix (null or zero rows/columns).
 * 
 * Complexity:
 * Time: O(m x n) - We visit each element in the matrix exactly once. 
 * Space: O(1) - We only use a constant amount of extra space (the result list is not counted in space complexity).
 */

import java.util.List;
import java.util.ArrayList;

public class SpiralMatrix {
    // Implementation
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> result = new ArrayList<>();
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return result;
        }
        int top = 0, bottom = matrix.length;
        int left = 0, right = matrix[0].length;

        while (top < bottom && left < right) {
            // Traverse from left to right
            for (int i = left; i < right; i++) {
                result.add(matrix[top][i]);
            }
            top++;

            // Traverse from top to bottom
            for (int i = top; i < bottom; i++) {
                result.add(matrix[i][right - 1]);
            }
            right--;

            if (top >= bottom || left >= right) {
                break;
            }

            // Traverse from right to left
            for (int i = right - 1; i >= left; i--) {
                result.add(matrix[bottom - 1][i]);
            }
            bottom--;

            // Traverse from bottom to top
            for (int i = bottom - 1; i >= top; i--) {
                result.add(matrix[i][left]);
            }
            left++;
        }

        return result;
    }

    public static void main(String[] args) {
        // Test cases
        int[][] matrix1 = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };

        SpiralMatrix sm = new SpiralMatrix();
        List<Integer> result1 = sm.spiralOrder(matrix1);
        System.out.println(result1); // Expected: [1, 2, 3, 6, 9, 8, 7, 4, 5]
    }

}
