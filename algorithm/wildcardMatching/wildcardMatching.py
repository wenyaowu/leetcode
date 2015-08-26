# Wildcard Matching
"""
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
"""
class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
    	s_pointer = 0
    	p_pointer = 0
    	star = -1
    	match = 0
    	while s_pointer<len(s):
    		if p_pointer<len(p) and (p[p_pointer]==s[s_pointer] or p[p_pointer]=='?'):
    			p_pointer+=1
    			s_pointer+=1
    		elif p_pointer<len(p) and p[p_pointer]=='*': #If there's a start, update
    			star = p_pointer
    			match = s_pointer
    			p_pointer+=1
    		elif star!=-1:
    			p_pointer = star+1
    			match+=1
    			s_pointer = match
    		else: return False
    	while p_pointer<len(p) and p[p_pointer]=='*': p_pointer+=1

    	return p_pointer==len(p)
