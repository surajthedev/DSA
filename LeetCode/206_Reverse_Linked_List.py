# Given the head of a singly linked list, reverse the list, and return the reversed list.

 

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Example 2:


# Input: head = [1,2]
# Output: [2,1]
# Example 3:

# Input: head = []
# Output: []
 

# Constraints:

# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000
 


# Brute force:
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        values = []

        curr = head

        while curr:
            values.append(curr.val)
            curr = curr.next

        curr = head

        for val in reversed(values):
            curr.val = val
            curr = curr.next

        return head






# Optimal:
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        curr = head

        while curr:
            next_node = curr.next

            curr.next = prev

            prev = curr
            curr = next_node

        return prev