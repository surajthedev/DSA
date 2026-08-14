# Given the head of a linked list, return the list after sorting it in ascending order.

 

# Example 1:


# Input: head = [4,2,1,3]
# Output: [1,2,3,4]
# Example 2:


# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]
# Example 3:

# Input: head = []
# Output: []
 

# Constraints:

# The number of nodes in the list is in the range [0, 5 * 104].
# -105 <= Node.val <= 105



# Brute force:
class Solution:
    def sortList(self, head):
        # Linked list -> array
        values = []

        curr = head

        while curr:
            values.append(curr.val)
            curr = curr.next

        # Sort array
        values.sort()

        # Array -> linked list
        dummy = ListNode(0)
        curr = dummy

        for value in values:
            curr.next = ListNode(value)
            curr = curr.next

        return dummy.next






# Optimal:
class Solution:
    def sortList(self, head):

        # Base case
        if not head or not head.next:
            return head

        # Find middle
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Split list
        mid = slow.next
        slow.next = None

        # Sort left and right
        left = self.sortList(head)
        right = self.sortList(mid)

        # Merge
        return self.merge(left, right)

    def merge(self, left, right):
        dummy = ListNode(0)
        curr = dummy

        while left and right:

            if left.val <= right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next

            curr = curr.next

        # Remaining nodes
        if left:
            curr.next = left
        else:
            curr.next = right

        return dummy.next