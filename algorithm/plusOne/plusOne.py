# Plus One
"""
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
"""

class Solution:
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
        carry = 0
        digits[-1]+=1
        for i in reversed(range(len(digits))):
            if (digits[i]+carry)==10:
                carry = 1
                digits[i]=0
            else:
                digits[i] += carry
                carry = 0
                break
        
        return digits if not carry else [1]+digits