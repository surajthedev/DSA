# You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

# Return true if you can make this square and false otherwise.

 

# Example 1:


# Input: matchsticks = [1,1,2,2,2]
# Output: true
# Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
# Example 2:

# Input: matchsticks = [3,3,3,3,4]
# Output: false
# Explanation: You cannot find a way to form a square with all the matchsticks.
 

# Constraints:

# 1 <= matchsticks.length <= 15
# 1 <= matchsticks[i] <= 108







# Brute force:
class Solution:
    def makesquare(self, matchsticks):
        total = sum(matchsticks)

        if total % 4 != 0:
            return False

        target = total // 4
        n = len(matchsticks)

        used = [False] * n

        def backtrack(side, count):
            if side == 4:
                return True

            if count == target:
                return backtrack(side + 1, 0)

            for i in range(n):
                if not used[i] and count + matchsticks[i] <= target:
                    used[i] = True

                    if backtrack(side, count + matchsticks[i]):
                        return True

                    used[i] = False

            return False

        return backtrack(0, 0)







# Optimal:
class Solution:
    def makesquare(self, matchsticks):
        total = sum(matchsticks)

        if total % 4 != 0:
            return False

        target = total // 4
        matchsticks.sort(reverse=True)

        sides = [0] * 4

        def backtrack(i):
            if i == len(matchsticks):
                return True

            stick = matchsticks[i]

            for j in range(4):
                if sides[j] + stick <= target:
                    sides[j] += stick

                    if backtrack(i + 1):
                        return True

                    sides[j] -= stick

                if sides[j] == 0:
                    break

            return False

        return backtrack(0)