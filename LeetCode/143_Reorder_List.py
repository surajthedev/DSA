# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

# Example 1:


# Input: head = [1,2,3,4]
# Output: [1,4,2,3]
# Example 2:


# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]
 

# Constraints:

# The number of nodes in the list is in the range [1, 5 * 104].
# 1 <= Node.val <= 1000








# Brute force:
class Solution:
    def reorderList(self, head):
        nodes = []

        curr = head

        # Store all nodes
        while curr:
            nodes.append(curr)
            curr = curr.next

        left = 0
        right = len(nodes) - 1

        while left < right:
            # L0 -> Ln
            nodes[left].next = nodes[right]
            left += 1

            # Ln -> L1
            nodes[right].next = nodes[left]
            right -= 1

        # Last node should point to None
        nodes[left].next = None









# Optimal:
class Solution:
    def reorderList(self, head):
        if not head or not head.next:
            return

        # --------------------------------
        # Step 1: Find middle
        # --------------------------------
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # --------------------------------
        # Step 2: Reverse second half
        # --------------------------------
        second = slow.next
        slow.next = None

        prev = None

        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        second = prev

        # --------------------------------
        # Step 3: Merge two halves
        # --------------------------------
        first = head

        while second:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next