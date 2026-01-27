/**
 * 242. Valid Anagram
 * 
 * Difficulty: Easy
 * Topics: Arrays, Hashing, Sorting
 * 
 * Problem:
 * Given two strings s and t, return true if t is an anagram of s, and false otherwise.
 * 
 * Approach:
 * Use a hash map to count the frequency of each character in both strings.
 * 
 * Key Insights:
 * 1. If both strings have the same character frequencies, they are anagrams.
 * 2. Hash maps provide O(1) average time complexity for lookups and updates.
 * 3. Using a single dictionary to count frequencies for both strings can optimize space.
 * 
 * Edge Cases:
 * 1. Different lengths of strings should immediately return False.
 * 2. Empty strings are anagrams of each other.
 * 
 * Complexity:
 * Time: O(n) - We traverse both strings once.
 * Space: O(1) - The hash map will have at most 26 entries for lowercase letters.
 */

import java.util.HashMap;
import java.util.Map;

public class ValidAnagram {
    // Implementation
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        Map<Character, Integer> charCount = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            charCount.put(s.charAt(i), charCount.getOrDefault(s.charAt(i), 0) + 1);
        }

        for (int i = 0; i < t.length(); i++) {
            charCount.put(t.charAt(i), charCount.getOrDefault(t.charAt(i), 0) - 1);
            if (charCount.get(t.charAt(i)) < 0) {
                return false;
            }
        }

        return true;
    }

    public static void main(String[] args) {
        System.out.println("Running tests for ValidAnagram...");
        ValidAnagram solution = new ValidAnagram();
        System.out.println(solution.isAnagram("anagram", "nagaram")); // true
        System.out.println(solution.isAnagram("rat", "car")); // false
        System.out.println(solution.isAnagram("", "")); // true
        System.out.println(solution.isAnagram("a", "b")); // false
    }
}
