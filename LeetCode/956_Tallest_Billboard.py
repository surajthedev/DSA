# You are installing a billboard and want it to have the largest height. The billboard will have two steel supports, one on each side. Each steel support must be an equal height.

# You are given a collection of rods that can be welded together. For example, if you have rods of lengths 1, 2, and 3, you can weld them together to make a support of length 6.

# Return the largest possible height of your billboard installation. If you cannot support the billboard, return 0.



# Example 1:

# Input: rods = [1,2,3,6]
# Output: 6
# Explanation: We have two disjoint subsets {1,2,3} and {6}, which have the same sum = 6.
# Example 2:

# Input: rods = [1,2,3,4,5,6]
# Output: 10
# Explanation: We have two disjoint subsets {2,3,5} and {4,6}, which have the same sum = 10.
# Example 3:

# Input: rods = [1,2]
# Output: 0
# Explanation: The billboard cannot be supported, so we return 0.


# Constraints:

# 1 <= rods.length <= 20
# 1 <= rods[i] <= 1000
# sum(rods[i]) <= 5000
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# Brute force:
class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        n = len(rods)
        best = 0

        def dfs(i, left, right):
            nonlocal best

            if i == n:
                if left == right:
                    best = max(best, left)
                return

            # Don't use this rod
            dfs(i + 1, left, right)

            # Put rod on left
            dfs(i + 1, left + rods[i], right)

            # Put rod on right
            dfs(i + 1, left, right + rods[i])

        dfs(0, 0, 0)
        return best














# Optimal:
class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        # dp[diff] = maximum height of the shorter side
        dp = {0: 0}

        for rod in rods:
            cur = dp.copy()

            for diff, height in dp.items():
                # Put rod on taller side
                new_diff = diff + rod
                cur[new_diff] = max(cur.get(new_diff, 0), height)

                # Put rod on shorter side
                if rod <= diff:
                    new_diff = diff - rod
                    new_height = height + rod
                else:
                    new_diff = rod - diff
                    new_height = height + diff

                cur[new_diff] = max(
                    cur.get(new_diff, 0),
                    new_height
                )

            dp = cur

        return dp.get(0, 0)
