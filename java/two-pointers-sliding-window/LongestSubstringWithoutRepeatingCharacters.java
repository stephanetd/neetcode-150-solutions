/**
 * 3. Longest Substring Without Repeating Characters
 * Difficulty: Medium
 * Topics: Staff, String, Hash Table Sliding Window
 * 
 * Problem:
 * Given a string s, find the length of the longest substring without duplicate characters.
 * 
 * Approach:
 * We can use the sliding window technique with two pointers to keep track of the current substring without repeating characters.
 * We will also use a hashmap to store the characters in the current window and their last position. As we expand the right pointer, we check if the character is already in the set. 
 * If it is, we move the left pointer to the right until we remove the duplicate character from the set. We keep track of the maximum length of the substring found during this process.
 * 
 * Key Insights:
 * 1. Using a hashmap allows for O(1) average time complexity for checking duplicates.
 * 2. The sliding window technique efficiently narrows down the search space without needing to check all possible substrings.

 * Edge Cases:
 * 1. A string with all unique characters.
 * 2. A string with all identical characters.

 * Complexity:
 * Time: O(n) - We traverse the string once with the right pointer, and the left pointer only moves forward.
 * Space: O(n) - At worst, we may need to store all characters in the hashmap if all characters are unique.
 */

import java.util.HashMap;
import java.util.Map;

public class LongestSubstringWithoutRepeatingCharacters {
    public static void main(String[] args) {
        // Test cases
    }

    public static int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> charIndexMap = new HashMap<>();
        int left = 0; int maxLength = 0;

        for (int right = 0; right < s.length(); right++) {
            char currentChar = s.charAt(right);
            if (charIndexMap.containsKey(currentChar)) {
                if (charIndexMap.get(currentChar) >= left) {
                    left = charIndexMap.get(currentChar) + 1;
                }
            }
            charIndexMap.put(currentChar, right);
            maxLength = Math.max(maxLength, right - left + 1);
        }
        
        return maxLength;
    }
        
}
