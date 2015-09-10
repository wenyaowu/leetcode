# Minimum Window Substring
"""
Given a string S and a string T,
find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the emtpy string "".

If there are multiple such windows,
you are guaranteed that there will always be only one unique minimum window in S.
"""
class Solution:
    # @param {string} s
    # @param {string} t
    # @return {string}
    def minWindow(self, s, t):
        if not s:
            return ''
        head = 0 
        tail = 0
        total_count = 0 #How many valid chars have been found
        min_len = pow(2,31)-1
        substring = ''
        dict_T = {}
        dict_S = {}
        for char in t: #The dictionary count the appearence of char in t
            if char in dict_T:
                dict_T[char]+=1
            else:
                dict_T[char]=1
                dict_S[char]=0
                
        while tail<len(s):
            if s[tail] in dict_T:
                if dict_S[s[tail]]<dict_T[s[tail]]:
                    total_count+=1
                dict_S[s[tail]]+=1
            tail+=1
            
            while total_count==len(t): #start moving head
                if s[head] in dict_T:
                    if dict_S[s[head]]>dict_T[s[head]]:
                        dict_S[s[head]]-=1
                    else:
                        dict_S[s[head]]-=1
                        total_count-=1
                    if tail-head<min_len:
                        substring = s[head:tail]
                        min_len = tail-head
                head+=1
        return substring
