# Longest Common Prefix

"""
Write a function to find the longest common prefix 
string amongst an array of strings.
"""

class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
    	if not strs: return ''
    	pre = strs[0]
    	for s in strs[1:]:
    		cmp_len = min(len(pre), len(s))
    		temp = ''
    		for i in range(cmp_len):
    			if pre[i]==s[i]:
    				temp+=pre[i]
    			else:
    				break
    		pre = temp
    	return pre