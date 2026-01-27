"""
242. Valid Anagram

Difficulty: Easy
Topics: Hashing, Sorting, String

Problem:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Approach:
Use a hash map (dictionary) to count the frequency of each character in both strings.

Key Insights:
1. If both strings have the same character frequencies, they are anagrams.
2. Hash maps provide O(1) average time complexity for lookups and updates.
3. Using a single dictionary to count frequencies for both strings can optimize space.

Edge Cases:
1. Different lengths of strings should immediately return False.
2. Empty strings are anagrams of each other.

Complexity:
Time: O(n) - Where n is the length of the strings, as we traverse each string once.
Space: O(1) - The space used by the hash map is bounded by the character set (e.g., 26 for lowercase English letters), which is constant.
"""

from collections import defaultdict, Counter

def isAnagram(s: str, t: str) -> bool:
    if len(t) != len(s):
        return False
    
    char_count = defaultdict(int)

    for char in s:
        char_count[char] += 1

    for char in t:
        char_count[char] -= 1
        if char_count[char] < 0:
            return False
        
    return True

    #return Counter(s) == Counter(t)

if __name__ == "__main__":
    print("Running tests for ContainsDuplicate...")
    assert isAnagram(None, "anagram", "nagaram") == True
    assert isAnagram(None, "rat", "car") == False
    assert isAnagram(None, "a", "ab") == False
    assert isAnagram(None, "", "") == True
    print("All tests passed.")
