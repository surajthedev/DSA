# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

# Example 1:

# Input: num1 = "2", num2 = "3"
# Output: "6"
# Example 2:

# Input: num1 = "123", num2 = "456"
# Output: "56088"
 

# Constraints:

# 1 <= num1.length, num2.length <= 200
# num1 and num2 consist of digits only.
# Both num1 and num2 do not contain any leading zero, except the number 0 itself.


# Brute Force:
class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        if num1 == "0" or num2 == "0":
            return "0"

        def addStrings(a, b):
            i = len(a) - 1
            j = len(b) - 1
            carry = 0
            ans = []

            while i >= 0 or j >= 0 or carry:

                x = ord(a[i]) - ord('0') if i >= 0 else 0
                y = ord(b[j]) - ord('0') if j >= 0 else 0

                total = x + y + carry

                ans.append(str(total % 10))
                carry = total // 10

                i -= 1
                j -= 1

            return "".join(ans[::-1])

        answer = "0"
        zeros = ""

        for j in range(len(num2) - 1, -1, -1):

            digit2 = ord(num2[j]) - ord('0')

            carry = 0
            part = []

            for i in range(len(num1) - 1, -1, -1):

                digit1 = ord(num1[i]) - ord('0')

                prod = digit1 * digit2 + carry

                part.append(str(prod % 10))
                carry = prod // 10

            if carry:
                part.append(str(carry))

            part = "".join(part[::-1]) + zeros

            answer = addStrings(answer, part)

            zeros += "0"

        return answer.lstrip("0") or "0"








# Optimal:
class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        if num1 == "0" or num2 == "0":
            return "0"

        n = len(num1)
        m = len(num2)

        result = [0] * (n + m)

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):

                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))

                p1 = i + j
                p2 = i + j + 1

                total = mul + result[p2]

                result[p2] = total % 10
                result[p1] += total // 10

        ans = []

        for num in result:
            if not (len(ans) == 0 and num == 0):
                ans.append(str(num))

        return "".join(ans)