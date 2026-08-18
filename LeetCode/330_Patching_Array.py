# Given a sorted integer array nums and an integer n, add/patch elements to the array such that any number in the range [1, n] inclusive can be formed by the sum of some elements in the array.

# Return the minimum number of patches required.

 

# Example 1:

# Input: nums = [1,3], n = 6
# Output: 1
# Explanation:
# Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
# Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
# Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
# So we only need 1 patch.
# Example 2:

# Input: nums = [1,5,10], n = 20
# Output: 2
# Explanation: The two patches can be [2, 4].
# Example 3:

# Input: nums = [1,2,2], n = 5
# Output: 0
 

# Constraints:

# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 104
# nums is sorted in ascending order.
# 1 <= n <= 231 - 1




# Brute force:
class Solution:
    def minPatches(self, nums, n):
        nums = nums[:]
        patches = 0

        while True:
            possible = {0}

            # Generate all subset sums
            for num in nums:
                new_sums = set()

                for s in possible:
                    if s + num <= n:
                        new_sums.add(s + num)

                possible.update(new_sums)

            # Find first missing number
            missing = -1

            for x in range(1, n + 1):
                if x not in possible:
                    missing = x
                    break

            # Everything is covered
            if missing == -1:
                return patches

            # Add missing number
            nums.append(missing)
            patches += 1





# Optimal:
class Solution:
    def minPatches(self, nums, n):
        miss = 1
        i = 0
        patches = 0

        while miss <= n:

            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1

            else:
                # Patch with miss
                miss += miss
                patches += 1

        return patches