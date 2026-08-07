# Given an integer array nums of unique elements, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]
 

# Constraints:

# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.


# Brute force:
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:

        n = len(nums)
        result = []

        for mask in range(1 << n):

            subset = []

            for i in range(n):

                # Check whether ith bit is 1
                if mask & (1 << i):
                    subset.append(nums[i])

            result.append(subset)

        return result






# Optimal:
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:

        result = []
        path = []

        def backtrack(index):

            # Current path ek valid subset hai
            result.append(path[:])

            # Har remaining element ko choose karne ki possibility
            for i in range(index, len(nums)):

                # Choose
                path.append(nums[i])

                # Next elements
                backtrack(i + 1)

                # Undo choice
                path.pop()

        backtrack(0)

        return result