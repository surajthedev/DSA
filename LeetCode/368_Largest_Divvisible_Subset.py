# Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

# answer[i] % answer[j] == 0, or
# answer[j] % answer[i] == 0
# If there are multiple solutions, return any of them.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [1,2]
# Explanation: [1,3] is also accepted.
# Example 2:

# Input: nums = [1,2,4,8]
# Output: [1,2,4,8]
 

# Constraints:

# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 2 * 109
# All the integers in nums are unique.










# Brute force:
class Solution:
    def largestDivisibleSubset(self, nums):
        n = len(nums)

        best = []

        def is_divisible_subset(subset):
            for i in range(len(subset)):
                for j in range(i + 1, len(subset)):
                    a = subset[i]
                    b = subset[j]

                    if a % b != 0 and b % a != 0:
                        return False

            return True

        def backtrack(index, current):
            nonlocal best

            # Saare elements process ho gaye
            if index == n:
                if len(current) > len(best):
                    if is_divisible_subset(current):
                        best = current[:]
                return

            # Current element ko nahi lena
            backtrack(index + 1, current)

            # Current element ko lena
            current.append(nums[index])
            backtrack(index + 1, current)
            current.pop()

        backtrack(0, [])

        return best









# Optimal:
class Solution:
    def largestDivisibleSubset(self, nums):
        nums.sort()

        n = len(nums)

        # dp[i] = largest subset length ending at i
        dp = [1] * n

        # parent[i] = previous index in the subset
        parent = [-1] * n

        max_len = 1
        max_index = 0

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        parent[i] = j

            if dp[i] > max_len:
                max_len = dp[i]
                max_index = i

        # Reconstruct answer
        answer = []

        while max_index != -1:
            answer.append(nums[max_index])
            max_index = parent[max_index]

        answer.reverse()

        return answer