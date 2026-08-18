# Given an integer array nums, handle multiple queries of the following types:

# Update the value of an element in nums.
# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:

# NumArray(int[] nums) Initializes the object with the integer array nums.
# void update(int index, int val) Updates the value of nums[index] to be val.
# int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
 

# Example 1:

# Input
# ["NumArray", "sumRange", "update", "sumRange"]
# [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
# Output
# [null, 9, null, 8]

# Explanation
# NumArray numArray = new NumArray([1, 3, 5]);
# numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
# numArray.update(1, 2);   // nums = [1, 2, 5]
# numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8
 

# Constraints:

# 1 <= nums.length <= 3 * 104
# -100 <= nums[i] <= 100
# 0 <= index < nums.length
# -100 <= val <= 100
# 0 <= left <= right < nums.length
# At most 3 * 104 calls will be made to update and sumRange.





# Brute force:
class NumArray:

    def __init__(self, nums):
        self.nums = nums

    def update(self, index, val):
        self.nums[index] = val

    def sumRange(self, left, right):
        total = 0

        for i in range(left, right + 1):
            total += self.nums[i]

        return total





# Optimal:
class NumArray:

    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)

        def build(node, start, end):
            if start == end:
                self.tree[node] = nums[start]
                return

            mid = (start + end) // 2

            build(node * 2, start, mid)
            build(node * 2 + 1, mid + 1, end)

            self.tree[node] = (
                self.tree[node * 2] +
                self.tree[node * 2 + 1]
            )

        build(1, 0, self.n - 1)

    def update(self, index, val):
        def update_tree(node, start, end):
            if start == end:
                self.tree[node] = val
                return

            mid = (start + end) // 2

            if index <= mid:
                update_tree(node * 2, start, mid)
            else:
                update_tree(node * 2 + 1, mid + 1, end)

            self.tree[node] = (
                self.tree[node * 2] +
                self.tree[node * 2 + 1]
            )

        update_tree(1, 0, self.n - 1)

    def sumRange(self, left, right):
        def query(node, start, end):
            # Completely outside
            if right < start or end < left:
                return 0

            # Completely inside
            if left <= start and end <= right:
                return self.tree[node]

            mid = (start + end) // 2

            return (
                query(node * 2, start, mid) +
                query(node * 2 + 1, mid + 1, end)
            )

        return query(1, 0, self.n - 1)