# A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of length n where:

# s[i] == 'I' if perm[i] < perm[i + 1], and
# s[i] == 'D' if perm[i] > perm[i + 1].
# Given a string s, reconstruct the permutation perm and return it. If there are multiple valid permutations perm, return any of them.



# Example 1:

# Input: s = "IDID"
# Output: [0,4,1,3,2]
# Example 2:

# Input: s = "III"
# Output: [0,1,2,3]
# Example 3:

# Input: s = "DDI"
# Output: [3,2,0,1]


# Constraints:

# 1 <= s.length <= 105
# s[i] is either 'I' or 'D'.
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
class Solution:
    def findPermutation(self, s):
        n = len(s)
        nums = list(range(n + 1))

        def backtrack(index):
            if index == n:
                return nums[:]

            if s[index] == 'I':
                for i in range(index, n):
                    if nums[i] < nums[i + 1]:
                        nums[i], nums[i + 1] = nums[i + 1], nums[i]
                        result = backtrack(index + 1)
                        if result:
                            return result
                        nums[i], nums[i + 1] = nums[i + 1], nums[i]
            else:
                for i in range(index, n):
                    if nums[i] > nums[i + 1]:
                        nums[i], nums[i + 1] = nums[i + 1], nums[i]
                        result = backtrack(index + 1)
                        if result:
                            return result
                        nums[i], nums[i + 1] = nums[i + 1], nums[i]

            return None

        return backtrack(0)











# Optimal:
class Solution:
    def diStringMatch(self, s: str):
        low = 0
        high = len(s)
        ans = []

        for ch in s:
            if ch == 'I':
                ans.append(low)
                low += 1
            else:
                ans.append(high)
                high -= 1

        ans.append(low)

        return ans
