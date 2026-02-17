/**
 * 20. Valid Parentheses
 * Difficulty: Easy
 * Topics: String, Stack
 * 
 * Problem:
 * Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
 * An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
 * 
 * Approach:
 * 
 * Use a stack to keep track of opening brackets. For each character in the string:
 *  If it's an opening bracket, push it onto the stack.
 *  If it's a closing bracket, check if the stack is not empty and the top of the stack is the corresponding opening bracket. If it is, pop from the stack. Otherwise, return False.
 * At the end, if the stack is empty, return True; otherwise, return False.
 * 
 * Key Insights:
 * 1. The order of brackets matters, which is why a stack is an appropriate data structure for this problem.

 * Complexity:
 * Time: O(n), where n is the length of the string, since we need to check each character once.
 * Space: O(n) in the worst case, if all characters are opening brackets, we will push all of them onto the stack.
 */

import java.util.Stack;

public class ValidParentheses {
    public static void main(String[] args) {
        // Test cases
    }

    public static boolean isValid(String s) {
        Stack<Character> st = new Stack<>();
        int n = s.length();
        for(int i=0;i<n;i++){
            char ch = s.charAt(i);
            if(ch =='(' || ch =='{' || ch == '[') st.push(ch);
            else{
                if(st.size()==0) return false;
                char top = st.pop();
                if (ch == ')' && top != '(') return false;
                if (ch == '}' && top != '{') return false;
                if (ch == ']' && top != '[') return false;
            }
        }
        return st.size()>0 ? false : true;
    }
}
