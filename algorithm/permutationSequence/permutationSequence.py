# Permutation Sequence
"""
The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
"""
class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
    	res = ''
    	nums = [x for x in range(1,n+1)]
    	comb = self.fac(n-1)
    	while len(nums)>1:
    		group = k/comb
    		k%=comb
    		if k==0:
    			group -= 1
    			k = comb
    		res += str(nums.pop(group))
    		comb/=len(nums)
    	return res + str(nums.pop())

    def fac(self, n):
    	res = 1
    	for i in range(1,n+1):
    		res*=i
    	return res
