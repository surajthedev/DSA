# There is an m x n binary grid matrix with all the values set 0 initially. Design an algorithm to randomly pick an index (i, j) where matrix[i][j] == 0 and flips it to 1. All the indices (i, j) where matrix[i][j] == 0 should be equally likely to be returned.

# Optimize your algorithm to minimize the number of calls made to the built-in random function of your language and optimize the time and space complexity.

# Implement the Solution class:

# Solution(int m, int n) Initializes the object with the size of the binary matrix m and n.
# int[] flip() Returns a random index [i, j] of the matrix where matrix[i][j] == 0 and flips it to 1.
# void reset() Resets all the values of the matrix to be 0.
 

# Example 1:

# Input
# ["Solution", "flip", "flip", "flip", "reset", "flip"]
# [[3, 1], [], [], [], [], []]
# Output
# [null, [1, 0], [2, 0], [0, 0], null, [2, 0]]

# Explanation
# Solution solution = new Solution(3, 1);
# solution.flip();  // return [1, 0], [0,0], [1,0], and [2,0] should be equally likely to be returned.
# solution.flip();  // return [2, 0], Since [1,0] was returned, [2,0] and [0,0]
# solution.flip();  // return [0, 0], Based on the previously returned indices, only [0,0] can be returned.
# solution.reset(); // All the values are reset to 0 and can be returned.
# solution.flip();  // return [2, 0], [0,0], [1,0], and [2,0] should be equally likely to be returned.
 

# Constraints:

# 1 <= m, n <= 104
# There will be at least one free cell for each call to flip.
# At most 1000 calls will be made to flip and reset.







# Brute force:
import random

class Solution:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.cells = [(i, j) for i in range(m) for j in range(n)]

    def flip(self) -> list[int]:
        idx = random.randint(0, len(self.cells) - 1)

        self.cells[idx], self.cells[-1] = self.cells[-1], self.cells[idx]
        cell = self.cells.pop()

        return list(cell)

    def reset(self) -> None:
        self.cells = [(i, j) for i in range(self.m) for j in range(self.n)]







# Optimal:
import random

class Solution:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.total = m * n
        self.remaining = self.total
        self.mp = {}

    def flip(self) -> list[int]:
        self.remaining -= 1

        r = random.randint(0, self.remaining)

        # Map r to the actual unused index
        x = self.mp.get(r, r)

        # Last available index
        last = self.mp.get(self.remaining, self.remaining)

        # Move last index into r's position
        self.mp[r] = last

        # Convert 1D index -> 2D index
        return [x // self.n, x % self.n]

    def reset(self) -> None:
        self.remaining = self.total
        self.mp.clear()