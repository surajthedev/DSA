# Given an integer array nums, return all the different possible non-decreasing subsequences of the given array with at least two elements. You may return the answer in any order.

 

# Example 1:

# Input: nums = [4,6,7,7]
# Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
# Example 2:

# Input: nums = [4,4,3,2,1]
# Output: [[4,4]]
 

# Constraints:

# 1 <= nums.length <= 15
# -100 <= nums[i] <= 100







# Brute force:
class Solution:
    def findSubsequences(self, nums):
        n = len(nums)
        result = set()

        for mask in range(1 << n):
            subseq = []

            for i in range(n):
                if mask & (1 << i):
                    if not subseq or subseq[-1] <= nums[i]:
                        subseq.append(nums[i])
                    else:
                        break

            if len(subseq) >= 2:
                result.add(tuple(subseq))

        return [list(x) for x in result]







# Optimal:
class Solution:
    def findSubsequences(self, nums):
        result = []

        def backtrack(start, path):
            if len(path) >= 2:
                result.append(path[:])

            used = set()

            for i in range(start, len(nums)):
                if nums[i] in used:
                    continue

                if path and nums[i] < path[-1]:
                    continue

                used.add(nums[i])
                path.append(nums[i])

                backtrack(i + 1, path)

                path.pop()

        backtrack(0, [])

        return result