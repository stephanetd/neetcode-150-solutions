/**
 * 49. Group Anagrams
 * 
 * Difficulty: Medium
 * Topics: Arrays, Hashing, String, HashTable
 * 
 * Problem:
 * Given an array of strings strs, group the anagrams together. You can return the answer in any order.
 * 
 * Approach:
 * Use a dictionary to map sorted strings to lists of anagrams that correspond to that sorted string
 * 
 * Key Insights:
 * 1. Anagrams have the same characters when sorted
 * 
 * Edge Cases:
 * 1. Empty strings.
 * 2. Single character strings.
 * 
 * Complexity:
 * Time: O(m * n log n) - where m is the number of strings and n is the average length of each string.
 * Space: O(m * n) - for storing the grouped anagrams.
 */
import java.util.*;

public class GroupAnagrams {
    // Implementation
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> anagrams = new HashMap<>();

        for (String str: strs) {
            char[] sorted_str = str.toCharArray();
            Arrays.sort(sorted_str);
            String key = new String(sorted_str);
            if (!anagrams.containsKey(key)) {
                anagrams.put(key, new ArrayList<>());
            }
            anagrams.get(key).add(str);

        }
        return new ArrayList<>(anagrams.values());
    }

    public static void main(String[] args) {
        // Example test cases
        System.out.println("Running tests for GroupAnagrams...");
        GroupAnagrams ga = new GroupAnagrams();
        System.out.println(ga.groupAnagrams(new String[]{"eat","tea","tan","ate","nat","bat"})); // Expected: [["bat"],["nat","tan"],["ate","eat","tea"]]
        System.out.println(ga.groupAnagrams(new String[]{""})); // Expected: [[""]]
        System.out.println(ga.groupAnagrams(new String[]{"a"})); // Expected: [["a"]]
    }
}
