# The factorial of a positive integer n is the product of all positive integers less than or equal to n.

# For example, factorial(10) = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1.
# We make a clumsy factorial using the integers in decreasing order by swapping out the multiply operations for a fixed rotation of operations with multiply '*', divide '/', add '+', and subtract '-' in this order.

# For example, clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1.
# However, these operations are still applied using the usual order of operations of arithmetic. We do all multiplication and division steps before any addition or subtraction steps, and multiplication and division steps are processed left to right.

# Additionally, the division that we use is floor division such that 10 * 9 / 8 = 90 / 8 = 11.

# Given an integer n, return the clumsy factorial of n.



# Example 1:

# Input: n = 4
# Output: 7
# Explanation: 7 = 4 * 3 / 2 + 1
# Example 2:

# Input: n = 10
# Output: 12
# Explanation: 12 = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1


# Constraints:

# 1 <= n <= 104
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
# ### Brute Force

python
```

class Solution:
    def clumsy(self, n: int) -> int:
        nums = list(range(n, 0, -1))
        ops = ['*', '/', '+', '-']
        expression = ""

        for i, num in enumerate(nums):
            expression += str(num)
            if i < len(nums) - 1:
                expression += ops[i % 4]

        parts = []
        i = 0

        while i < len(nums):
            value = nums[i]

            if i + 1 < len(nums):
                value *= nums[i + 1]
            if i + 2 < len(nums):
                value //= nums[i + 2]

            parts.append(value)
            i += 3

        result = parts[0]
        i = 3

        while i < n:
            if (i // 3) % 2 == 1:
                result -= parts[(i // 3)]
            else:
                result += parts[(i // 3)]
            i += 3

        return result
```

### Optimal — O(1) Time, O(1) Space

python
```

class Solution:
    def clumsy(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 6
        if n == 4:
            return 7

        if n % 4 == 0:
            return n + 1
        if n % 4 == 1 or n % 4 == 2:
            return n + 2
        return n - 1
```
