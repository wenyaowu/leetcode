# Valid Sudoku
"""
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, 
where empty cells are filled with the character '.'.
"""

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Check Row and Column
        if not board: return False
        for n in range(len(board)):
        	# nth Row
        	temp = filter(lambda x: x in '123456789', board[n])
        	temp = [x for x in temp]
        	if len(set(temp)) != len(temp): return False
        	# nth Column
        	temp = filter(lambda x: x in '123456789', [row[n] for row in board])
        	if len(set(temp)) != len(temp): return False
        # Check Square
        for i in range(0,3):
        	t = [r for r in board[i*3:i*3+3]]
        	for j in range(0,3):
        		p = [x[j*3:j*3+3] for x in t]
        		temp = [x for x in ''.join(p)]
        		temp = filter(lambda x: x in '123456789', temp)
        		if len(set(temp)) != len(temp): return False
        return True
