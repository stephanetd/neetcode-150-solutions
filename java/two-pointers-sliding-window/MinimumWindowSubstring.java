/**
 * 76. Minimum Window Substring
 * Difficulty: Hard
 * Topics: Hash Table, String, Sliding Window
 * 
 * Problem:
 * Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. 
 * If there is no such substring, return the empty string "".
 * 
 * Approach:
 * 
 * 
 * Key Insights:
 * 1. 

 * Complexity:
 * Time: O() - 
 * Space: O() - 
 */

import java.util.HashMap;
import java.util.Map;

public class MinimumWindowSubstring {
    public static void main(String[] args) {
        // Test cases
        System.out.println(minWindow("ADOBECODEBANC", "ABC")); // Expect: "BANC"
        System.out.println(minWindow("a", "a")); // Expect: "a"
        System.out.println(minWindow("aa", "aa")); // Expect: "aa"
    }

    public static String minWindow(String s, String t) {
        // Variables to track the smallest window
        int maxlen = Integer.MAX_VALUE;  // Minimum window length found
        int idx = 0;                     // Starting index of minimum window
        
        // Hash array to count characters (ASCII size 128)
        int hash[] = new int[128];
        
        // cnt: count of required characters found in current window
        int cnt = 0;
        
        // Two pointers for sliding window
        int left = 0, right = 0;

        // Step 1: Build frequency map for string t
        for (int j = 0; j < t.length(); j++) {
            char ch = t.charAt(j);
            hash[ch]++;  // Count each character in t
        }

        // Step 2: Expand window by moving right pointer
        while (right < s.length()) {
            char ch = s.charAt(right);
            
            // If this character is needed (count > 0), increment cnt
            if (hash[ch] > 0) {
                cnt++;
            }
            hash[ch]--;  // Decrement count (we've included this character)

            // Step 3: Shrink window when we have all required characters
            while (cnt == t.length()) {
                // Update minimum window if current is smaller
                if ((right - left + 1) < maxlen) {
                    maxlen = right - left + 1;
                    idx = left;
                }

                // Try to shrink: remove left character from window
                char leftChar = s.charAt(left);
                hash[leftChar]++;  // Put the character back in hash
                
                // If we removed a needed character, decrement cnt
                if (hash[leftChar] > 0) {
                    cnt--;
                }
                
                left++;  // Move left pointer forward
            }
            
            right++;  // Move right pointer forward
        }

        // Step 4: Return result
        if (maxlen == Integer.MAX_VALUE) return "";  // No valid window found
        return s.substring(idx, idx + maxlen);       // Return minimum window

    }
}
