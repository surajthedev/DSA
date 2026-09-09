# You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

# You are given an integer array nums representing the data status of this set after the error.

# Find the number that occurs twice and the number that is missing and return them in the form of an array.

 

# Example 1:

# Input: nums = [1,2,2,4]
# Output: [2,3]
# Example 2:

# Input: nums = [1,1]
# Output: [1,2]
 

# Constraints:

# 2 <= nums.length <= 104
# 1 <= nums[i] <= 104






# Brute force:
class Solution:
    def findErrorNums(self, nums):
        n = len(nums)

        duplicate = -1
        missing = -1

        for i in range(1, n + 1):
            count = nums.count(i)

            if count == 2:
                duplicate = i
            elif count == 0:
                missing = i

        return [duplicate, missing]







# Optimal:
class Solution:
    def findErrorNums(self, nums):
        n = len(nums)
        seen = [False] * (n + 1)

        duplicate = -1

        for num in nums:
            if seen[num]:
                duplicate = num
            seen[num] = True

        for i in range(1, n + 1):
            if not seen[i]:
                missing = i
                break

        return [duplicate, missing]