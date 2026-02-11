"""
239. Sliding Window Maximum

Difficulty: Hard
Topics: Array, Queue, Sliding Window, Heap (Priority Queue), Monotonic Queue

Problem:
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. 
You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Approach:
Use a heap or a deque to keep track of the maximum element in the current window. As the window slides, remove elements that are out of the current window and add new elements.

Key Insights:
1. A max-heap can efficiently retrieve the maximum element, but it may require additional steps to remove outdated elements.
2. A deque can maintain the indices of elements in a way that the maximum element is always at the front, allowing for efficient updates as the window slides.

Edge Cases:
1. An array with all elements the same.
2. k equals the length of the array.

Complexity:
Time: O(nlogn) - where n is the number of elements in the array, log n due to heap operations.
Space: O(n) - for storing the heap or deque.
"""

from typing import List
from collections import deque

def maxSlidingWindow(nums: List[int], k: int) -> List[int]: 
    q = deque()
    res = []

    for idx in range(len(nums)):
        # maintain queue in descending order
        while q and q[-1] < nums[idx]:
            q.pop()
        q.append(nums[idx])

        # remove an element that is out of the current window
        if idx >= k and nums[idx - k] == q[0]:
            q.popleft()
        
        # append maximum of current window to result
        if idx >= k - 1:
            res.append(q[0])    

    return res

if __name__ == "__main__":
    # Test cases
    assert maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]
    assert maxSlidingWindow([1], 1) == [1]
    assert maxSlidingWindow([-7,-8,7,5,7,1,6,0], 4) == [7,7,7,7,7]
    assert maxSlidingWindow([9,11], 2) == [11]
    print("All test cases passed!")
