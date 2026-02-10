"""
567. Permutation in String

Difficulty: Medium
Topics: Principal, Hash Table, Two Pointers, String, Sliding Window

Problem:
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Approach:
Since a permutation of s1 must have the same character counts, we can use a fixed-size sliding window over s2 whose length is exactly len(s1).
We maintain two frequency arrays: one for s1 and one for the current window in s2
If these two arrays ever match, the window is a valid permutation. As we slide the window forward, we update counts by removing the left character and adding the new right character — no need to rebuild the counts each time.

Key Insights:
1. The sliding window must be exactly the length of s1 to ensure we are checking for valid permutations. A window of different size cannot be a permutation of s1.
2. When updating the frequency counts during window sliding, the matches counter must be carefully updated. A character transition from matching to non-matching should decrement matches, and vice versa.

Complexity:
Time: O(n) - where n is the length of s2, since we are sliding through s2 once and each character update is O(1)
Space: O(1) - since the frequency arrays are of fixed size 26 for lowercase letters
"""

def checkInclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False

    s1Count, s2Count = [0] * 26, [0] * 26
    for i in range(len(s1)):
        s1Count[ord(s1[i]) - ord('a')] += 1
        s2Count[ord(s2[i]) - ord('a')] += 1

    matches = 0
    for i in range(26):
        matches += (1 if s1Count[i] == s2Count[i] else 0)

    l = 0
    for r in range(len(s1), len(s2)):
        if matches == 26:
            return True

        index = ord(s2[r]) - ord('a')
        s2Count[index] += 1
        if s1Count[index] == s2Count[index]:
            matches += 1
        elif s1Count[index] + 1 == s2Count[index]:
            matches -= 1

        index = ord(s2[l]) - ord('a')
        s2Count[index] -= 1
        if s1Count[index] == s2Count[index]:
            matches += 1
        elif s1Count[index] - 1 == s2Count[index]:
            matches -= 1
        l += 1
    return matches == 26

if __name__ == "__main__":
    # Test cases
    print(checkInclusion("ab", "eidbaooo"))  # True
    print(checkInclusion("ab", "eidboaoo"))  # False
    print(checkInclusion("adc", "dcda"))  # True
