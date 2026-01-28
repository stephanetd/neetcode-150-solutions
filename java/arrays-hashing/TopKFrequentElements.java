import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

/**
 * 347. Top K Frequent Elements
 * 
 * Difficulty: Medium
 * Topics: Array, HashTable, Heap, Divide and Conquer, Sorting, Bucket Sort, Counting, Quickselect
 * 
 * Problem:
 * Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
 * 
 * Approach:
 * Use a hash table to count the frequency of each element, then use a heap or bucket sort to find the k most frequent elements.
 * 
 * Key Insights:
 * 1. Counting frequencies allows efficient retrieval of the most common elements.
 * 2. A max-heap or bucket sort can efficiently extract the top k elements.
 * 
 * Edge Cases:
 * 1. All elements are the same.
 * 
 * Complexity:
 * Time: O(n log n) - where n in the number of unique elements
 * Space: O(n) - for storing the frequency map and heap
 */

public class TopKFrequentElements {
    // Implementation
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> frequency = new HashMap<>();
        for (int num : nums) {
            frequency.put(num, frequency.getOrDefault(num, 0) + 1);
        }

        PriorityQueue<int[]> maxHeap = new PriorityQueue<>((a, b) -> b[1] - a[1]);
        for (Map.Entry<Integer, Integer> entry : frequency.entrySet()) {
            maxHeap.offer(new int[]{entry.getKey(), entry.getValue()});
        }

        int[] res = new int[k];
        for (int i = 0; i < k; i++) {
            res[i] = maxHeap.poll()[0];
        }
        return res;
    }

    public static void main(String[] args) {
        // Example test cases
        System.out.println("Running tests for TopKFrequentElements...");
        TopKFrequentElements tkfe = new TopKFrequentElements();
        int[] result1 = tkfe.topKFrequent(new int[]{1,1,1,2,2,3}, 2);
        System.out.println(java.util.Arrays.toString(result1)); // Expected: [1, 2]
        int[] result2 = tkfe.topKFrequent(new int[]{1}, 1);
        System.out.println(java.util.Arrays.toString(result2)); // Expected: [1]
        int[] result3 = tkfe.topKFrequent(new int[]{4,4,4,4}, 1);
        System.out.println(java.util.Arrays.toString(result3)); // Expected: [4]
        int[] result4 = tkfe.topKFrequent(new int[]{1,2,3,4,5}, 5);
        System.out.println(java.util.Arrays.toString(result4)); // Expected: [1,2,3,4,5] or any 5 unique elements
    }
}
