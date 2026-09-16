# A k-booking happens when k events have some non-empty intersection (i.e., there is some time that is common to all k events.)

# You are given some events [startTime, endTime), after each given event, return an integer k representing the maximum k-booking between all the previous events.

# Implement the MyCalendarThree class:

# MyCalendarThree() Initializes the object.
# int book(int startTime, int endTime) Returns an integer k representing the largest integer such that there exists a k-booking in the calendar.
 

# Example 1:

# Input
# ["MyCalendarThree", "book", "book", "book", "book", "book", "book"]
# [[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
# Output
# [null, 1, 1, 2, 3, 3, 3]

# Explanation
# MyCalendarThree myCalendarThree = new MyCalendarThree();
# myCalendarThree.book(10, 20); // return 1
# myCalendarThree.book(50, 60); // return 1
# myCalendarThree.book(10, 40); // return 2
# myCalendarThree.book(5, 15); // return 3
# myCalendarThree.book(5, 10); // return 3
# myCalendarThree.book(25, 55); // return 3

 

# Constraints:

# 0 <= startTime < endTime <= 109
# At most 400 calls will be made to book.











# Brute force:
class MyCalendarThree:

    def __init__(self):
        self.events = []

    def book(self, startTime: int, endTime: int) -> int:
        self.events.append((startTime, 1))
        self.events.append((endTime, -1))

        self.events.sort()

        active = 0
        max_booking = 0

        for _, change in self.events:
            active += change
            max_booking = max(max_booking, active)

        return max_booking








# Optimal:
class MyCalendarThree:

    def __init__(self):
        self.tree = {}
        self.lazy = {}

    def _update(self, node, left, right, ql, qr, value):
        if ql <= left and right <= qr:
            self.tree[node] = self.tree.get(node, 0) + value
            self.lazy[node] = self.lazy.get(node, 0) + value
            return

        mid = (left + right) // 2

        if ql <= mid:
            self._update(
                node * 2,
                left,
                mid,
                ql,
                qr,
                value
            )

        if qr > mid:
            self._update(
                node * 2 + 1,
                mid + 1,
                right,
                ql,
                qr,
                value
            )

        self.tree[node] = self.lazy.get(node, 0) + max(
            self.tree.get(node * 2, 0),
            self.tree.get(node * 2 + 1, 0)
        )

    def book(self, startTime: int, endTime: int) -> int:
        self._update(
            1,
            0,
            10**9,
            startTime,
            endTime - 1,
            1
        )

        return self.tree.get(1, 0)