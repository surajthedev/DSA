# There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

# After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

# When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

# For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

# You are given a string dominoes representing the initial state where:

# dominoes[i] = 'L', if the ith domino has been pushed to the left,
# dominoes[i] = 'R', if the ith domino has been pushed to the right, and
# dominoes[i] = '.', if the ith domino has not been pushed.
# Return a string representing the final state.



# Example 1:

# Input: dominoes = "RR.L"
# Output: "RR.L"
# Explanation: The first domino expends no additional force on the second domino.
# Example 2:


# Input: dominoes = ".L.R...LR..L.."
# Output: "LL.RR.LLRRLL.."


# Constraints:

# n == dominoes.length
# 1 <= n <= 105
# dominoes[i] is either 'L', 'R', or '.'.
#
#
#
#
#
#
#
## Brute Force - O(n^2)

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = list(dominoes)
        n = len(dominoes)

        while True:
            nxt = dominoes[:]
            changed = False

            for i in range(n):
                if dominoes[i] == 'R':
                    if i + 1 < n and dominoes[i + 1] == '.':
                        if i + 2 >= n or dominoes[i + 2] != 'L':
                            nxt[i + 1] = 'R'

                elif dominoes[i] == 'L':
                    if i - 1 >= 0 and dominoes[i - 1] == '.':
                        if i - 2 < 0 or dominoes[i - 2] != 'R':
                            nxt[i - 1] = 'L'

            if nxt == dominoes:
                break

            dominoes = nxt

        return ''.join(dominoes)










# Optimal - O(n)

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        result = list(dominoes)

        forces = [0] * n

        # Force from left to right (R)
        force = 0
        for i in range(n):
            if dominoes[i] == 'R':
                force = n
            elif dominoes[i] == 'L':
                force = 0
            else:
                force = max(force - 1, 0)

            forces[i] += force

        # Force from right to left (L)
        force = 0
        for i in range(n - 1, -1, -1):
            if dominoes[i] == 'L':
                force = n
            elif dominoes[i] == 'R':
                force = 0
            else:
                force = max(force - 1, 0)

            forces[i] -= force

        # Decide final direction
        for i in range(n):
            if forces[i] > 0:
                result[i] = 'R'
            elif forces[i] < 0:
                result[i] = 'L'
            else:
                result[i] = '.'

        return ''.join(result)
