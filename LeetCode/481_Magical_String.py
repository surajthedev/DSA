# A magical string s consists of only '1' and '2' and obeys the following rule:

# Concatenating the sequence of lengths of its consecutive groups of identical characters '1' and '2' generates the string s itself.
# The first few elements of s is s = "1221121221221121122……". If we group the consecutive 1's and 2's in s, it will be "1 22 11 2 1 22 1 22 11 2 11 22 ......" and counting the occurrences of 1's or 2's in each group yields the sequence "1 2 2 1 1 2 1 2 2 1 2 2 ......".

# You can see that concatenating the occurrence sequence gives us s itself.

# Given an integer n, return the number of 1's in the first n number in the magical string s.

 

# Example 1:

# Input: n = 6
# Output: 3
# Explanation: The first 6 elements of magical string s is "122112" and it contains three 1's, so return 3.
# Example 2:

# Input: n = 1
# Output: 1
 

# Constraints:

# 1 <= n <= 105








# Brute force:
class Solution:
    def magicalString(self, n):
        if n == 1:
            return 1

        s = "122"
        i = 2

        while len(s) < n:
            count = int(s[i])
            char = '1' if s[-1] == '2' else '2'

            s += char * count
            i += 1

        return s[:n].count('1')






# Optimal:
class Solution:
    def magicalString(self, n):
        if n <= 3:
            return 1 if n == 1 else 1

        s = [1, 2, 2]
        i = 2
        ones = 1

        while len(s) < n:
            char = 1 if s[-1] == 2 else 2

            for _ in range(s[i]):
                s.append(char)

                if char == 1 and len(s) <= n:
                    ones += 1

            i += 1

        return ones