# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 

# Example 1:

# Input: head = [1,2,3,4]

# Output: [2,1,4,3]

# Explanation:



# Example 2:

# Input: head = []

# Output: []

# Example 3:

# Input: head = [1]

# Output: [1]

# Example 4:

# Input: head = [1,2,3]

# Output: [2,1,3]

 

# Constraints:

# The number of nodes in the list is in the range [0, 100].
# 0 <= Node.val <= 100




# Brute Force:
class Solution:
    def swapPairs(self, head):
        arr = []

        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next

        for i in range(0, len(arr) - 1, 2):
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

        curr = head
        i = 0
        while curr:
            curr.val = arr[i]
            i += 1
            curr = curr.next

        return head






# Optimal Approach:
class Solution:
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        while prev.next and prev.next.next:
            first = prev.next
            second = first.next

            first.next = second.next
            second.next = first
            prev.next = second

            prev = first

        return dummy.next