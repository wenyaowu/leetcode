# Count and Say
"""
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
"""
class Solution:
    # @param {integer} n
    # @return {string}
    def countAndSay(self, n):
    	if n==0: return ''
    	res = '1'
    	for i in range(n-1):
    		current = res[0]
    		count = 1
    		temp = ''
    		for j in range(1,len(res)):
    			if res[j]!=current:
    				temp += (str(count)+current)
    				current = res[j]
    				count = 1
    			else:
    				count += 1
    		res = temp + str(count)+current
    	return res