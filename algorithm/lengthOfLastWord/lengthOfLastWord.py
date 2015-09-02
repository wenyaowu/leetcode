# Length of last word
"""
Given a string s consists of upper/lower-case
alphabets and empty space characters ' ',
return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence
consists of non-space characters only.

For example, 
Given s = "Hello World",
return 5.
"""
class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        s= s.strip()
        result = ''
        for char in s[::-1]:
            if char!=' ':
                result+=char
            else:
                break
        return len(result)