# Given a binary tree

# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.

 

# Example 1:


# Input: root = [1,2,3,4,5,null,7]
# Output: [1,#,2,3,#,4,5,7,#]
# Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
# Example 2:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 6000].
# -100 <= Node.val <= 100




# Brute force:
from collections import deque

class Solution:
    def connect(self, root):
        if root is None:
            return None

        queue = deque([root])

        while queue:
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()

                # Connect to next node in same level
                if i < level_size - 1:
                    node.next = queue[0]

                # Add children
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return root







# Optimal:
class Solution:
    def connect(self, root):
        current = root

        while current:
            # Dummy node for the next level
            dummy = Node(0)
            tail = dummy

            # Traverse current level using next pointers
            while current:
                if current.left:
                    tail.next = current.left
                    tail = tail.next

                if current.right:
                    tail.next = current.right
                    tail = tail.next

                current = current.next

            # Move to the first node of next level
            current = dummy.next

        return root