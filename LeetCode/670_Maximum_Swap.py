# You are given an integer num. You can swap two digits at most once to get the maximum valued number.

# Return the maximum valued number you can get.

 

# Example 1:

# Input: num = 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.
# Example 2:

# Input: num = 9973
# Output: 9973
# Explanation: No swap.
 

# Constraints:

# 0 <= num <= 108








# Brute force:
class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        best = s[:]

        n = len(s)

        for i in range(n):
            for j in range(i + 1, n):
                s[i], s[j] = s[j], s[i]

                if s > best:
                    best = s[:]

                s[i], s[j] = s[j], s[i]

        return int("".join(best))









# Optimal:
class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        last = [-1] * 10

        for i, digit in enumerate(s):
            last[int(digit)] = i

        for i, digit in enumerate(s):
            current = int(digit)

            for d in range(9, current, -1):
                if last[d] > i:
                    j = last[d]

                    s[i], s[j] = s[j], s[i]

                    return int("".join(s))

        return num