# Given an array arr of 4 digits, find the latest 24-hour time that can be made using each digit exactly once.

# 24-hour times are formatted as "HH:MM", where HH is between 00 and 23, and MM is between 00 and 59. The earliest 24-hour time is 00:00, and the latest is 23:59.

# Return the latest 24-hour time in "HH:MM" format. If no valid time can be made, return an empty string.



# Example 1:

# Input: arr = [1,2,3,4]
# Output: "23:41"
# Explanation: The valid 24-hour times are "12:34", "12:43", "13:24", "13:42", "14:23", "14:32", "21:34", "21:43", "23:14", and "23:41". Of these times, "23:41" is the latest.
# Example 2:

# Input: arr = [5,5,5,5]
# Output: ""
# Explanation: There are no valid 24-hour times as "55:55" is not valid.


# Constraints:

# arr.length == 4
# 0 <= arr[i] <= 9
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
#
#
#
# Brute force:
class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        import itertools

        best = ""

        for p in itertools.permutations(arr):
            hour = p[0] * 10 + p[1]
            minute = p[2] * 10 + p[3]

            if hour < 24 and minute < 60:
                time = f"{hour:02d}:{minute:02d}"
                best = max(best, time)

        return best














# Optimal:
class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        best = ""

        def backtrack(path, used):
            nonlocal best

            if len(path) == 4:
                hour = path[0] * 10 + path[1]
                minute = path[2] * 10 + path[3]

                if hour < 24 and minute < 60:
                    time = f"{hour:02d}:{minute:02d}"
                    best = max(best, time)

                return

            for i in range(4):
                if not used[i]:
                    used[i] = True
                    path.append(arr[i])

                    backtrack(path, used)

                    path.pop()
                    used[i] = False

        backtrack([], [False] * 4)

        return best
