# Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

 

# Example 1:


# Input: head = [1,2,3,3,4,4,5]
# Output: [1,2,5]
# Example 2:


# Input: head = [1,1,1,2,3]
# Output: [2,3]
 

# Constraints:

# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.


# Brute force:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head):
        if not head:
            return None

        dummy = ListNode(0)
        tail = dummy

        curr = head

        while curr:
            # Check whether current value occurs more than once
            temp = curr.next
            is_duplicate = False

            while temp:
                if temp.val == curr.val:
                    is_duplicate = True
                    break
                temp = temp.next

            if not is_duplicate:
                tail.next = curr
                tail = tail.next

            curr = curr.next

        # Important: terminate the result list
        tail.next = None

        return dummy.next






# Optimal:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head):
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = head

        while curr:

            # Duplicate found
            if curr.next and curr.val == curr.next.val:

                duplicate_value = curr.val

                # Skip all nodes having duplicate value
                while curr and curr.val == duplicate_value:
                    curr = curr.next

                # Connect previous unique node to next unique node
                prev.next = curr

            else:
                # Current node is unique
                prev = curr
                curr = curr.next

        return dummy.next