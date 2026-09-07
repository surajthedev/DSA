# Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

 

# Example 1:

# Input: nums = [2,2,3,4]
# Output: 3
# Explanation: Valid combinations are: 
# 2,3,4 (using the first 2)
# 2,3,4 (using the second 2)
# 2,2,3
# Example 2:

# Input: nums = [4,2,3,4]
# Output: 4
 

# Constraints:

# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 1000







# Brute force:
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    a, b, c = nums[i], nums[j], nums[k]

                    if a + b > c and a + c > b and b + c > a:
                        count += 1

        return count






# Optimal:
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        count = 0

        for k in range(n - 1, 1, -1):
            i = 0
            j = k - 1

            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    count += j - i
                    j -= 1
                else:
                    i += 1

        return count