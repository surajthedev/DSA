# Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

 

# Example 1:


# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:

# Example 2:


# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
 

# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in a strictly increasing order.






# Brute force:
class Solution:
    def sortedArrayToBST(self, nums):

        if not nums:
            return None

        mid = len(nums) // 2

        root = TreeNode(nums[mid])

        # Left half
        root.left = self.sortedArrayToBST(nums[:mid])

        # Right half
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        return root






# optimal:
class Solution:
    def sortedArrayToBST(self, nums):

        def build(left, right):

            if left > right:
                return None

            mid = (left + right) // 2

            root = TreeNode(nums[mid])

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(nums) - 1)