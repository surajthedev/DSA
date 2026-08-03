# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
# Example 3:

# Input: intervals = [[4,7],[1,4]]
# Output: [[1,7]]
# Explanation: Intervals [1,4] and [4,7] are considered overlapping.
 

# Constraints:

# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104


# Brute Force:
class Solution:
    def merge(self, intervals):
        changed = True

        while changed:
            changed = False
            result = []
            used = [False] * len(intervals)

            for i in range(len(intervals)):
                if used[i]:
                    continue

                start, end = intervals[i]

                for j in range(i + 1, len(intervals)):
                    if used[j]:
                        continue

                    if not (intervals[j][0] > end or intervals[j][1] < start):
                        start = min(start, intervals[j][0])
                        end = max(end, intervals[j][1])
                        used[j] = True
                        changed = True

                used[i] = True
                result.append([start, end])

            intervals = result

        return intervals







# Optimal:
class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])

        merged = []

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged