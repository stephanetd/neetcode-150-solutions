import java.util.HashSet;
import java.util.Set;

/**
 * 217. Contains Duplicate
 * 
 * Difficulty: Easy
 * Topics: Arrays, Hashing, Sorting
 * 
 * Problem:
 * Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
 * 
 * Approach:
 * Use a set to track seen numbers as we iterate through the list. 
 * If we encounter a number that is already in the set, we return True. 
 * If we finish iterating without finding duplicates, we return False.
 * 
 * Key Insights:
 * 1. Sets provide O(1) average time complexity for lookups.
 * 2. Early exit upon finding the first duplicate improves efficiency.
 * 
 * Edge Cases:
 * 1. Empty array should return False.
 * 2. Array with one element should return False.
 * 
 * Complexity: 
 * Time: O(n) - Single pass through the array
 * Space: O(n) - Worst case stores all n elements
 */

public class ContainsDuplicate {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> seen = new HashSet<>();
        for (int num : nums) {
            if (seen.contains(num)) {
                return true;
            }
            seen.add(num);
        }
        return false;
    }

    public static void main(String[] args) {
        System.out.println("Running tests for ContainsDuplicate...");
        ContainsDuplicate sol = new ContainsDuplicate();
        System.out.println(sol.containsDuplicate(new int[]{1,2,3,1}));  // true
        System.out.println(sol.containsDuplicate(new int[]{1,2,3,4}));  // false
        System.out.println(sol.containsDuplicate(new int[]{}));  // false
        System.out.println(sol.containsDuplicate(new int[]{1}));  // false
    } 

}
