# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

 

# Example 1:


# Input: head = [1,2,2,1]
# Output: true
# Example 2:


# Input: head = [1,2]
# Output: false
 

# Constraints:

# The number of nodes in the list is in the range [1, 105].
# 0 <= Node.val <= 9






# Brute force:
class Solution:
    def isPalindrome(self, head):
        values = []

        current = head

        while current:
            values.append(current.val)
            current = current.next

        return values == values[::-1]






# Optimal:
class Solution:
    def isPalindrome(self, head):
        # Find middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Odd length list:
        # skip the middle node
        if fast:
            slow = slow.next

        # Reverse second half
        second_half = self.reverse(slow)

        # Compare both halves
        first_half = head

        while second_half:
            if first_half.val != second_half.val:
                return False

            first_half = first_half.next
            second_half = second_half.next

        return True

    def reverse(self, head):
        prev = None
        current = head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev