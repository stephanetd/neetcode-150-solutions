/**
 * 567. Permutation in String
 * Difficulty: Medium
 * Topics: Principal, Hash Table, Two Pointers, String, Sliding Window
 * 
 * Problem:
 * Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
 * In other words, return true if one of s1's permutations is the substring of s2.
 * 
 * Approach:
 * Since a permutation of s1 must have the same character counts, we can use a fixed-size sliding window over s2 whose length is exactly len(s1).
 * We maintain two frequency arrays: one for s1 and one for the current window in s2
 * If these two arrays ever match, the window is a valid permutation. As we slide the window forward, we update counts by removing the left character and adding the new right character — no need to rebuild the counts each time.
 * 
 * Key Insights:
 * 1. The sliding window must be exactly the length of s1 to ensure we are checking for valid permutations. A window of different size cannot be a permutation of s1.
 * 2. When updating the frequency counts during window sliding, the matches counter must be carefully updated. A character transition from matching to non-matching should decrement matches, and vice versa. 

 * Complexity:
 * Time: O(n) - where n is the length of s2, since we are sliding through s2 once and each character update is O(1)
 * Space: O(1) - since the frequency arrays are of fixed size 26 for lowercase letters
 */

public class PermutationInString {
    public static void main(String[] args) {
        // Test cases
        System.out.println(checkInclusion("ab", "eidbaooo")); // true
        System.out.println(checkInclusion("ab", "eidboaoo")); // false

    }

    public static boolean checkInclusion(String s1, String s2) {
        if (s1.length() > s2.length()) {
            return false;
        }

        int[] s1Count = new int[26];
        int[] s2Count = new int[26];
        for (int i = 0; i < s1.length(); i++) {
            s1Count[s1.charAt(i) - 'a']++;
            s2Count[s2.charAt(i) - 'a']++;
        }

        int matches = 0;
        for (int i = 0; i < 26; i++) {
            if (s1Count[i] == s2Count[i]) {
                matches++;
            }
        }

        int l = 0;
        for (int r = s1.length(); r < s2.length(); r++) {
            if (matches == 26) {
                return true;
            }

            int index = s2.charAt(r) - 'a';
            s2Count[index]++;
            if (s1Count[index] == s2Count[index]) {
                matches++;
            } else if (s1Count[index] + 1 == s2Count[index]) {
                matches--;
            }

            index = s2.charAt(l) - 'a';
            s2Count[index]--;
            if (s1Count[index] == s2Count[index]) {
                matches++;
            } else if (s1Count[index] - 1 == s2Count[index]) {
                matches--;
            }
            l++;
        }
        return matches == 26;
    }
}
