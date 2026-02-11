/**
 * 239. Sliding Window Maximum
 * Difficulty: Hard
 * Topics: Array, Queue, Sliding Window, Heap (Priority Queue), Monotonic Queue
 * 
 * Problem:
 * You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. 
 * You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.
 * 
 * Approach:
 * Use a heap or a deque to keep track of the maximum element in the current window. As the window slides, remove elements that are out of the current window and add new elements.
 * 
 * Key Insights:
 * 1. A max-heap can efficiently retrieve the maximum element, but it may require additional steps to remove outdated elements.
 * 2. A deque can maintain the indices of elements in a way that the maximum element is always at the front, allowing for efficient updates as the window slides.
 * 
 * Edge Cases:
 * 1. An array with all elements the same.
 * 2. k equals the length of the array.
 * 
 * Complexity:
 * Time: O(nlogn) - where n is the number of elements in the array, log n due to heap operations.
 * Space: O(n) - for storing the heap or deque.
 */

import java.util.*;

public class SlidingWindowMaximum {
    public static void main(String[] args) {
        // Test cases
    }

    public static int[] maxSlidingWindow(int[] nums, int k) {
        Deque<Integer> q = new ArrayDeque<>();
        List<Integer> res = new ArrayList<>();

        for (int idx = 0; idx < nums.length; idx++) {
            // maintain queue in descending order
            while (!q.isEmpty() && q.peekLast() < nums[idx]) {
                q.removeLast();
            }
            q.addLast(nums[idx]);

            // remove an element that is out of the current window
            if (idx >= k && nums[idx-k] == q.peek()) {
                q.pop();
            }

            // append maximum of current window to result
            if (idx >= k-1) {
                res.add(q.peek());
            }
        }
        return res.toArray();
}
