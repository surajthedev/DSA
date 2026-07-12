# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
# 
# P   A   H   N
# A P L S I I G
# Y   I   R
# 
# And then read line by line: "PAHNAPLSIIGYIR"
# 
# Write the code that will take a string and make this conversion given a number of rows:
# string convert(string s, int numRows);
# 
# Example 1:
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# 
# Example 2:
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# 
# Example 3:
# Input: s = "A", numRows = 1
# Output: "A"
# 
# Constraints:
# 1 <= s.length <= 1000
# s consists of English letters (lower-case and upper-case), ',' and '.'.
# 1 <= numRows <= 1000

# Brute Force Solution
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
            
        rows = [[] for _ in range(numRows)]
        curr_row = 0
        going_down = False
        
        for char in s:
            rows[curr_row].append(char)
            if curr_row == 0 or curr_row == numRows - 1:
                going_down = not going_down
            curr_row += 1 if going_down else -1
            
        return ''.join(''.join(row) for row in rows)

# Optimal Solution
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
            
        res = []
        cycle_len = 2 * numRows - 2
        
        for i in range(numRows):
            for j in range(0, len(s) - i, cycle_len):
                res.append(s[j + i])
                if i != 0 and i != numRows - 1 and j + cycle_len - i < len(s):
                    res.append(s[j + cycle_len - i])
                    
        return ''.join(res)
