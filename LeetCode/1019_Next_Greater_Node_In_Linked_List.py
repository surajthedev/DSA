# You are given the head of a linked list with n nodes.

# For each node in the list, find the value of the next greater node. That is, for each node, find the value of the first node that is next to it and has a strictly larger value than it.

# Return an integer array answer where answer[i] is the value of the next greater node of the ith node (1-indexed). If the ith node does not have a next greater node, set answer[i] = 0.



# Example 1:


# Input: head = [2,1,5]
# Output: [5,5,0]
# Example 2:


# Input: head = [2,7,4,3,5]
# Output: [7,0,5,5,0]


# Constraints:

# The number of nodes in the list is n.
# 1 <= n <= 104
# 1 <= Node.val <= 109
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# ### Brute Force

python
```

class Solution:
    def nextLargerNodes(self, head: ListNode) -> list[int]:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        n = len(nums)
        ans = [0] * n

        for i in range(n):
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    ans[i] = nums[j]
                    break

        return ans
```

### Optimal — Monotonic Stack

python
```

class Solution:
    def nextLargerNodes(self, head: ListNode) -> list[int]:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        ans = [0] * len(nums)
        stack = []

        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                ans[stack.pop()] = num

            stack.append(i)

        return ans
```
