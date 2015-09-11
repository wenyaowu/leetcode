# Word Search
"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ["ABCE"],
  ["SFCS"],
  ["ADEE"]
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
"""
class Solution:
    # @param {character[][]} board
    # @param {string} word
    # @return {boolean}
    def exist(self, board, word):  
        if not word:
             return False
        if not board:
            return False
        for i in range(len(board)):
            board[i] = [x for x in board[i]]
        m,n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                print 'i:'+str(i)+' j:'+str(j)+' v:'+str(board[i][j])
                if board[i][j] == word[0]:
                    if self.helper(i, j, board, word):
                        return True
        return False

    def helper(self, i, j, b, word):
        m,n = len(b), len(b[0])
        if i>=m or i<0 or j>=n or j<0:
            return False
        else:
            if b[i][j] == word[0]:
                if len(word)==1: 
                    return True
                else:
                    b[i][j] = ""
                    if self.helper(i+1, j, b, word[1:]): return True
                    if self.helper(i-1, j, b, word[1:]): return True
                    if self.helper(i, j+1, b, word[1:]): return True
                    if self.helper(i, j-1, b, word[1:]): return True
                    return False
            else:
                return False
