"""
49. Group Anagrams

Difficulty: Medium
Topics: Arrays, Hashing, String, HashTable

Problem:
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Approach:
Use a dictionary to map sorted strings to lists of anagrams that correspond to that sorted string.

Key Insights:
1. Anagrams have the same characters when sorted.

Edge Cases:
1. Empty strings.
2. Single character strings.

Complexity:
Time: O(m * n log n) - where m is the number of strings and n is the average length of each string.
Space: O(m * n) - for storing the grouped anagrams.
"""
from collections import defaultdict

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    anagrams = defaultdict(list)
    
    for s in strs:
        sorted_s = ''.join(sorted(s))
        anagrams[sorted_s].append(s)
    
    return list(anagrams.values())
    """
    Without using defaultdict:
    anagrams = {}
    for s in strs:
        sorted_s = ''.join(sorted(s))
        if sorted_s not in anagrams:
            anagrams[sorted_s] = []
        anagrams[sorted_s].append(s)
    return list(anagrams.values())
    """

if __name__ == "__main__":
    # Example test cases
    print("Running tests for GroupAnagrams...")
    print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))  # Expected: [["bat"],["nat","tan"],["ate","eat","tea"]]
    print(groupAnagrams([""]))  # Expected: [[""]]
    print(groupAnagrams(["a"]))  # Expected: [["a"]]