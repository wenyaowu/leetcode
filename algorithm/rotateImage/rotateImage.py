# Rotate Image
"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
"""
class Solution:
    def rotate(self, matrix):
    	for i in range(len(matrix)):
    		for j in range(0,i):
    			matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    	for i in range(len(matrix)):
    		matrix[i] = matrix[i][::-1]
