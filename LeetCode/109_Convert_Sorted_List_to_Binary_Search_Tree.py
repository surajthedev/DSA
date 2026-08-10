# Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height-balanced binary search tree.

 

# Example 1:


# Input: head = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
# Example 2:

# Input: head = []
# Output: []
 

# Constraints:

# The number of nodes in head is in the range [0, 2 * 104].
# -105 <= Node.val <= 105




# Brute force:
class Solution:
    def sortedListToBST(self, head):

        if not head:
            return None

        # Sirf ek node
        if not head.next:
            return TreeNode(head.val)

        # Middle find karo
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Left half ko separate karo
        prev.next = None

        # slow = middle
        root = TreeNode(slow.val)

        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)

        return root







# Optimal:
class Solution:
    def sortedListToBST(self, head):

        # Linked list ko array mein convert karo
        nums = []

        while head:
            nums.append(head.val)
            head = head.next

        def build(left, right):

            if left > right:
                return None

            mid = (left + right) // 2

            root = TreeNode(nums[mid])

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(nums) - 1)