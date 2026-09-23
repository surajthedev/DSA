# Your car starts at position 0 and speed +1 on an infinite number line. Your car can go into negative positions. Your car drives automatically according to a sequence of instructions 'A' (accelerate) and 'R' (reverse):

# When you get an instruction 'A', your car does the following:
# position += speed
# speed *= 2
# When you get an instruction 'R', your car does the following:
# If your speed is positive then speed = -1
# otherwise speed = 1
# Your position stays the same.
# For example, after commands "AAR", your car goes to positions 0 --> 1 --> 3 --> 3, and your speed goes to 1 --> 2 --> 4 --> -1.

# Given a target position target, return the length of the shortest sequence of instructions to get there.



# Example 1:

# Input: target = 3
# Output: 2
# Explanation:
# The shortest instruction sequence is "AA".
# Your position goes from 0 --> 1 --> 3.
# Example 2:

# Input: target = 6
# Output: 5
# Explanation:
# The shortest instruction sequence is "AAARA".
# Your position goes from 0 --> 1 --> 3 --> 7 --> 7 --> 6.


# Constraints:

# 1 <= target <= 104
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
from collections import deque

class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 1, 0)])
        visited = {(0, 1)}

        while queue:
            position, speed, steps = queue.popleft()

            if position == target:
                return steps

            # A
            new_pos = position + speed
            new_speed = speed * 2

            if abs(new_pos) <= 2 * target and (new_pos, new_speed) not in visited:
                visited.add((new_pos, new_speed))
                queue.append((new_pos, new_speed, steps + 1))

            # R
            new_speed = -1 if speed > 0 else 1

            if (position, new_speed) not in visited:
                visited.add((position, new_speed))
                queue.append((position, new_speed, steps + 1))











# Optimal:
class Solution:
    def racecar(self, target: int) -> int:
        dp = [0] * (target + 1)

        for t in range(1, target + 1):
            n = t.bit_length()

            if (1 << n) - 1 == t:
                dp[t] = n
                continue

            dp[t] = n + 1 + dp[(1 << n) - 1 - t]

            for m in range(n - 1):
                forward = (1 << (n - 1)) - 1
                backward = (1 << m) - 1

                remaining = t - forward + backward
                dp[t] = min(
                    dp[t],
                    (n - 1) + 1 + m + 1 + dp[remaining]
                )

        return dp[target]
