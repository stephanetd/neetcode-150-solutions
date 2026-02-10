/**
 * 424. Longest Repeating Character Replacement
 * Difficulty: Medium
 * Topics: String, Hash Table, Sliding Window
 * 
 * Problem:
 * You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
 * Return the length of the longest substring containing the same letter you can get after performing the above operations.
 * 
 * Approach:
 * Using sliding window, checked window length with the max frequency, if greater then increase the left pointer, to find is it the best substring or not.
 * 
 * Key Insights:
 * 1. We can use a sliding window to keep track of the longest substring with the same character.
 * 2. We need to keep track of the frequency of characters in the current window to determine how many characters we need to replace to make all characters the same.

 * Edge Cases:
 * 1. A string with all identical characters.
 * 2. A string with all unique characters.

 * Complexity:
 * Time: O(n) - We traverse the string once with the right pointer, and the left pointer only moves forward.
 * Space: O(1) - We use a hashmap to store the frequency of characters in the current window, which can grow up to O(26) for uppercase English letters, so it is O(1) in terms of space complexity.
 */

public class LongestRepeatingCharacterReplacement {
    public static void main(String[] args) {
        // Test cases
        System.out.println(characterReplacement("ABAB", 2));  // Output: 4
        System.out.println(characterReplacement("AABABBA", 1));  // Output: 4
        System.out.println(characterReplacement("AAAA", 2));  // Output: 4
    }

    public static int characterReplacement(String s, int k) {
        int[] freq = new int[26];
        int maxFreq = 0; int maxLength = 0; int left = 0;

        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);
            freq[c - 'A']++;
            int windowLength = right - left + 1;
            maxFreq = Math.max(maxFreq, freq[c-'A']);

            if (windowLength - maxFreq > k) {
                freq[s.charAt(left) - 'A']--;
                left += 1;
            } else {
                maxLength = Math.max(maxLength, windowLength);
            }
        }
        return maxLength;
    }
}
