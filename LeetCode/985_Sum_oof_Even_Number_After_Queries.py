# You are given an integer array nums and an array queries where queries[i] = [vali, indexi].

# For each query i, first, apply nums[indexi] = nums[indexi] + vali, then print the sum of the even values of nums.

# Return an integer array answer where answer[i] is the answer to the ith query.



# Example 1:

# Input: nums = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
# Output: [8,6,2,4]
# Explanation: At the beginning, the array is [1,2,3,4].
# After adding 1 to nums[0], the array is [2,2,3,4], and the sum of even values is 2 + 2 + 4 = 8.
# After adding -3 to nums[1], the array is [2,-1,3,4], and the sum of even values is 2 + 4 = 6.
# After adding -4 to nums[0], the array is [-2,-1,3,4], and the sum of even values is -2 + 4 = 2.
# After adding 2 to nums[3], the array is [-2,-1,3,6], and the sum of even values is -2 + 6 = 4.
# Example 2:

# Input: nums = [1], queries = [[4,0]]
# Output: [0]


# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# 1 <= queries.length <= 104
# -104 <= vali <= 104
# 0 <= indexi < nums.length
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
    def sumEvenAfterQueries(
        self,
        nums: list[int],
        queries: list[list[int]]
    ) -> list[int]:

        ans = []

        for val, index in queries:
            nums[index] += val

            even_sum = 0

            for num in nums:
                if num % 2 == 0:
                    even_sum += num

            ans.append(even_sum)

        return ans














# Optimal:
class Solution:
    def sumEvenAfterQueries(
        self,
        nums: list[int],
        queries: list[list[int]]
    ) -> list[int]:

        even_sum = sum(num for num in nums if num % 2 == 0)
        ans = []

        for val, index in queries:
            old = nums[index]

            # Remove old value if it was even
            if old % 2 == 0:
                even_sum -= old

            nums[index] += val

            # Add new value if it is even
            if nums[index] % 2 == 0:
                even_sum += nums[index]

            ans.append(even_sum)

        return ans
