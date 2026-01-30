/**
 * 128. Longest Consecutive Sequence
 * 
 * Difficulty: Medium
 * Topics: Arrays, Hash Table, Union Find
 * 
 * Problem:
 * Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence. Algorithm must run in O(n) time.
 * 
 * Approach:
 * Only start counting at the beginning of a sequence (i.e., when num - 1 is not in the set).
 * 
 * Key Insights:
 * 1. O(1) Membership Check: Using a set allows for O(1) average time complexity for membership checks.
 * 2. Sequence Start Identification: By only starting to count a sequence from numbers that are the beginning of a sequence 
 * (i.e., num - 1 not in set), we avoid redundant work and ensure each sequence is counted only once.
 * 
 * Edge Cases:
 * 1. Array is sorted in descending order.
 * 
 * Complexity:
 * Time: O(n) - We iterate through the array twice, and each operation in the set is O(1) on average.
 * Space: O(n) - The set stores all elements of the input array.
 */

import java.util.HashSet;
import java.util.Set;

public class LongestConsecutiveSequence {
    // Implementation
    public int longestConsecutive(int[] nums) {
        Set<Integer> numSet = new HashSet<>();
        for (int num : nums) {
            numSet.add(num);
        }

        int longestStreak = 0;

        for (int num : numSet) {
            // Only start counting if 'num' is the start of a sequence
            if (!numSet.contains(num - 1)) {
                int currentNum = num;
                int currentStreak = 1;

                while (numSet.contains(currentNum + 1)) {
                    currentNum += 1;
                    currentStreak += 1;
                }

                longestStreak = Math.max(longestStreak, currentStreak);
            }
        }

        return longestStreak;
    }
 }
