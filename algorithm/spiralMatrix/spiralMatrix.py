# Spiral Matrix
"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
"""
class Solution:
    # @param {integer[][]} matrix
    # @return {integer[]}
    def spiralOrder(self, matrix):
        
        result = []
        while matrix:
            try:
                result += matrix.pop(0)
            except:
                break
            try:
                for row in matrix:
                    result += [row.pop(-1)]
            except:
                break
            try:
                result += matrix.pop(-1)[-1::-1]
            except:
                break
            try:
                for row in matrix[-1::-1]:
                    result += [row.pop(0)]
            except:
                break
        return result


                