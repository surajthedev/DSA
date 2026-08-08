# Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

 

# Example 1:


# Input: head = [1,4,3,2,5,2], x = 3
# Output: [1,2,2,4,3,5]
# Example 2:

# Input: head = [2,1], x = 2
# Output: [1,2]
 

# Constraints:

# The number of nodes in the list is in the range [0, 200].
# -100 <= Node.val <= 100
# -200 <= x <= 200


# Brute Force:
class Solution:
    def partition(self, head, x):
        values = []

        curr = head

        while curr:
            values.append(curr.val)
            curr = curr.next

        less = []
        greater_equal = []

        for value in values:
            if value < x:
                less.append(value)
            else:
                greater_equal.append(value)

        result = less + greater_equal

        dummy = ListNode(0)
        curr = dummy

        for value in result:
            curr.next = ListNode(value)
            curr = curr.next

        return dummy.next



# Optimal:
class Solution:
    def partition(self, head, x):
        # Dummy nodes for the two partitions
        less_dummy = ListNode(0)
        greater_dummy = ListNode(0)

        less = less_dummy
        greater = greater_dummy

        curr = head

        while curr:
            if curr.val < x:
                less.next = curr
                less = less.next
            else:
                greater.next = curr
                greater = greater.next

            curr = curr.next

        # Join the two partitions
        less.next = greater_dummy.next

        # Very important:
        # terminate the greater/equal list
        greater.next = None

        return less_dummy.next