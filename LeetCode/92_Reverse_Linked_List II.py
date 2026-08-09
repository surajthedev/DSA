# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 

# Example 1:


# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]
# Example 2:

# Input: head = [5], left = 1, right = 1
# Output: [5]
 

# Constraints:

# The number of nodes in the list is n.
# 1 <= n <= 500
# -500 <= Node.val <= 500
# 1 <= left <= right <= n


# Brute force:
class Solution:
    def reverseBetween(self, head, left, right):
        # Linked list ko array mein convert karo
        values = []

        curr = head

        while curr:
            values.append(curr.val)
            curr = curr.next

        # Required portion reverse karo
        values[left - 1:right] = values[left - 1:right][::-1]

        # New linked list banao
        dummy = ListNode(0)
        curr = dummy

        for value in values:
            curr.next = ListNode(value)
            curr = curr.next

        return dummy.next




# Optimal:
class Solution:
    def reverseBetween(self, head, left, right):
        # Dummy node
        dummy = ListNode(0)
        dummy.next = head

        # prev ko left - 1 position par le jao
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        # Reversal ka first node
        curr = prev.next

        # right-left times reversal
        for _ in range(right - left):
            # curr ke next node ko nikalo
            next_node = curr.next

            # curr ke next ko next_node ke next par lagao
            curr.next = next_node.next

            # next_node ko front mein insert karo
            next_node.next = prev.next
            prev.next = next_node

        return dummy.next