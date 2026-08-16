# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?

 

# Example 1:

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:

# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
 

# Constraints:

# 1 <= k <= nums.length <= 105
# -104 <= nums[i] <= 104




# Brute force:
class Solution:
    def findKthLargest(self, nums, k):
        n = len(nums)

        for x in nums:
            greater = 0

            for y in nums:
                if y > x:
                    greater += 1

            if greater == k - 1:
                return x








# Optimal:
class Solution:
    def findKthLargest(self, nums, k):
        count = [0] * 20001

        # Frequency count
        for num in nums:
            count[num + 10000] += 1

        # Largest se traverse karo
        for i in range(20000, -1, -1):
            k -= count[i]

            if k <= 0:
                return i - 10000