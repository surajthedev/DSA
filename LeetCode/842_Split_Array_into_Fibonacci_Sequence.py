# You are given a string of digits num, such as "123456579". We can split it into a Fibonacci-like sequence [123, 456, 579].

# Formally, a Fibonacci-like sequence is a list f of non-negative integers such that:

# 0 <= f[i] < 231, (that is, each integer fits in a 32-bit signed integer type),
# f.length >= 3, and
# f[i] + f[i + 1] == f[i + 2] for all 0 <= i < f.length - 2.
# Note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if the piece is the number 0 itself.

# Return any Fibonacci-like sequence split from num, or return [] if it cannot be done.



# Example 1:

# Input: num = "1101111"
# Output: [11,0,11,11]
# Explanation: The output [110, 1, 111] would also be accepted.
# Example 2:

# Input: num = "112358130"
# Output: []
# Explanation: The task is impossible.
# Example 3:

# Input: num = "0123"
# Output: []
# Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not valid.


# Constraints:

# 1 <= num.length <= 200
# num contains only digits.
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
# Brute force:
class Solution:
    def splitIntoFibonacci(self, num: str) -> list[int]:
        n = len(num)

        for i in range(1, n):
            if num[0] == '0' and i > 1:
                break

            a = int(num[:i])
            if a >= 2**31:
                break

            for j in range(i + 1, n):
                if num[i] == '0' and j > i + 1:
                    break

                b = int(num[i:j])
                if b >= 2**31:
                    break

                seq = [a, b]
                k = j

                while k < n:
                    c = seq[-1] + seq[-2]

                    if c >= 2**31:
                        break

                    s = str(c)

                    if not num.startswith(s, k):
                        break

                    seq.append(c)
                    k += len(s)

                if k == n and len(seq) >= 3:
                    return seq

        return []










# Optimal:
class Solution:
    def splitIntoFibonacci(self, num: str) -> list[int]:
        n = len(num)
        ans = []
        LIMIT = 2**31 - 1

        def backtrack(index):
            if index == n:
                return len(ans) >= 3

            value = 0

            for end in range(index, n):
                if end > index and num[index] == '0':
                    break

                value = value * 10 + int(num[end])

                if value > LIMIT:
                    break

                if len(ans) >= 2:
                    target = ans[-1] + ans[-2]

                    if value < target:
                        continue

                    if value > target:
                        break

                ans.append(value)

                if backtrack(end + 1):
                    return True

                ans.pop()

            return False

        if backtrack(0):
            return ans

        return []
