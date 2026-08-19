# A cinema has n rows of seats, numbered from 1 to n. Each row has 10 seats, numbered from 1 to 10.

# You are given a 2D integer array reservedSeats, where reservedSeats[i] = [rowi, seati] means that seat seati in row rowi is already reserved.

# A four-person group must be assigned to four seats in the same row. The group can be seated in one of the following seat blocks:

# seats 2, 3, 4, 5
# seats 4, 5, 6, 7
# seats 6, 7, 8, 9
# A block can be used only if none of its seats are reserved. Each seat can be assigned to at most one group.

# Return an integer denoting the maximum number of four-person groups that can be assigned.

 

# Example 1:



# Input: n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
# Output: 4
# Explanation: The figure above shows an optimal allocation of four groups. Seats marked in blue are already reserved, and each set of four contiguous seats marked in orange is assigned to one group.
# Example 2:

# Input: n = 2, reservedSeats = [[2,1],[1,8],[2,6]]
# Output: 2
# Example 3:

# Input: n = 4, reservedSeats = [[4,3],[1,4],[4,6],[1,7]]
# Output: 4
 

# Constraints:

# 1 <= n <= 109
# 1 <= reservedSeats.length <= min(10 * n, 104)
# reservedSeats[i] == [rowi, seati]
# 1 <= rowi <= n
# 1 <= seati <= 10
# All reservedSeats[i] are distinct.





# Brute force:
from itertools import combinations

class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        reserved = {}

        # Store reserved seats row-wise
        for row, seat in reservedSeats:
            if row not in reserved:
                reserved[row] = set()
            reserved[row].add(seat)

        # Three possible blocks
        blocks = [
            {2, 3, 4, 5},
            {4, 5, 6, 7},
            {6, 7, 8, 9}
        ]

        ans = 0

        for row in reserved:
            seats = reserved[row]

            # Check every pair of blocks
            max_groups = 0

            for block1, block2 in combinations(blocks, 2):
                # Check if block1 can be used
                can_use_1 = not (seats & block1)

                # Check if block2 can be used
                can_use_2 = not (seats & block2)

                groups = 0

                if can_use_1:
                    groups += 1

                if can_use_2:
                    groups += 1

                max_groups = max(max_groups, groups)

            # Also check individual blocks
            for block in blocks:
                if not (seats & block):
                    max_groups = max(max_groups, 1)

            ans += max_groups

        # Completely empty rows can always fit 2 groups
        ans += (n - len(reserved)) * 2

        return ans







# Optimal:
class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        rows = {}

        # Create bitmask for every row having reserved seats
        for row, seat in reservedSeats:
            rows[row] = rows.get(row, 0) | (1 << seat)

        # Masks for the three possible blocks
        left = (1 << 2) | (1 << 3) | (1 << 4) | (1 << 5)
        middle = (1 << 4) | (1 << 5) | (1 << 6) | (1 << 7)
        right = (1 << 6) | (1 << 7) | (1 << 8) | (1 << 9)

        ans = (n - len(rows)) * 2

        for mask in rows.values():

            left_free = (mask & left) == 0
            right_free = (mask & right) == 0

            if left_free and right_free:
                # Both non-overlapping groups can sit
                ans += 2

            elif left_free or right_free:
                # One group can sit
                ans += 1

            elif (mask & middle) == 0:
                # Only middle block works
                ans += 1

        return ans