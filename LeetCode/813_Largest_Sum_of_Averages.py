# You are given an integer array nums and an integer k. You can partition the array into at most k non-empty adjacent subarrays. The score of a partition is the sum of the averages of each subarray.

# Note that the partition must use every integer in nums, and that the score is not necessarily an integer.

# Return the maximum score you can achieve of all the possible partitions. Answers within 10-6 of the actual answer will be accepted.



# Example 1:

# Input: nums = [9,1,2,3,9], k = 3
# Output: 20.00000
# Explanation:
# The best choice is to partition nums into [9], [1, 2, 3], [9]. The answer is 9 + (1 + 2 + 3) / 3 + 9 = 20.
# We could have also partitioned nums into [9, 1], [2], [3, 9], for example.
# That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.
# Example 2:

# Input: nums = [1,2,3,4,5,6,7], k = 4
# Output: 20.50000


# Constraints:

# 1 <= nums.length <= 100
# 1 <= nums[i] <= 104
# 1 <= k <= nums.length
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
# Brute force:
class Solution:
    def largestSumOfAverages(self, nums, k):
        n = len(nums)

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        def avg(l, r):
            return (prefix[r] - prefix[l]) / (r - l)

        def dfs(start, groups):
            if groups == 1:
                return avg(start, n)

            ans = 0

            for end in range(start + 1, n - groups + 2):
                ans = max(
                    ans,
                    avg(start, end) + dfs(end, groups - 1)
                )

            return ans

        return dfs(0, k)









# Optimal:
class Solution:
    def largestSumOfAverages(self, nums, k):
        n = len(nums)

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        dp = [0.0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = prefix[i] / i

        for groups in range(2, k + 1):
            new_dp = [0.0] * (n + 1)

            for i in range(groups, n + 1):
                for j in range(groups - 1, i):
                    current_avg = (prefix[i] - prefix[j]) / (i - j)
                    new_dp[i] = max(
                        new_dp[i],
                        dp[j] + current_avg
                    )

            dp = new_dp

        return dp[n]
