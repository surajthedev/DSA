# Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

# BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
# boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
# int next() Moves the pointer to the right, then returns the number at the pointer.
# Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

# You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.

 

# Example 1:


# Input
# ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
# [[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
# Output
# [null, 3, 7, true, 9, true, 15, true, 20, false]

# Explanation
# BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
# bSTIterator.next();    // return 3
# bSTIterator.next();    // return 7
# bSTIterator.hasNext(); // return True
# bSTIterator.next();    // return 9
# bSTIterator.hasNext(); // return True
# bSTIterator.next();    // return 15
# bSTIterator.hasNext(); // return True
# bSTIterator.next();    // return 20
# bSTIterator.hasNext(); // return False
 

# Constraints:

# The number of nodes in the tree is in the range [1, 105].
# 0 <= Node.val <= 106
# At most 105 calls will be made to hasNext, and next.







# Brute force:
class BSTIterator:

    def __init__(self, root):
        self.values = []
        self.index = 0

        self.inorder(root)

    def inorder(self, node):
        if node is None:
            return

        self.inorder(node.left)
        self.values.append(node.val)
        self.inorder(node.right)

    def next(self):
        value = self.values[self.index]
        self.index += 1
        return value

    def hasNext(self):
        return self.index < len(self.values)









# Optimal:
class BSTIterator:

    def __init__(self, root):
        self.stack = []
        self.pushLeft(root)

    def pushLeft(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        node = self.stack.pop()

        if node.right:
            self.pushLeft(node.right)

        return node.val

    def hasNext(self):
        return len(self.stack) > 0