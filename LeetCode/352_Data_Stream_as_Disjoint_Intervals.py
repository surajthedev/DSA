# Given a data stream input of non-negative integers a1, a2, ..., an, summarize the numbers seen so far as a list of disjoint intervals.

# Implement the SummaryRanges class:

# SummaryRanges() Initializes the object with an empty stream.
# void addNum(int value) Adds the integer value to the stream.
# int[][] getIntervals() Returns a summary of the integers in the stream currently as a list of disjoint intervals [starti, endi]. The answer should be sorted by starti.
 

# Example 1:

# Input
# ["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
# [[], [1], [], [3], [], [7], [], [2], [], [6], []]
# Output
# [null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7, 7]], null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]]

# Explanation
# SummaryRanges summaryRanges = new SummaryRanges();
# summaryRanges.addNum(1);      // arr = [1]
# summaryRanges.getIntervals(); // return [[1, 1]]
# summaryRanges.addNum(3);      // arr = [1, 3]
# summaryRanges.getIntervals(); // return [[1, 1], [3, 3]]
# summaryRanges.addNum(7);      // arr = [1, 3, 7]
# summaryRanges.getIntervals(); // return [[1, 1], [3, 3], [7, 7]]
# summaryRanges.addNum(2);      // arr = [1, 2, 3, 7]
# summaryRanges.getIntervals(); // return [[1, 3], [7, 7]]
# summaryRanges.addNum(6);      // arr = [1, 2, 3, 6, 7]
# summaryRanges.getIntervals(); // return [[1, 3], [6, 7]]
 

# Constraints:

# 0 <= value <= 104
# At most 3 * 104 calls will be made to addNum and getIntervals.
# At most 102 calls will be made to getIntervals.





# Brute force:
class SummaryRanges:

    def __init__(self):
        self.nums = set()

    def addNum(self, value: int) -> None:
        self.nums.add(value)

    def getIntervals(self) -> list[list[int]]:
        nums = sorted(self.nums)

        if not nums:
            return []

        result = []

        start = nums[0]
        prev = nums[0]

        for num in nums[1:]:
            if num == prev + 1:
                prev = num
            else:
                result.append([start, prev])
                start = num
                prev = num

        result.append([start, prev])

        return result





# Optimal:
from bisect import bisect_left

class SummaryRanges:

    def __init__(self):
        self.intervals = []

    def addNum(self, value: int) -> None:
        intervals = self.intervals

        # Find position where value should be inserted
        i = bisect_left(intervals, [value, value])

        # Already exists in previous interval
        if i > 0 and intervals[i - 1][0] <= value <= intervals[i - 1][1]:
            return

        # Already exists in current interval
        if i < len(intervals) and intervals[i][0] <= value <= intervals[i][1]:
            return

        merge_left = (
            i > 0 and intervals[i - 1][1] + 1 == value
        )

        merge_right = (
            i < len(intervals) and intervals[i][0] - 1 == value
        )

        if merge_left and merge_right:
            # Merge both intervals
            intervals[i - 1][1] = intervals[i][1]
            intervals.pop(i)

        elif merge_left:
            # Extend left interval
            intervals[i - 1][1] = value

        elif merge_right:
            # Extend right interval
            intervals[i][0] = value

        else:
            # Create a new interval
            intervals.insert(i, [value, value])

    def getIntervals(self) -> list[list[int]]:
        return self.intervals