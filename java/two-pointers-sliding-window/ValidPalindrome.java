/**
 * 125. Valid Palindrome
 * Difficulty: Easy
 * Topics: Two Pointers, Sliding Window
 * 
 * Problem:
 * A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
 * it reads the same forward and backward. Alphanumeric characters include letters and numbers.
 * Given a string s, return true if it is a palindrome, or false otherwise.
 * 
 * Approach:
 * Clean the string by removing all non-alphanumeric characters and converting it to lowercase. 
 * Use two pointers to compare characters from the start and end of the cleaned string moving towards the center.
 * 
 * Key Insights:
 * 1. Using two pointers allows for efficient comparison from both ends of the string.

 * Edge Cases:
 * 1. An empty string is considered a palindrome.

 * Complexity:
 * Time: O(n) - Where n is the length of the input string, since we process each charater once
 * Space: O(n) - for storing the cleaned string
 */

public class ValidPalindrome {
    public static void main(String[] args) {
        // Test cases
    }

    public static boolean validePalindrome(String s) {
        s = s.toLowerCase().replaceAll("[^a-z0-9]", "");
        int left = 0;
        int right = s.length() - 1;

        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true; 
    }
}
