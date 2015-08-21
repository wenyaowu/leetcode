# Generate Parentheses
"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
"""
class Solution:
    # @param {integer} n
    # @return {string[]}
    # n = current left, m=current right remain
    def generateParenthesis(self, n):
    	self.res = []
    	self.helper('', 0, 0, n)
    	return self.res
    def helper(self, curr, l, r, n):
    	if l==r==n: self.res.append(curr)
    	if l>n: return
    	if l<n: self.helper(curr+'(', l+1, r, n)
    	if r<l: self.helper(curr+')', l, r+1, n)
