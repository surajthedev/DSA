# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

# The first node is considered odd, and the second node is even, and so on.

# Note that the relative order inside both the even and odd groups should remain as it was in the input.

# You must solve the problem in O(1) extra space complexity and O(n) time complexity.

 

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [1,3,5,2,4]
# Example 2:


# Input: head = [2,1,3,5,6,4,7]
# Output: [2,3,6,7,1,5,4]
 

# Constraints:

# The number of nodes in the linked list is in the range [0, 104].
# -106 <= Node.val <= 106






# Brute force:
class Solution:
    def oddEvenList(self, head):
        if not head:
            return head

        odd = []
        even = []

        index = 1
        curr = head

        while curr:
            if index % 2 == 1:
                odd.append(curr.val)
            else:
                even.append(curr.val)

            curr = curr.next
            index += 1

        values = odd + even

        curr = head
        i = 0

        while curr:
            curr.val = values[i]
            curr = curr.next
            i += 1

        return head





# Optimal:
class Solution:
    def oddEvenList(self, head):
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        # Connect odd list with even list
        odd.next = even_head

        return head