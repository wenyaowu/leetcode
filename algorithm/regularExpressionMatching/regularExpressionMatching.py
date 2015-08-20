# Regular Expression Matching
"""
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
"""

class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p): # Recursive solution ----> TLE
    	if not p: return len(s)==0

    	if len(p)==1 or p[1]!='*': # Match one char
    		if len(s)==0 or (p[0]!=s[0] and p[0]!='.'): return False
    		else: self.isMatch(s[1:], p[1:])
    	else: # Match more than one char
    		i=-1
    		while i<len(s)-1 and (i<0 or s[i]==p[0] or p[0]=='.'):
    			if self.isMatch(s[i+1:],p[2:]): return True
    			i+=1
    	return False

    def isMatchDP(self, s, p):
        m, n = len(s), len(p)
        dp = [[False for x in range(n+1)] for x in range(m+1)]
        dp[0][0] = True
        for i in range(m+1):
            for j in range(1, n+1):
                if p[j-1]!='.' and p[j-1]!='*':
                    if i>0 and dp[i-1][j-1] and s[i-1]==p[j-1]:
                        dp[i][j] = True
                elif p[j-1]=='.':
                    if i>0 and dp[i-1][j-1]:
                        dp[i][j] = True
                elif j-1>0:
                    if dp[i][j-2] or dp[i][j-1]:
                        dp[i][j] = True
                    elif (i>0 and (p[j-2]==s[i-1] or p[j-2]=='.')) and dp[i-1][j]:
                        dp[i][j] = True
        return dp[m][n]