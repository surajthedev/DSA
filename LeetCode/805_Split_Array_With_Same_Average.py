# You are given an integer array nums.

# You should move each element of nums into one of the two arrays A and B such that A and B are non-empty, and average(A) == average(B).

# Return true if it is possible to achieve that and false otherwise.

# Note that for an array arr, average(arr) is the sum of all the elements of arr over the length of arr.

 

# Example 1:

# Input: nums = [1,2,3,4,5,6,7,8]
# Output: true
# Explanation: We can split the array into [1,4,5,8] and [2,3,6,7], and both of them have an average of 4.5.
# Example 2:

# Input: nums = [3,1]
# Output: false
 

# Constraints:

# 1 <= nums.length <= 30
# 0 <= nums[i] <= 104













# Brute Force - Backtracking

class Solution:
    def splitArraySameAverage(self, nums):
        n = len(nums)
        total = sum(nums)

        def dfs(i, count, curr_sum):
            if count > 0 and count < n:
                if curr_sum * n == total * count:
                    return True

            if i == n or count >= n:
                return False

            if dfs(i + 1, count + 1, curr_sum + nums[i]):
                return True

            if dfs(i + 1, count, curr_sum):
                return True

            return False

        return dfs(0, 0, 0)












# Optimal - DP / Bitset

class Solution:
    def splitArraySameAverage(self, nums):
        n = len(nums)
        total = sum(nums)

        dp = [0] * (n + 1)
        dp[0] = 1

        for num in nums:
            for count in range(n, 0, -1):
                dp[count] |= dp[count - 1] << num

        for count in range(1, n):
            if total * count % n == 0:
                target = total * count // n

                if (dp[count] >> target) & 1:
                    return True

        return False