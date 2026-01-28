"""
347. Top K Frequent Elements

Difficulty: Medium
Topics: Array, HashTable, Heap, Divide and Conquer, Sorting, Bucket Sort, Counting, Quickselect

Problem:
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Approach:
Use a hash table to count the frequency of each element, then use a heap or bucket sort to find the k most frequent elements.

Key Insights:
1. Counting frequencies allows efficient retrieval of the most common elements.
2. A max-heap or bucket sort can efficiently extract the top k elements.

Edge Cases:
1. All elements are the same.
2. k equals the number of unique elements.

Complexity:
Time: O(n log n) - where n is the number of unique elements.
Space: O(n) - for storing the frequency map and heap.
"""

import heapq
from collections import Counter


def topKFrequent(nums: list[int], k: int) -> list[int]:
    # Count the frequency of each element
    frequency = {}
    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1
    
    # Use a heapq.nlargest to find the k most frequent elements in one line
    # return [item for item, count in heapq.nlargest(k, frequency.items(), key=lambda x: x[1])]

    max_heap = []
    for num, count in frequency.items():
        heapq.heappush(max_heap, (-count, num))
    
    res = []
    for _ in range(k):
        res.append(heapq.heappop(max_heap)[1])
    return res


# Bucket Sort Approach (less efficient)
def topKFrequent(nums: list[int], k: int) -> list[int]:
    frequency = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]

    for num, freq in frequency.items():
        buckets[freq].append(num)
    
    res = []
    for bucket in reversed(buckets):
        for num in bucket:
            res.append(num)
            if len(res) == k:
                return res

if __name__ == "__main__":
    print("Running tests for TopKFrequent...")
    assert topKFrequent([1,1,1,2,2,3], 2) == [1, 2]
    assert topKFrequent([1], 1) == [1]
    assert topKFrequent([4,4,4,4], 1) == [4]
    assert topKFrequent([1,2,3,4,5], 5) == [1,2,3,4,5]  # or any 5 unique elements
    print("All tests passed!")