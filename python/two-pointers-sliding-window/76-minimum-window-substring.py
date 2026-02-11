"""
76. Minimum Window Substring

Difficulty: Hard
Topics: Hash Table, String, Sliding Window

Problem:
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. 
If there is no such substring, return the empty string "".

Approach:  
We use two hashmaps, one (Counter) for the character frequency of t and another (defaultdict) for the moving window for the substring in s.

Key Insights
1.

Complexity:
Time: O() - 
Space: O() - 
"""
from collections import Counter, defaultdict

def minWindow(s: str, t: str) -> str:
    if len(t) > len(s):
        return ""
    if len(t) == 0:
        return ""
    
    window, count_t = defaultdict(int), Counter(t)
    have, need = 0, len(count_t)
    res, res_len = (-1,-1), float("inf")
    l = 0
    for r in range(len(s)):
        c = s[r]
        window[c] += 1
        # Check if we have the right count of c in the window
        if c in count_t and window[c] == count_t[c]:
            have += 1
        # If we have all the characters we need
        while have == need:
            # Check if we need to update our result
            window_len = r - l + 1
            if window_len < res_len: # if we found a smaller window
                res = (l,r+1)
                res_len = window_len
            # Try to shrink the window from the left
            window[s[l]] -= 1
            if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                have -= 1
            l += 1
        
    return s[res[0]:res[1]]



if __name__ == "__main__":
    # Test cases
    assert minWindow("ADOBECODEBANC", "ABC") == "BANC"
    assert minWindow("a", "a") == "a"
    assert minWindow("aa", "aa") == "aa"
    print("All tests passed !")
