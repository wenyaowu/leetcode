# pow(x,n)
"""
Implement pow(x, n).
"""
class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPowHelper(self,x,n):
    	if n==0: return 1
    	v = self.myPowHelper(x, n/2)
    	if n%2 == 0: 
    		return v*v
    	else:
    		return v*v*x

    def myPow(self, x, n):
    	if n>0: return self.myPowHelper(x,n)
    	else: return 1.0/self.myPowHelper(x,-n)