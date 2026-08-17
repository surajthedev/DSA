# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

# Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

 

# Example 1:


# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]
# Example 2:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 104].
# -1000 <= Node.val <= 1000





# Brute force:
class Codec:

    def serialize(self, root):
        if not root:
            return ""

        result = []

        def dfs(node):
            if not node:
                result.append("N")
                return

            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(result)

    def deserialize(self, data):
        if not data:
            return None

        values = data.split(",")
        index = 0

        def dfs():
            nonlocal index

            if values[index] == "N":
                index += 1
                return None

            node = TreeNode(int(values[index]))
            index += 1

            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()







# Optimal:
from collections import deque

class Codec:

    def serialize(self, root):
        if not root:
            return ""

        result = []
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node is None:
                result.append("N")
                continue

            result.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)

        return ",".join(result)

    def deserialize(self, data):
        if not data:
            return None

        values = data.split(",")

        root = TreeNode(int(values[0]))
        queue = deque([root])

        i = 1

        while queue:
            node = queue.popleft()

            if values[i] != "N":
                node.left = TreeNode(int(values[i]))
                queue.append(node.left)
            i += 1

            if values[i] != "N":
                node.right = TreeNode(int(values[i]))
                queue.append(node.right)
            i += 1

        return root