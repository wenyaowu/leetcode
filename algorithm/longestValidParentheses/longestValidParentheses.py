# Longest Valid Parentheses
"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
"""

class Solution:
    # @param {string} s
    # @return {integer}
    def longestValidParentheses(self, s):
        if not s:return 0
        stack = [] #Used to store the INDEX of '('
        start = 0
        max_len = 0
        for ii, char in enumerate(s):
            if char == '(':
                stack.append(ii)
            if char == ')':
                if not stack:
                    start = ii+1
                else:
                    curr = stack.pop() #Index of last '('
                    if stack: #Not empty after pop()
                        max_len = max(max_len, ii-curr+1)
                    else: #stack is empty after pop()
                        max_len = max(max_len, ii-start+1)
        return max_len