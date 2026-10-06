# Given two integers n and k, return an array of all the integers of length n where the difference between every two consecutive digits is k. You may return the answer in any order.

# Note that the integers should not have leading zeros. Integers as 02 and 043 are not allowed.



# Example 1:

# Input: n = 3, k = 7
# Output: [181,292,707,818,929]
# Explanation: Note that 070 is not a valid number, because it has leading zeroes.
# Example 2:

# Input: n = 2, k = 1
# Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]


# Constraints:

# 2 <= n <= 9
# 0 <= k <= 9
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # Brute Force
# Time: O(9 * 10^(n-1) * n)
# Space: O(1) excluding output

class Solution:
    def numsSameConsecDiff(self, n, k):
        ans = []

        start = 10 ** (n - 1)
        end = 10 ** n

        for num in range(start, end):
            s = str(num)

            valid = True

            for i in range(1, n):
                if abs(int(s[i]) - int(s[i - 1])) != k:
                    valid = False
                    break

            if valid:
                ans.append(num)

        return ans














# Optimal - DFS
# Time: O(2^n)
# Space: O(n) recursion stack

class Solution:
    def numsSameConsecDiff(self, n, k):
        ans = []

        def dfs(num, length):
            if length == n:
                ans.append(num)
                return

            last = num % 10

            if last + k <= 9:
                dfs(num * 10 + last + k, length + 1)

            if k != 0 and last - k >= 0:
                dfs(num * 10 + last - k, length + 1)

        for digit in range(1, 10):
            dfs(digit, 1)

        return ans
