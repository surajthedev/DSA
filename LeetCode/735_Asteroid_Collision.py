# We are given an array asteroids of integers representing asteroids in a row. The indices of the asteroid in the array represent their relative position in space.

# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

 

# Example 1:

# Input: asteroids = [5,10,-5]
# Output: [5,10]
# Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
# Example 2:

# Input: asteroids = [8,-8]
# Output: []
# Explanation: The 8 and -8 collide exploding each other.
# Example 3:

# Input: asteroids = [10,2,-5]
# Output: [10]
# Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
# Example 4:

# Input: asteroids = [3,5,-6,2,-1,4]​​​​​​​
# Output: [-6,2,4]
# Explanation: The asteroid -6 makes the asteroid 3 and 5 explode, and then continues going left. On the other side, the asteroid 2 destroys -1. Since 2 and 4 are both moving right, they never collide.
 

# Constraints:

# 2 <= asteroids.length <= 104
# -1000 <= asteroids[i] <= 1000
# asteroids[i] != 0








# Brute force:
class Solution:
    def asteroidCollision(self, asteroids):
        asteroids = asteroids[:]

        changed = True

        while changed:
            changed = False
            result = []
            i = 0

            while i < len(asteroids):
                if (
                    i + 1 < len(asteroids)
                    and asteroids[i] > 0
                    and asteroids[i + 1] < 0
                ):
                    changed = True

                    if abs(asteroids[i]) > abs(asteroids[i + 1]):
                        result.append(asteroids[i])
                        i += 2

                    elif abs(asteroids[i]) < abs(asteroids[i + 1]):
                        result.append(asteroids[i + 1])
                        i += 2

                    else:
                        i += 2
                else:
                    result.append(asteroids[i])
                    i += 1

            asteroids = result

        return asteroids













# Optimal:
class Solution:
    def asteroidCollision(self, asteroids):
        stack = []

        for asteroid in asteroids:
            alive = True

            while alive and asteroid < 0 and stack and stack[-1] > 0:
                if stack[-1] < -asteroid:
                    stack.pop()

                elif stack[-1] == -asteroid:
                    stack.pop()
                    alive = False

                else:
                    alive = False

            if alive:
                stack.append(asteroid)

        return stack