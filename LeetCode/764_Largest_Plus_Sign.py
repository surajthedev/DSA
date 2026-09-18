# You are given an integer n. You have an n x n binary grid grid with all values initially 1's except for some indices given in the array mines. The ith element of the array mines is defined as mines[i] = [xi, yi] where grid[xi][yi] == 0.

# Return the order of the largest axis-aligned plus sign of 1's contained in grid. If there is none, return 0.

# An axis-aligned plus sign of 1's of order k has some center grid[r][c] == 1 along with four arms of length k - 1 going up, down, left, and right, and made of 1's. Note that there could be 0's or 1's beyond the arms of the plus sign, only the relevant area of the plus sign is checked for 1's.

 

# Example 1:


# Input: n = 5, mines = [[4,2]]
# Output: 2
# Explanation: In the above grid, the largest plus sign can only be of order 2. One of them is shown.
# Example 2:


# Input: n = 1, mines = [[0,0]]
# Output: 0
# Explanation: There is no plus sign, so return 0.
 

# Constraints:

# 1 <= n <= 500
# 1 <= mines.length <= 5000
# 0 <= xi, yi < n
# All the pairs (xi, yi) are unique.








# Brute Force

class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: list[list[int]]) -> int:
        grid = [[1] * n for _ in range(n)]

        for r, c in mines:
            grid[r][c] = 0

        ans = 0

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    continue

                k = 1

                while True:
                    d = k

                    if (
                        r - d < 0 or
                        r + d >= n or
                        c - d < 0 or
                        c + d >= n
                    ):
                        break

                    if (
                        grid[r - d][c] == 0 or
                        grid[r + d][c] == 0 or
                        grid[r][c - d] == 0 or
                        grid[r][c + d] == 0
                    ):
                        break

                    k += 1

                ans = max(ans, k)

        return ans












# Optimal - O(n^2)

class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: list[list[int]]) -> int:
        grid = [[n] * n for _ in range(n)]

        for r, c in mines:
            grid[r][c] = 0

        for r in range(n):
            count = 0
            for c in range(n):
                if grid[r][c] == 0:
                    count = 0
                else:
                    count += 1
                    grid[r][c] = min(grid[r][c], count)

            count = 0
            for c in range(n - 1, -1, -1):
                if grid[r][c] == 0:
                    count = 0
                else:
                    count += 1
                    grid[r][c] = min(grid[r][c], count)

        for c in range(n):
            count = 0
            for r in range(n):
                if grid[r][c] == 0:
                    count = 0
                else:
                    count += 1
                    grid[r][c] = min(grid[r][c], count)

            count = 0
            for r in range(n - 1, -1, -1):
                if grid[r][c] == 0:
                    count = 0
                else:
                    count += 1
                    grid[r][c] = min(grid[r][c], count)

        return max(map(max, grid))