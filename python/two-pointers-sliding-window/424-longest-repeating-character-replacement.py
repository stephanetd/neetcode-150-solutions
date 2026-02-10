"""
424. Longest Repeating Character Replacement

Difficulty: Medium
Topics: String, Hash Table, Sliding Window

Problem:
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.

Approach:
Using sliding window, checked window length with the max frequency, if greater then increase the left pointer, to find is it the best substring or not.

Key Insights:
1. We can use a sliding window to keep track of the longest substring with the same character.
2. We need to keep track of the frequency of characters in the current window to determine how many characters we need to replace to make all characters the same.

Edge Cases:
1. A string with all identical characters.
2. A string with all unique characters.

Complexity:
Time: O(n) - We traverse the string once with the right pointer, and the left pointer only moves forward.
Space: O(1) - We use a hashmap to store the frequency of characters in the current window, which can grow up to O(26) for uppercase English letters, so it is O(1) in terms of space complexity.
"""

def characterReplacement(s: str, k: int) -> int:
    freq = {}
    max_freq, max_length = 0, 0
    left = 0

    for right in range(len(s)):
        char = s[right]
        freq[char] = freq.get(char, 0) + 1
        window_length = right - left + 1
        max_freq = max(max_freq, freq[char])
        if window_length - max_freq > k:
            freq[s[left]] -= 1
            left += 1
        else:
            max_length = max(max_length, window_length)

if __name__ == "__main__":
    # Test cases
    print(characterReplacement("ABAB", 2))  # Output: 4
    print(characterReplacement("AABABBA", 1))  # Output: 4
    print(characterReplacement("AAAA", 2))  # Output: 4
