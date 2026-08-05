# Given the head of a linked list, rotate the list to the right by k places.

 

# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
# Example 2:


# Input: head = [0,1,2], k = 4
# Output: [2,0,1]
 

# Constraints:

# The number of nodes in the list is in the range [0, 500].
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 109






# Brute Force:
class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next:
            return head

        for _ in range(k):
            if not head.next:
                return head

            prev = None
            curr = head

            while curr.next:
                prev = curr
                curr = curr.next

            prev.next = None
            curr.next = head
            head = curr

        return head






# Optimal:
class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head

        # Find length and tail
        length = 1
        tail = head

        while tail.next:
            tail = tail.next
            length += 1

        # Reduce rotations
        k %= length

        if k == 0:
            return head

        # Make circular
        tail.next = head

        # Find new tail
        steps = length - k - 1
        newTail = head

        for _ in range(steps):
            newTail = newTail.next

        # Break circle
        newHead = newTail.next
        newTail.next = None

        return newHead