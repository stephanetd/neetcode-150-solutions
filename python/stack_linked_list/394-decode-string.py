"""
394. Decode String

Difficulty: Medium
Topics: String, Stack, Recursion

Problem:
Given an encoded string, return its decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. 
Note that k is guaranteed to be a positive integer between 1 and 300.

Approach:
Use a stack to keep track of the current string and the number of times it should be repeated.
Iterate through the string character by character:
- If the character is a digit, update the current number.
- If the character is a closing bracket ']', pop characters from stack until '[' is found to build the substring
    Pop digits before [ to get the repetition count k. Repeat the substring k times and push it back onto the stack.
Join all elements in the stack to form the decoded string.

Key Insights:
1. While popping characters, they come out in reverse order, so we rebuild strings by adding popped characters to the front.

Complexity:
Time: O(n) - We traverse the string once
Space: O(n) - Size of the stack which in the worst case contains all the elements of s
"""

def decodeString(s: str) -> str:
    # Base case: empty string
    if s == "": 
        return ""
    stack = []

    for i in range(len(s)):
        # Keep adding to Stack until a ']'
        if s[i] != "]":
            stack.append(s[i])
        else:
            substr = ""
            # Extracting SubString to be Multiplied
            while stack[-1] != "[":
                substr = stack.pop() + substr
            # Pop to remove '['
            stack.pop()

            k = ""
            # Extract full number (handles multi-digit, e.g. 10)
            while stack and stack[-1].isdigit():
                k = stack.pop() + k
            # Updating Stack with multiplied string
            stack.append(int(k)*substr)
    
    return "".join(stack)

if __name__ == "__main__":
    # Test cases
    assert(decodeString("3[a]2[bc]") == "aaabcbc")  # Output: "aaabcbc"
    assert(decodeString("3[a2[c]]") == "accaccacc")   # Output: "accaccacc
    assert(decodeString("12[abc]3[cd]ef") == "abcabcabcabcabcabcabcabcabcabcabcabccdcdcdef")  # Output: "abcabcabcabcabcabcabcabcabcabcabcabccdcdcdef"
    print("All test cases passed !")