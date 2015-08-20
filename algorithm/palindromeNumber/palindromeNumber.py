# Palindrome Number
"""
Determine whether an integer is a palindrome. Do this without extra space.
"""
class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        return x-int(str(x)[::-1])==0