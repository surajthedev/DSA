# A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

# Given a row x col grid of integers, how many 3 x 3 magic square subgrids are there?

# Note: while a magic square can only contain numbers from 1 to 9, grid may contain numbers up to 15.



# Example 1:


# Input: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
# Output: 1
# Explanation:
# The following subgrid is a 3 x 3 magic square:

# while this one is not:

# In total, there is only one magic square inside the given grid.
# Example 2:

# Input: grid = [[8]]
# Output: 0


# Constraints:

# row == grid.length
# col == grid[i].length
# 1 <= row, col <= 10
# 0 <= grid[i][j] <= 15
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
    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        ans = 0

        for r in range(rows - 2):
            for c in range(cols - 2):

                nums = []
                for i in range(3):
                    for j in range(3):
                        nums.append(grid[r + i][c + j])

                if set(nums) != set(range(1, 10)):
                    continue

                target = sum(nums[:3])

                # Rows
                if any(sum(grid[r + i][c:c + 3]) != target for i in range(3)):
                    continue

                # Columns
                if any(
                    grid[r][c + j] +
                    grid[r + 1][c + j] +
                    grid[r + 2][c + j] != target
                    for j in range(3)
                ):
                    continue

                # Diagonals
                if grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2] != target:
                    continue

                if grid[r][c + 2] + grid[r + 1][c + 1] + grid[r + 2][c] != target:
                    continue

                ans += 1

        return ans















# Optimal:
class Solution:
    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        ans = 0

        for r in range(rows - 2):
            for c in range(cols - 2):

                # Center of every 3x3 magic square is 5
                if grid[r + 1][c + 1] != 5:
                    continue

                nums = set()

                valid = True

                for i in range(3):
                    for j in range(3):
                        x = grid[r + i][c + j]

                        if x < 1 or x > 9 or x in nums:
                            valid = False
                            break

                        nums.add(x)

                    if not valid:
                        break

                if not valid:
                    continue

                # Since numbers are 1..9, magic sum must be 15
                if any(
                    sum(grid[r + i][c:c + 3]) != 15
                    for i in range(3)
                ):
                    continue

                if any(
                    grid[r][c + j] +
                    grid[r + 1][c + j] +
                    grid[r + 2][c + j] != 15
                    for j in range(3)
                ):
                    continue

                if (
                    grid[r][c] +
                    grid[r + 1][c + 1] +
                    grid[r + 2][c + 2] != 15
                ):
                    continue

                if (
                    grid[r][c + 2] +
                    grid[r + 1][c + 1] +
                    grid[r + 2][c] != 15
                ):
                    continue

                ans += 1

        return ans
