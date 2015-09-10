# Set Matrix Zeroes
"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. 
Do it in place.
"""
class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def setZeroes(self, matrix):
    	if not matrix: return 
    	m, n = len(matrix), len(matrix[0])

    	if matrix[0][0]==0:
    		first_row = first_column = 0
    	else:
    		first_row = first_column = 1
    	

    	for i in range(1,m):
    		if matrix[i][0] == 0:
    			first_column = 0
    			break
    	for i in range(1,n):
    		if matrix[0][i] == 0:
    			first_row = 0
    			break

    	for i in range(1,m):
    		for j in range(1,n):
    			if matrix[i][j] == 0:
    				matrix[i][0] = 0
    				matrix[0][j] = 0


    	for i in range(1,m):
    		if matrix[i][0] == 0:  # Set whole row 0
    		    for j in range(n):
    		    	matrix[i][j] = 0

    	for j in range(1,n):
    		if matrix[0][j] == 0:
    			for i in range(m):
    				matrix[i][j] = 0

    	if first_row == 0:
    	   for i in range(n):
    		  matrix[0][i]=0
        if first_column == 0:
            for i in range(m):
                matrix[i][0]=0

        if not first_column or not first_row:
            matrix[0][0] = 0
