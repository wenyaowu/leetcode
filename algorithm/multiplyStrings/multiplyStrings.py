# Multiply Strings
"""
Given two numbers represented as strings,
return multiplication of the numbers as a string.

Note: The numbers can be arbitrarily large and are non-negative.
"""
class Solution:
    # @param {string} num1
    # @param {string} num2
    # @return {string}
    def multiply(self, num1, num2):
        result = 0
        for ii, digit1 in enumerate(num1[::-1]):
            for jj, digit2 in enumerate(num2[::-1]):
                result+= int(digit1)*(10**ii) * int(digit2)*(10**jj)
        return str(result)