# Substring with Concatenation of All Words
"""
You are given a string, s, and a list of words, words,
that are all of the same length. Find all starting indices
of substring(s) in s that is a concatenation of each word in
words exactly once and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).

0 1 2 3 4 5
L = 2
N = 6
"""
class Solution:
    # @param {string} s
    # @param {string[]} words
    # @return {integer[]}
    def findSubstring(self, s, words):
    	res = []
    	if not s or not words: return res
    	
    	w_dict = {} # Word Dictionary, to record word in words
    	for word in words: # Initialization
    		if word in w_dict: w_dict[word]+=1
    		else: w_dict[word] = 1

    	step = len(words[0])
    	L = len(words)
    	N = len(s)

    	for i in range(step):
    		count = 0
    		c_dict = {} # Record current words appearence in substring
    		head = i
    		for j in range(i, N-step+1, step):
    			temp = s[j:j+step]
    			if temp in w_dict:
    				if temp in c_dict: c_dict[temp]+=1
    				else: c_dict[temp]=1

    				if c_dict[temp]<=w_dict[temp]: count+=1
    				else: # Exceed
    					while c_dict[temp]>w_dict[temp]:
    						temp2 = s[head:head+step]
    						if temp2 in c_dict:
    							if c_dict[temp2]<=w_dict[temp2]: count-=1
    							c_dict[temp2]-=1
    						head+=step

    				if count==L:
    					res.append(head)
    					temp = s[head:head+step]
    					c_dict[temp]-=1
    					count-=1
    					head+=step

    			else: # Word not in words, restart the substring
    				count = 0
    				head = j+step
    				c_dict = {}
    	return res
