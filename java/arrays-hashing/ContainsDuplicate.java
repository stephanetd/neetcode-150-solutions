import java.util.HashSet;
import java.util.Set;

/**
 * 217. Contains Duplicate
 * 
 * Difficulty: Easy
 * Topics: Arrays, Hashing, Sorting
 * 
 * Time Complexity: O(n)
 * Space Complexity: O(n)
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

    public void test() {
        // Test cases
        Object[][] testCases = {
            {new int[]{1,2,3,1}, true},
            {new int[]{1,2,3,4}, false},
            {new int[]{}, false},
            {new int[]{1}, false},
        };
        
        for (int i = 0; i < testCases.length; i++) {
            Object input = testCases[i][0];
            Object expected = testCases[i][1];
            Object result = containsDuplicate((int[]) input);
            
            if (result.equals(expected)) {
                System.out.println("Test case " + (i+1) + ": PASSED");
            } else {
                System.out.println("Test case " + (i+1) + ": FAILED");
                System.out.println("  Expected: " + expected);
                System.out.println("  Got: " + result);
            }
        }
    }

    public static void main(String[] args) {
        System.out.println("Running tests for ContainsDuplicate...");
        ContainsDuplicate solution = new ContainsDuplicate();
        solution.test();
    } 

}
