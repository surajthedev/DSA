# There are n persons on a social media website. You are given an integer array ages where ages[i] is the age of the ith person.

# A Person x will not send a friend request to a person y (x != y) if any of the following conditions is true:

# age[y] <= 0.5 * age[x] + 7
# age[y] > age[x]
# age[y] > 100 && age[x] < 100
# Otherwise, x will send a friend request to y.

# Note that if x sends a request to y, y will not necessarily send a request to x. Also, a person will not send a friend request to themself.

# Return the total number of friend requests made.



# Example 1:

# Input: ages = [16,16]
# Output: 2
# Explanation: 2 people friend request each other.
# Example 2:

# Input: ages = [16,17,18]
# Output: 2
# Explanation: Friend requests are made 17 -> 16, 18 -> 17.
# Example 3:

# Input: ages = [20,30,100,110,120]
# Output: 3
# Explanation: Friend requests are made 110 -> 100, 120 -> 110, 120 -> 100.


# Constraints:

# n == ages.length
# 1 <= n <= 2 * 104
# 1 <= ages[i] <= 120
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
    def numFriendRequests(self, ages: list[int]) -> int:
        count = [0] * 121

        for age in ages:
            count[age] += 1

        ans = 0

        for x in range(1, 121):
            if count[x] == 0:
                continue

            min_age = int(0.5 * x + 7)

            for y in range(min_age + 1, x + 1):
                if count[y] == 0:
                    continue

                if y > 100 and x < 100:
                    continue

                ans += count[x] * count[y]

                if x == y:
                    ans -= count[x]

        return ans










# Optimal:
class Solution:
    def numFriendRequests(self, ages: list[int]) -> int:
        count = [0] * 121

        for age in ages:
            count[age] += 1

        ans = 0

        for x in range(1, 121):
            if count[x] == 0:
                continue

            for y in range(1, 121):
                if count[y] == 0:
                    continue

                if y <= 0.5 * x + 7:
                    continue

                if y > x:
                    continue

                if y > 100 and x < 100:
                    continue

                ans += count[x] * count[y]

                if x == y:
                    ans -= count[x]

        return ans
