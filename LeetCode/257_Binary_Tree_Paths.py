# Given the root of a binary tree, return all root-to-leaf paths in any order.

# A leaf is a node with no children.

 

# Example 1:


# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]
# Example 2:

# Input: root = [1]
# Output: ["1"]
 

# Constraints:

# The number of nodes in the tree is in the range [1, 100].
# -100 <= Node.val <= 100






# Brute force:
class Solution:
    def binaryTreePaths(self, root):
        result = []

        def dfs(node, path):
            if not node:
                return

            path.append(str(node.val))

            # Leaf node
            if not node.left and not node.right:
                result.append("->".join(path))
                path.pop()
                return

            dfs(node.left, path)
            dfs(node.right, path)

            # Backtrack
            path.pop()

        dfs(root, [])

        return result




# Optimal:
class Solution:
    def binaryTreePaths(self, root):
        result = []

        def dfs(node, path):
            if not node:
                return

            current_path = path + str(node.val)

            if not node.left and not node.right:
                result.append(current_path)
                return

            current_path += "->"

            dfs(node.left, current_path)
            dfs(node.right, current_path)

        dfs(root, "")

        return result