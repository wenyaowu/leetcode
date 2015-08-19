# Longest Substring Without Repeating Characters
"""
Given a string, find the length of the longest substring
without repeating characters.

For example, the longest substring without repeating
letters for "abcabcbb" is "abc", which the length is 3.

For "bbbbb" the longest substring is "b", with the length of 1.
  h       i
0 1 2 3 4 5 
"""
        
class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
    	if not s: return 0
    	char_d = {}
    	head = 0 # Head of current substring
    	max_len = 0
    	for ii, char in enumerate(s):
    		if char in char_d and char_d[char]>=head:
    			max_len = max(max_len, ii-head)
    			head = char_d[char]+1
    		char_d[char] = ii
    	max_len = max(max_len, len(s)-head)
    	return max_len