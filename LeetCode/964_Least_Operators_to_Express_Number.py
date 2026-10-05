# Given a single positive integer x, we will write an expression of the form x (op1) x (op2) x (op3) x ... where each operator op1, op2, etc. is either addition, subtraction, multiplication, or division (+, -, *, or /). For example, with x = 3, we might write 3 * 3 / 3 + 3 - 3 which is a value of 3.

# When writing such an expression, we adhere to the following conventions:

# The division operator (/) returns rational numbers.
# There are no parentheses placed anywhere.
# We use the usual order of operations: multiplication and division happen before addition and subtraction.
# It is not allowed to use the unary negation operator (-). For example, "x - x" is a valid expression as it only uses subtraction, but "-x + x" is not because it uses negation.
# We would like to write an expression with the least number of operators such that the expression equals the given target. Return the least number of operators used.



# Example 1:

# Input: x = 3, target = 19
# Output: 5
# Explanation: 3 * 3 + 3 * 3 + 3 / 3.
# The expression contains 5 operations.
# Example 2:

# Input: x = 5, target = 501
# Output: 8
# Explanation: 5 * 5 * 5 * 5 - 5 * 5 * 5 + 5 / 5.
# The expression contains 8 operations.
# Example 3:

# Input: x = 100, target = 100000000
# Output: 3
# Explanation: 100 * 100 * 100 * 100.
# The expression contains 3 operations.


# Constraints:

# 2 <= x <= 100
# 1 <= target <= 2 * 108
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
# Brute force:
class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def dp(t):
            if t == 0:
                return 0

            if t < x:
                return min(2 * t - 1, 2 * (x - t))

            p = 1
            k = 0

            while p * x <= t:
                p *= x
                k += 1

            if p == t:
                return k

            rem = t - p

            ans = (k - 1) + 1 + dp(rem)

            diff = p * x - t

            if diff < x:
                ans = min(ans, k + 1 + 2 * diff)

            else:
                ans = min(ans, k + 1 + dp(diff))

            return ans

        return dp(target)











# Optimal:
class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        pos = 0
        neg = 0
        k = 0
        t = target

        while t:
            digit = t % x
            t //= x

            if k == 0:
                pos = digit * 2
                neg = (x - digit) * 2
            else:
                new_pos = min(
                    pos + digit * k,
                    neg + (digit + 1) * k
                )

                new_neg = min(
                    pos + (x - digit) * k,
                    neg + (x - digit - 1) * k
                )

                pos = new_pos
                neg = new_neg

            k += 1

        return min(pos, neg + k) - 1
