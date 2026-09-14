# A Range Module is a module that tracks ranges of numbers. Design a data structure to track the ranges represented as half-open intervals and query about them.

# A half-open interval [left, right) denotes all the real numbers x where left <= x < right.

# Implement the RangeModule class:

# RangeModule() Initializes the object of the data structure.
# void addRange(int left, int right) Adds the half-open interval [left, right), tracking every real number in that interval. Adding an interval that partially overlaps with currently tracked numbers should add any numbers in the interval [left, right) that are not already tracked.
# boolean queryRange(int left, int right) Returns true if every real number in the interval [left, right) is currently being tracked, and false otherwise.
# void removeRange(int left, int right) Stops tracking every real number currently being tracked in the half-open interval [left, right).
 

# Example 1:

# Input
# ["RangeModule", "addRange", "removeRange", "queryRange", "queryRange", "queryRange"]
# [[], [10, 20], [14, 16], [10, 14], [13, 15], [16, 17]]
# Output
# [null, null, null, true, false, true]

# Explanation
# RangeModule rangeModule = new RangeModule();
# rangeModule.addRange(10, 20);
# rangeModule.removeRange(14, 16);
# rangeModule.queryRange(10, 14); // return True,(Every number in [10, 14) is being tracked)
# rangeModule.queryRange(13, 15); // return False,(Numbers like 14, 14.03, 14.17 in [13, 15) are not being tracked)
# rangeModule.queryRange(16, 17); // return True, (The number 16 in [16, 17) is still being tracked, despite the remove operation)
 

# Constraints:

# 1 <= left < right <= 109
# At most 104 calls will be made to addRange, queryRange, and removeRange.











# Brute force:
class RangeModule:

    def __init__(self):
        self.intervals = []

    def addRange(self, left: int, right: int) -> None:
        new_intervals = []
        placed = False

        for l, r in self.intervals:
            if r < left:
                new_intervals.append([l, r])
            elif right < l:
                if not placed:
                    new_intervals.append([left, right])
                    placed = True
                new_intervals.append([l, r])
            else:
                left = min(left, l)
                right = max(right, r)

        if not placed:
            new_intervals.append([left, right])

        self.intervals = new_intervals

    def queryRange(self, left: int, right: int) -> bool:
        for l, r in self.intervals:
            if l <= left and right <= r:
                return True
            if l > left:
                break

        return False

    def removeRange(self, left: int, right: int) -> None:
        new_intervals = []

        for l, r in self.intervals:
            if r <= left or l >= right:
                new_intervals.append([l, r])
            else:
                if l < left:
                    new_intervals.append([l, left])
                if r > right:
                    new_intervals.append([right, r])

        self.intervals = new_intervals









# Optimal:
from bisect import bisect_left

class RangeModule:

    def __init__(self):
        self.intervals = []

    def addRange(self, left: int, right: int) -> None:
        i = bisect_left(self.intervals, [left])

        if i > 0 and self.intervals[i - 1][1] >= left:
            i -= 1

        j = i

        while j < len(self.intervals) and self.intervals[j][0] <= right:
            left = min(left, self.intervals[j][0])
            right = max(right, self.intervals[j][1])
            j += 1

        self.intervals[i:j] = [[left, right]]

    def queryRange(self, left: int, right: int) -> bool:
        i = bisect_left(self.intervals, [left])

        if i > 0:
            i -= 1

        return (
            i < len(self.intervals)
            and self.intervals[i][0] <= left
            and right <= self.intervals[i][1]
        )

    def removeRange(self, left: int, right: int) -> None:
        i = bisect_left(self.intervals, [left])

        if i > 0:
            i -= 1

        result = self.intervals[:i]

        while i < len(self.intervals):
            l, r = self.intervals[i]

            if l >= right:
                break

            if l < left:
                result.append([l, left])

            if r > right:
                result.append([right, r])

            i += 1

        result.extend(self.intervals[i:])
        self.intervals = result
