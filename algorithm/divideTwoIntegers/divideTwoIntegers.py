# Divide Two Integers
"""
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
"""
class Solution:
    # @param {integer} dividend
    # @param {integer} divisor
    # @return {integer}
    def divide(self, dividend, divisor):
        isNeg = False
        if dividend<0:
            if divisor<0:
                isNeg = False
                dividend = abs(dividend)
                divisor = abs(divisor)
            elif divisor>0:
                isNeg = True
                dividend = abs(dividend)
            else:
                return pow(2,31)-1
        elif dividend>0:
            if divisor<0:
                divisor = abs(divisor)
                isNeg = True
            elif divisor==0:
                return pow(2,31)-1
        else:
            return 0
        result = 0
        original_divisor = divisor
        current_double_rate = 1
        while dividend >= divisor:
            dividend -= divisor
            result += current_double_rate
            divisor*=2
            current_double_rate *=2
            if dividend<divisor: #Restart
                divisor = original_divisor
                current_double_rate = 1
        if not isNeg and result>= (pow(2,31)-1): 
            result = pow(2,31)-1
        return -result if isNeg else result
