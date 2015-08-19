# Longest Palindromic Substring
"""
Given a string S, find the longest palindromic substring in S.
You may assume that the maximum length of S is 1000,
and there exists one unique longest palindromic substring.
"""

class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        T = '#'.join('${}^'.format(s))
        print T
        P = [0 for n in range(len(T))]
        C = R = 0
        for i in range(1,len(T)-1): #Do not include the edge
            P[i] = (R>i) and (min(P[2*C-i],R-i))
        
            while T[i-1-P[i]]==T[i+1+P[i]]: #Futher extend the palindrome
                P[i]+=1
        
            if i+P[i]>R: #Update new bound of R
                C, R = i, i+P[i]


        n,i = max( (v,i) for i,v in enumerate(P))
        print i, n
        return filter(lambda x: x not in '^#$',T[i-n:i+n+1]) #include the tail
