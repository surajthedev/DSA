# An array nums of length n is beautiful if:

# nums is a permutation of the integers in the range [1, n].
# For every 0 <= i < j < n, there is no index k with i < k < j where 2 * nums[k] == nums[i] + nums[j].
# Given the integer n, return any beautiful array nums of length n. There will be at least one valid answer for the given n.



# Example 1:

# Input: n = 4
# Output: [2,1,4,3]
# Example 2:

# Input: n = 5
# Output: [3,1,2,5,4]


# Constraints:

# 1 <= n <= 1000
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
    def beautifulArray(self, n: int) -> list[int]:
        def valid(arr, x):
            for i in range(len(arr)):
                for j in range(i + 1, len(arr)):
                    if (arr[i] + arr[j]) % 2 == 0:
                        mid = (arr[i] + arr[j]) // 2

                        for k in range(i + 1, j):
                            if arr[k] == mid:
                                return False
            return True

        def backtrack(arr, used):
            if len(arr) == n:
                return arr[:]

            for x in range(1, n + 1):
                if not used[x]:
                    arr.append(x)
                    used[x] = True

                    if valid(arr, x):
                        result = backtrack(arr, used)
                        if result:
                            return result

                    used[x] = False
                    arr.pop()

            return None

        return backtrack([], [False] * (n + 1))














# Optimal:
class Solution:
    def beautifulArray(self, n: int) -> list[int]:
        ans = [1]

        while len(ans) < n:
            odd = [2 * x - 1 for x in ans if 2 * x - 1 <= n]
            even = [2 * x for x in ans if 2 * x <= n]

            ans = odd + even

        return ans
