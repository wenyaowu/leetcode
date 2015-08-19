# Zig Zag Conversion
"""
The string "PAYPALISHIRING" is written in a
zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""
class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        if not s:
            return ''
        if numRows==1:
            return s
        result = [[] for x in range(numRows)]
        row_pointer = 0
        direction = 1
        for char in s:
            result[row_pointer].append(char)
            row_pointer += direction
            if row_pointer==numRows-1:
                direction = -1
            if row_pointer==0:
                direction = 1
        output = ''
        for row in result:
            output+=''.join(row)
        return output