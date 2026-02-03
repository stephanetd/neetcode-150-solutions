"""
125. Valid Palindrome

Difficulty: Easy
Topics: Two Pointers, String

Problem:
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Approach:
Clean the string by removing all non-alphanumeric characters and converting it to lowercase. 
Use two pointers to compare characters from the start and end of the cleaned string moving towards the center.

Key Insights:
1. Using two pointers allows for efficient comparison from both ends of the string.

Edge Cases:
1. An empty string is considered a palindrome.

Complexity:
Time: O(n) - where n is the length of the input string, since we process each character once.
Space: O(n) - for storing the cleaned string.
"""

def isPalindrome(s: str) -> bool:
    """ Cleaning the string at the beginning
    s = ''.join(c.lower() for c in s if c.isalnum())    
    left = 0
    right = len(s)-1

    while left <= right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True"""
    # Cleaning the string on the fly
    left = 0
    right = len(s) - 1
    while left < right:
        if not s[left].isalnum():
            left += 1
            continue
        if not s[right].isalnum():
            right -= 1
            continue
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True

if __name__ == "__main__":
    # Test cases
    pass
