# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

 

# Example 1:

# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]
 

# Constraints:

# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
 


# Brute Force:
class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        all_subsets = []

        def backtrack(index, current):
            if index == len(nums):
                all_subsets.append(tuple(current))
                return

            # Don't take nums[index]
            backtrack(index + 1, current)

            # Take nums[index]
            current.append(nums[index])
            backtrack(index + 1, current)
            current.pop()

        backtrack(0, [])

        # Remove duplicates
        return [list(x) for x in set(all_subsets)]




# Optimal:
class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        result = []

        def backtrack(start, current):
            result.append(current[:])

            for i in range(start, len(nums)):

                # Skip duplicates at the same recursion level
                if i > start and nums[i] == nums[i - 1]:
                    continue

                current.append(nums[i])

                backtrack(i + 1, current)

                current.pop()

        backtrack(0, [])

        return result