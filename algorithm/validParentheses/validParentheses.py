# Valid Parentheses
"""
Given a string containing just the characters
'(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order,
"()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""
class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        stack = []
        for char in s:
            if char in '([{':
                stack.append(char)
            if char in ')]}':
                try: check = stack.pop()
                except: return False #Pop from empty list
                if char == ')':
                    if check!='(': return False
                if char == ']':
                    if check!='[': return False
                if char == '}':
                    if check!='{': return False
        return True if not stack else False