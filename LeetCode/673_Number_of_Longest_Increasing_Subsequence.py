# Given an integer array nums, return the number of longest increasing subsequences.

# Notice that the sequence has to be strictly increasing.

 

# Example 1:

# Input: nums = [1,3,5,4,7]
# Output: 2
# Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
# Example 2:

# Input: nums = [2,2,2,2,2]
# Output: 5
# Explanation: The length of the longest increasing subsequence is 1, and there are 5 increasing subsequences of length 1, so output 5.
 

# Constraints:

# 1 <= nums.length <= 2000
# -106 <= nums[i] <= 106
# The answer is guaranteed to fit inside a 32-bit integer.








# Brute force:
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]

            max_len = 1
            count = 1

            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    length, ways = dfs(j)
                    length += 1

                    if length > max_len:
                        max_len = length
                        count = ways
                    elif length == max_len:
                        count += ways

            memo[i] = (max_len, count)
            return memo[i]

        best_len = 0
        answer = 0

        for i in range(n):
            length, count = dfs(i)

            if length > best_len:
                best_len = length
                answer = count
            elif length == best_len:
                answer += count

        return answer





# Optimal:
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        length = [1] * n
        count = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = count[j]
                    elif length[j] + 1 == length[i]:
                        count[i] += count[j]

        max_len = max(length)
        return sum(count[i] for i in range(n) if length[i] == max_len)