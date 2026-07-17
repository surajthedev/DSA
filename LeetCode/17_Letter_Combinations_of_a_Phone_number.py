# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:

# Input: digits = "2"
# Output: ["a","b","c"]
 

# Constraints:

# 1 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].


# Brute Force:
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        phone = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        ans = [""]

        for digit in digits:
            temp = []

            for s in ans:
                for ch in phone[digit]:
                    temp.append(s + ch)

            ans = temp

        return ans




# Optimal:
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        phone = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        ans = []

        def dfs(index, path):

            if index == len(digits):
                ans.append(path)
                return

            for ch in phone[digits[index]]:
                dfs(index + 1, path + ch)

        dfs(0, "")

        return ans