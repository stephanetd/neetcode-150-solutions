/**
 * 36. Valid Sudoku
 * 
 * Difficulty: Medium
 * Topics: Array, Hash Table, Matrix 
 * 
 * Problem:
 * Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
 * Each row must contain the digits 1-9 without repetition.
 * Each column must contain the digits 1-9 without repetition.
 * Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
 * 
 * Approach:
 * Use a HashSet to track seen numbers in rows, columns, and 3x3 sub-boxes.
 * For each cell in the board:
 *   - If it's an empty cell ('.'), skip it.
 *   - Otherwise, check if the number is already in the corresponding row, column, or sub-box set.
 *   - If it is, return false (invalid Sudoku).
 *   - If not, add it to the respective sets.
 * 
 * Key Insights:
 * 1. 
 * 
 * Edge Cases:
 * 1. 
 * 
 * Complexity:
 * Time: O(1) - We iterate through the board once, and each operation in the set is O(1) on average.
 * Space: O(1) - The maximum number of elements in any set is 9, so space is constant.
 */

public class ValidSudoku {
    // Implementation
}
