# Unique Binary Search Tree 2
"""
Given n, generate all structurally unique BST's 
(binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""
class Solution:
    # @param {integer} n
    # @return {TreeNode[]}
    def generateTrees(self, n):
        return self.helper([x for x in range(1,n+1)])
    def helper(self, nums):
        if not nums: return [None]
        res = []
        for i in range(len(nums)):
            left = self.helper(nums[:i])
            right = self.helper(nums[i+1:])
            for l in left:
                for r in right:
                    root = TreeNode(nums[i])
                    root.left = l
                    root.right = r
                    res.append(root)
        return res
