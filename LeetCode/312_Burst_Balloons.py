# You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

# If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

# Return the maximum coins you can collect by bursting the balloons wisely.

 

# Example 1:

# Input: nums = [3,1,5,8]
# Output: 167
# Explanation:
# nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
# coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
# Example 2:

# Input: nums = [1,5]
# Output: 10
 

# Constraints:

# n == nums.length
# 1 <= n <= 300
# 0 <= nums[i] <= 100






# Brute force:
class Solution:
    def maxCoins(self, nums):
        def solve(arr):
            if not arr:
                return 0

            ans = 0

            for i in range(len(arr)):
                left = arr[i - 1] if i > 0 else 1
                right = arr[i + 1] if i < len(arr) - 1 else 1

                coins = left * arr[i] * right

                new_arr = arr[:i] + arr[i + 1:]

                ans = max(ans, coins + solve(new_arr))

            return ans

        return solve(nums)





# Optimal:
class Solution:
    def maxCoins(self, nums):
        nums = [1] + nums + [1]
        n = len(nums)

        dp = [[0] * n for _ in range(n)]

        # length = gap between left and right
        for length in range(2, n):
            for left in range(n - length):
                right = left + length

                for k in range(left + 1, right):
                    coins = (
                        dp[left][k]
                        + dp[k][right]
                        + nums[left] * nums[k] * nums[right]
                    )

                    dp[left][right] = max(
                        dp[left][right],
                        coins
                    )

        return dp[0][n - 1]