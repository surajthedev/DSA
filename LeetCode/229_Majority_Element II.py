# Given an integer array of size n, find all elements that appear more than ⌊n / 3⌋ times.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: [3]
# Example 2:

# Input: nums = [1]
# Output: [1]
# Example 3:

# Input: nums = [1,2]
# Output: [1,2]
 

# Constraints:

# 1 <= nums.length <= 5 * 104
# -109 <= nums[i] <= 109
 






# Brute force:
class Solution:
    def majorityElement(self, nums):
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        result = []

        for num, freq in count.items():
            if freq > len(nums) // 3:
                result.append(num)

        return result








# Optimal:
class Solution:
    def majorityElement(self, nums):
        candidate1 = None
        candidate2 = None

        count1 = 0
        count2 = 0

        # Find candidates
        for num in nums:

            if num == candidate1:
                count1 += 1

            elif num == candidate2:
                count2 += 1

            elif count1 == 0:
                candidate1 = num
                count1 = 1

            elif count2 == 0:
                candidate2 = num
                count2 = 1

            else:
                count1 -= 1
                count2 -= 1

        # Verify candidates
        count1 = 0
        count2 = 0

        for num in nums:
            if num == candidate1:
                count1 += 1

            elif num == candidate2:
                count2 += 1

        result = []

        if count1 > len(nums) // 3:
            result.append(candidate1)

        if count2 > len(nums) // 3:
            result.append(candidate2)

        return result