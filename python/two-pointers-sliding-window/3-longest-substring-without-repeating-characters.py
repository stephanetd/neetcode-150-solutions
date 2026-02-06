"""
3. Longest Substring Without Repeating Characters

Difficulty: Medium
Topics: Staff, String, Hash table, Sliding Window

Problem:
Given a string s, find the length of the longest substring without duplicate characters.

Approach:
We can use the sliding window technique with two pointers to keep track of the current substring without repeating characters. 
We will also use a hashmap to store the characters in the current window and their last position. As we expand the right pointer, we check if the character is already in the set. 
If it is, we move the left pointer to the right until we remove the duplicate character from the set. We keep track of the maximum length of the substring found during this process.

Key Insights:
1. Using a hashmap allows for O(1) average time complexity for checking duplicates.
2. The sliding window technique efficiently narrows down the search space without needing to check all possible substrings.

Edge Cases:
1. A string with all unique characters.
2. A string with all identical characters.

Complexity:
Time: O(n) - We traverse the string once with the right pointer, and the left pointer only moves forward.
Space: O(n) - In the worst case, we may need to store all characters in the hashmap if all characters are unique.
"""

def lengthOfLongestSubstring(s: str) -> int:
    char_index = {} # tuple (char, last_position) ex: at index 0 we have ('a', 0), at index 3 we have ('a', 3)
    max_length = 0
    left = 0

    for right in range(len(s)):
        char = s[right]
        if char in char_index.keys(): # char already in map -> we encounter a duplicate
            if char_index[char] >= left: # the duplicate is in the unique characters window
                left = char_index[char] + 1
        char_index[char] = right
        max_length = max(max_length, right - left + 1)
        
    return max_length

if __name__ == "__main__":
    # Test cases
    test_strings = [
        "abcabcbb",  # Expected output: 3 ("abc")
        "bbbbb",     # Expected output: 1 ("b")
        "pwwkew",    # Expected output: 3 ("wke")
        "",          # Expected output: 0
        "dvdfnaooy"       # Expected output: 6 ("vdfnao")
    ]
    for s in test_strings:
        result = lengthOfLongestSubstring(s)
        print(f"Input: '{s}' => Output: {result}")
