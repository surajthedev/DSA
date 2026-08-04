# The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

# By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.

 

# Example 1:

# Input: n = 3, k = 3
# Output: "213"
# Example 2:

# Input: n = 4, k = 9
# Output: "2314"
# Example 3:

# Input: n = 3, k = 1
# Output: "123"
 

# Constraints:

# 1 <= n <= 9
# 1 <= k <= n!


# Brute Force:
class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        nums = [str(i) for i in range(1, n + 1)]
        used = [False] * n
        perms = []

        def backtrack(path):
            if len(path) == n:
                perms.append("".join(path))
                return

            for i in range(n):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])

                    backtrack(path)

                    path.pop()
                    used[i] = False

        backtrack([])

        return perms[k - 1]





# Optimal:
class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        nums = [str(i) for i in range(1, n + 1)]

        fact = 1
        for i in range(1, n):
            fact *= i

        k -= 1
        ans = ""

        while nums:

            index = k // fact
            ans += nums.pop(index)

            if not nums:
                break

            k %= fact
            fact //= len(nums)

        return ans