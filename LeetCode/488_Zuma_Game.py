# You are playing a variation of the game Zuma.

# In this variation of Zuma, there is a single row of colored balls on a board, where each ball can be colored red 'R', yellow 'Y', blue 'B', green 'G', or white 'W'. You also have several colored balls in your hand.

# Your goal is to clear all of the balls from the board. On each turn:

# Pick any ball from your hand and insert it in between two balls in the row or on either end of the row.
# If there is a group of three or more consecutive balls of the same color, remove the group of balls from the board.
# If this removal causes more groups of three or more of the same color to form, then continue removing each group until there are none left.
# If there are no more balls on the board, then you win the game.
# Repeat this process until you either win or do not have any more balls in your hand.
# Given a string board, representing the row of balls on the board, and a string hand, representing the balls in your hand, return the minimum number of balls you have to insert to clear all the balls from the board. If you cannot clear all the balls from the board using the balls in your hand, return -1.

 

# Example 1:

# Input: board = "WRRBBW", hand = "RB"
# Output: -1
# Explanation: It is impossible to clear all the balls. The best you can do is:
# - Insert 'R' so the board becomes WRRRBBW. WRRRBBW -> WBBW.
# - Insert 'B' so the board becomes WBBBW. WBBBW -> WW.
# There are still balls remaining on the board, and you are out of balls to insert.
# Example 2:

# Input: board = "WWRRBBWW", hand = "WRBRW"
# Output: 2
# Explanation: To make the board empty:
# - Insert 'R' so the board becomes WWRRRBBWW. WWRRRBBWW -> WWBBWW.
# - Insert 'B' so the board becomes WWBBBWW. WWBBBWW -> WWWW -> empty.
# 2 balls from your hand were needed to clear the board.
# Example 3:

# Input: board = "G", hand = "GGGGG"
# Output: 2
# Explanation: To make the board empty:
# - Insert 'G' so the board becomes GG.
# - Insert 'G' so the board becomes GGG. GGG -> empty.
# 2 balls from your hand were needed to clear the board.
 

# Constraints:

# 1 <= board.length <= 16
# 1 <= hand.length <= 5
# board and hand consist of the characters 'R', 'Y', 'B', 'G', and 'W'.
# The initial row of balls on the board will not have any groups of three or more consecutive balls of the same color.










# Solution:
from collections import deque


class Solution:
    def findMinStep(self, board, hand):

        def shrink(s):
            while True:
                i = 0
                res = []
                changed = False

                while i < len(s):
                    j = i + 1

                    while j < len(s) and s[j] == s[i]:
                        j += 1

                    if j - i >= 3:
                        changed = True
                    else:
                        res.append(s[i:j])

                    i = j

                new_s = ''.join(res)

                if not changed:
                    return new_s

                s = new_s

        hand = ''.join(sorted(hand))

        queue = deque([(board, hand, 0)])
        visited = {(board, hand)}

        while queue:
            board, hand, steps = queue.popleft()

            if not board:
                return steps

            for c in set(hand):
                new_hand = hand.replace(c, '', 1)

                for i in range(len(board) + 1):

                    left = board[i - 1] if i > 0 else None
                    right = board[i] if i < len(board) else None

                    if left != c and right != c and left != right:
                        continue

                    new_board = shrink(
                        board[:i] + c + board[i:]
                    )

                    state = (new_board, new_hand)

                    if state in visited:
                        continue

                    visited.add(state)
                    queue.append(
                        (new_board, new_hand, steps + 1)
                    )

        return -1