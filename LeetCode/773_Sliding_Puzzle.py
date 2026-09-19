# On an 2 x 3 board, there are five tiles labeled from 1 to 5, and an empty square represented by 0. A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

# The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

# Given the puzzle board board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.

 

# Example 1:


# Input: board = [[1,2,3],[4,0,5]]
# Output: 1
# Explanation: Swap the 0 and the 5 in one move.
# Example 2:


# Input: board = [[1,2,3],[5,4,0]]
# Output: -1
# Explanation: No number of moves will make the board solved.
# Example 3:


# Input: board = [[4,1,2],[5,0,3]]
# Output: 5
# Explanation: 5 is the smallest number of moves that solves the board.
# An example path:
# After move 0: [[4,1,2],[5,0,3]]
# After move 1: [[4,1,2],[0,5,3]]
# After move 2: [[0,1,2],[4,5,3]]
# After move 3: [[1,0,2],[4,5,3]]
# After move 4: [[1,2,0],[4,5,3]]
# After move 5: [[1,2,3],[4,5,0]]
 

# Constraints:

# board.length == 2
# board[i].length == 3
# 0 <= board[i][j] <= 5
# Each value board[i][j] is unique.









# Brute force:
from collections import deque

class Solution:
    def slidingPuzzle(self, board):
        start = ''.join(map(str, sum(board, [])))
        target = "123450"

        queue = deque([(start, 0)])
        visited = {start}

        directions = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }

        while queue:
            state, moves = queue.popleft()

            if state == target:
                return moves

            zero = state.index('0')

            for nxt in directions[zero]:
                arr = list(state)
                arr[zero], arr[nxt] = arr[nxt], arr[zero]
                new_state = ''.join(arr)

                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, moves + 1))

        return -1











# Optimal:
from collections import deque

class Solution:
    def slidingPuzzle(self, board):
        start = ''.join(map(str, sum(board, [])))
        target = "123450"

        if start == target:
            return 0

        directions = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }

        q1 = {start}
        q2 = {target}
        dist1 = {start: 0}
        dist2 = {target: 0}

        while q1 and q2:
            if len(q1) > len(q2):
                q1, q2 = q2, q1
                dist1, dist2 = dist2, dist1

            next_level = set()

            for state in q1:
                zero = state.index('0')

                for nxt in directions[zero]:
                    arr = list(state)
                    arr[zero], arr[nxt] = arr[nxt], arr[zero]
                    new_state = ''.join(arr)

                    if new_state in dist2:
                        return dist1[state] + 1 + dist2[new_state]

                    if new_state not in dist1:
                        dist1[new_state] = dist1[state] + 1
                        next_level.add(new_state)

            q1 = next_level

        return -1