# An additive number is a string whose digits can form an additive sequence.

# A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

# Given a string containing only digits, return true if it is an additive number or false otherwise.

# Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

 

# Example 1:

# Input: "112358"
# Output: true
# Explanation: 
# The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
# 1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
# Example 2:

# Input: "199100199"
# Output: true
# Explanation: 
# The additive sequence is: 1, 99, 100, 199. 
# 1 + 99 = 100, 99 + 100 = 199
 

# Constraints:

# 1 <= num.length <= 35
# num consists only of digits.







# Brute force:
class Solution:
    def isAdditiveNumber(self, num):
        n = len(num)

        def backtrack(index, prev1, prev2, count):
            if index == n:
                return count >= 3

            # Try all possible next numbers
            for end in range(index + 1, n + 1):

                # Leading zero not allowed
                if num[index] == '0' and end > index + 1:
                    break

                curr = int(num[index:end])

                # First or second number
                if count < 2:
                    if backtrack(end, prev2, curr, count + 1):
                        return True

                else:
                    # Next number must be sum of previous two
                    if curr == prev1 + prev2:
                        if backtrack(end, prev2, curr, count + 1):
                            return True

            return False

        return backtrack(0, 0, 0, 0)






# Optimal:
class Solution:
    def isAdditiveNumber(self, num):
        n = len(num)

        def add(a, b):
            i = len(a) - 1
            j = len(b) - 1
            carry = 0
            res = []

            while i >= 0 or j >= 0 or carry:
                x = int(a[i]) if i >= 0 else 0
                y = int(b[j]) if j >= 0 else 0

                total = x + y + carry

                res.append(str(total % 10))
                carry = total // 10

                i -= 1
                j -= 1

            return ''.join(reversed(res))

        for i in range(1, n):
            # First number cannot have leading zero
            if num[0] == '0' and i > 1:
                break

            first = num[:i]

            for j in range(i + 1, n):
                # Second number cannot have leading zero
                if num[i] == '0' and j > i + 1:
                    break

                second = num[i:j]

                # IMPORTANT: reset for every new pair
                a = first
                b = second
                k = j
                count = 2

                while k < n:
                    c = add(a, b)

                    if not num.startswith(c, k):
                        break

                    k += len(c)
                    a, b = b, c
                    count += 1

                if k == n and count >= 3:
                    return True

        return False