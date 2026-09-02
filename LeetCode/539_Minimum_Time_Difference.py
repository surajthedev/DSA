# Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.
 

# Example 1:

# Input: timePoints = ["23:59","00:00"]
# Output: 1
# Example 2:

# Input: timePoints = ["00:00","23:59","00:00"]
# Output: 0
 

# Constraints:

# 2 <= timePoints.length <= 2 * 104
# timePoints[i] is in the format "HH:MM".








# Brute force:
class Solution:
    def findMinDifference(self, timePoints):
        times = []

        for time in timePoints:
            h, m = map(int, time.split(":"))
            times.append(h * 60 + m)

        ans = float('inf')

        for i in range(len(times)):
            for j in range(i + 1, len(times)):
                diff = abs(times[i] - times[j])
                diff = min(diff, 1440 - diff)
                ans = min(ans, diff)

        return ans







# Optimal:
class Solution:
    def findMinDifference(self, timePoints):
        times = []

        for time in timePoints:
            h, m = map(int, time.split(":"))
            times.append(h * 60 + m)

        times.sort()

        ans = float('inf')

        for i in range(1, len(times)):
            ans = min(ans, times[i] - times[i - 1])

        ans = min(ans, 1440 - times[-1] + times[0])

        return ans