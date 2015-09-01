# Group Anagrams
"""
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:
For the return value, each inner list's elements must follow the lexicographic order.
All inputs will be in lower-case.
"""
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
    	ana_d = {}
    	res = []
    	for s in strs:
    		s_key = ''.join(sorted(s))
    		if s_key not in ana_d:
    			ana_d[s_key] = [s]
    		else:
    			ana_d[s_key].append(s)
    	for i in ana_d.values():
    		res.append(sorted(i))
    	return res