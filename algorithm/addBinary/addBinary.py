# Add Binary
"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
"""

class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        result = ''
        carry = 0
        while a or b:
            if a:
                if b:
                    result += str((int(a[-1])+int(b[-1])+carry)%2)
                    carry =  (int(a[-1])+int(b[-1])+carry)//2
                    a=a[0:-1]
                    b=b[0:-1]
                else:
                    result += str((int(a[-1])+carry)%2)
                    carry = (int(a[-1])+carry)//2
                    a=a[0:-1]
            else:
                result += str((int(b[-1])+carry)%2)
                carry = (int(b[-1])+carry)//2
                b=b[0:-1]
        if carry:
            result+='1'
        return result[::-1]   
