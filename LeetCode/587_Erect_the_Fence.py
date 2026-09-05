# You are given an array trees where trees[i] = [xi, yi] represents the location of a tree in the garden.

# Fence the entire garden using the minimum length of rope, as it is expensive. The garden is well-fenced only if all the trees are enclosed.

# Return the coordinates of trees that are exactly located on the fence perimeter. You may return the answer in any order.

 

# Example 1:


# Input: trees = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
# Output: [[1,1],[2,0],[4,2],[3,3],[2,4]]
# Explanation: All the trees will be on the perimeter of the fence except the tree at [2, 2], which will be inside the fence.
# Example 2:


# Input: trees = [[1,2],[2,2],[4,2]]
# Output: [[4,2],[2,2],[1,2]]
# Explanation: The fence forms a line that passes through all the trees.
 

# Constraints:

# 1 <= trees.length <= 3000
# trees[i].length == 2
# 0 <= xi, yi <= 100
# All the given positions are unique.








# Solution:
class Solution:
    def outerTrees(self, trees: list[list[int]]) -> list[list[int]]:
        if len(trees) <= 3:
            return trees

        trees.sort()

        def cross(o, a, b):
            return (
                (a[0] - o[0]) * (b[1] - o[1])
                - (a[1] - o[1]) * (b[0] - o[0])
            )

        lower = []

        for p in trees:
            while len(lower) >= 2 and cross(lower[-2], lower[-1], p) < 0:
                lower.pop()
            lower.append(p)

        upper = []

        for p in reversed(trees):
            while len(upper) >= 2 and cross(upper[-2], upper[-1], p) < 0:
                upper.pop()
            upper.append(p)

        # Remove duplicates while preserving the points
        boundary = {tuple(p) for p in lower + upper}

        return [list(p) for p in boundary]
