# Given two integers a and b, return any string s such that:

# s has length a + b and contains exactly a 'a' letters, and exactly b 'b' letters,
# The substring 'aaa' does not occur in s, and
# The substring 'bbb' does not occur in s.


# Example 1:

# Input: a = 1, b = 2
# Output: "abb"
# Explanation: "abb", "bab" and "bba" are all correct answers.
# Example 2:

# Input: a = 4, b = 1
# Output: "aabaa"


# Constraints:

# 0 <= a, b <= 100
# It is guaranteed such an s exists for the given a and b.
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
    def strWithout3a3b(self, a: int, b: int) -> str:
        def backtrack(a, b, s):
            if a == 0 and b == 0:
                return s

            if a > 0 and not s.endswith("aa"):
                ans = backtrack(a - 1, b, s + "a")
                if ans:
                    return ans

            if b > 0 and not s.endswith("bb"):
                ans = backtrack(a, b - 1, s + "b")
                if ans:
                    return ans

            return None

        return backtrack(a, b, "")











# Optimal:
class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        ans = []

        while a or b:
            if a > b:
                if a >= 2:
                    ans.append("aa")
                    a -= 2
                else:
                    ans.append("a")
                    a -= 1

                if b:
                    ans.append("b")
                    b -= 1

            elif b > a:
                if b >= 2:
                    ans.append("bb")
                    b -= 2
                else:
                    ans.append("b")
                    b -= 1

                if a:
                    ans.append("a")
                    a -= 1

            else:
                if a:
                    ans.append("a")
                    a -= 1

                if b:
                    ans.append("b")
                    b -= 1

        return "".join(ans)
