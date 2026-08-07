# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

# Example 1:


# Input: head = [1,1,2]
# Output: [1,2]
# Example 2:


# Input: head = [1,1,2,3,3]
# Output: [1,2,3]
 

# Constraints:

# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.


# Brute force:
class Solution:
    def deleteDuplicates(self, head):
        if not head:
            return None

        seen = set()

        dummy = ListNode(0)
        tail = dummy

        curr = head

        while curr:
            if curr.val not in seen:
                seen.add(curr.val)

                tail.next = curr
                tail = tail.next

            curr = curr.next

        tail.next = None

        return dummy.next








# Optimal:
class Solution:
    def deleteDuplicates(self, head):
        curr = head

        while curr and curr.next:

            if curr.val == curr.next.val:
                # Delete duplicate node
                curr.next = curr.next.next
            else:
                # Move forward only when values are different
                curr = curr.next

        return head