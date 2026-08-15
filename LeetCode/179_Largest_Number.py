# Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

# Since the result may be very large, so you need to return a string instead of an integer.

 

# Example 1:

# Input: nums = [10,2]
# Output: "210"
# Example 2:

# Input: nums = [3,30,34,5,9]
# Output: "9534330"
 

# Constraints:

# 1 <= nums.length <= 100
# 0 <= nums[i] <= 109





# Brute force:
from itertools import permutations

class Solution:
    def largestNumber(self, nums):
        best = ""

        for perm in permutations(nums):
            current = ''.join(map(str, perm))

            if current > best:
                best = current

        # Special case: [0, 0] -> "0"
        return best.lstrip('0') or '0'









# Optimal:
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums):
        nums = list(map(str, nums))

        def compare(a, b):
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0

        nums.sort(key=cmp_to_key(compare))

        result = ''.join(nums)

        # Example: [0, 0, 0] -> "0"
        return '0' if result[0] == '0' else result