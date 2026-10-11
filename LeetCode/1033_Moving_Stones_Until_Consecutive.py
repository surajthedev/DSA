# There are three stones in different positions on the X-axis. You are given three integers a, b, and c, the positions of the stones.

# In one move, you pick up a stone at an endpoint (i.e., either the lowest or highest position stone), and move it to an unoccupied position between those endpoints. Formally, let's say the stones are currently at positions x, y, and z with x < y < z. You pick up the stone at either position x or position z, and move that stone to an integer position k, with x < k < z and k != y.

# The game ends when you cannot make any more moves (i.e., the stones are in three consecutive positions).

# Return an integer array answer of length 2 where:

# answer[0] is the minimum number of moves you can play, and
# answer[1] is the maximum number of moves you can play.


# Example 1:

# Input: a = 1, b = 2, c = 5
# Output: [1,2]
# Explanation: Move the stone from 5 to 3, or move the stone from 5 to 4 to 3.
# Example 2:

# Input: a = 4, b = 3, c = 2
# Output: [0,0]
# Explanation: We cannot make any moves.
# Example 3:

# Input: a = 3, b = 5, c = 1
# Output: [1,2]
# Explanation: Move the stone from 1 to 4; or move the stone from 1 to 2 to 4.


# Constraints:

# 1 <= a, b, c <= 100
# a, b, and c have different values.
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
# ### Brute Force

python
```
class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> list[int]:
        stones = sorted([a, b, c])
        x, y, z = stones

        def dfs(x, y, z):
            if z - x == 2:
                return (0, 0)

            moves = []

            for k in range(x + 1, z):
                if k != y:
                    if k < y:
                        moves.append(dfs(k, y, z))
                    else:
                        moves.append(dfs(x, y, k))

            if not moves:
                return (0, 0)

            return (
                1 + min(m[0] for m in moves),
                1 + max(m[1] for m in moves)
            )

        result = dfs(x, y, z)
        return list(result)
```

### Optimal (Greedy / Math)

python
```
class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> list[int]:
        x, y, z = sorted([a, b, c])

        if z - x == 2:
            return [0, 0]

        max_moves = (y - x - 1) + (z - y - 1)

        if y - x <= 2 or z - y <= 2:
            min_moves = 1
        else:
            min_moves = 2

        return [min_moves, max_moves]
```
