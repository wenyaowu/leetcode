# Letter Combination of a phone number
"""
Given a digit string, return all possible letter
combinations that the number could represent.

A mapping of digit to letters
(just like on the telephone buttons) is given below.


Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""
class Solution:
    # @param {string} digits
    # @return {string[]}    
    def letterCombinations(self, digits):
    	if not digits: return []
    	self.d = {
    	'2':'abc',
    	'3':'def',
    	'4':'ghi',
    	'5':'jkl',
    	'6':'mno',
    	'7':'pqrs',
    	'8':'tuv',
    	'9':'wxyz'}
    	digits = filter(lambda x: x in '23456789', digits)
    	res = self.helper(digits)
    	return res

    def helper(self, digits):
    	if not digits: return ['']
    	res = []
    	current = digits[0]

    	subsets = self.helper(digits[1:])

    	for subset in subsets:
    		for c in self.d[current]:
    			res.append(c+subset)
    	return res
