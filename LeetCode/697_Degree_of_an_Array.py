# Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

# Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

 

# Example 1:

# Input: nums = [1,2,2,3,1]
# Output: 2
# Explanation: 
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.
# Example 2:

# Input: nums = [1,2,2,3,1,4,2]
# Output: 6
# Explanation: 
# The degree is 3 because the element 2 is repeated 3 times.
# So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.
 

# Constraints:

# nums.length will be between 1 and 50,000.
# nums[i] will be an integer between 0 and 49,999.







# Brute Force
class Solution:
    def findShortestSubArray(self, nums):
        n = len(nums)

        degree = 0

        for x in nums:
            degree = max(degree, nums.count(x))

        ans = n

        for i in range(n):
            count = 0

            for j in range(i, n):
                if nums[j] == nums[i]:
                    count += 1

                if count == degree:
                    ans = min(ans, j - i + 1)
                    break

        return ans











# Optimal
class Solution:
    def findShortestSubArray(self, nums):
        first = {}
        last = {}
        freq = {}

        for i, x in enumerate(nums):
            if x not in first:
                first[x] = i

            last[x] = i
            freq[x] = freq.get(x, 0) + 1

        degree = max(freq.values())
        ans = len(nums)

        for x in freq:
            if freq[x] == degree:
                ans = min(ans, last[x] - first[x] + 1)

        return ans