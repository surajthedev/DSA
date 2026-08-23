# Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

 

# Example 1:

# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
# Example 2:

# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
# Example 3:

# Input: num = "10", k = 2
# Output: "0"
# Explanation: Remove all the digits from the number and it is left with nothing which is 0.
 

# Constraints:

# 1 <= k <= num.length <= 105
# num consists of only digits.
# num does not have any leading zeros except for the zero itself.





# Brute force:
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        def solve(s, k):
            # Agar koi digit remove nahi karni
            if k == 0:
                return s.lstrip('0') or '0'

            # Agar saare digits remove karne hain
            if len(s) == k:
                return "0"

            smallest = None

            # Har possible digit ko remove karke try karo
            for i in range(len(s)):
                new_num = s[:i] + s[i + 1:]

                candidate = solve(new_num, k - 1)

                if smallest is None or int(candidate) < int(smallest):
                    smallest = candidate

            return smallest

        return solve(num, k)






# Optimal:
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        stack = []

        for digit in num:

            # Agar previous digit current digit se bada hai,
            # toh previous digit remove karna better hai.
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1

            stack.append(digit)

        # Agar abhi bhi k digits remove karni hain,
        # toh end se remove karo.
        if k > 0:
            stack = stack[:-k]

        # Leading zeros remove karo
        result = ''.join(stack).lstrip('0')

        # Agar empty ho gaya toh "0"
        return result if result else "0"