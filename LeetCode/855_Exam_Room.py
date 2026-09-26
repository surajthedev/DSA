# There is an exam room with n seats in a single row labeled from 0 to n - 1.

# When a student enters the room, they must sit in the seat that maximizes the distance to the closest person. If there are multiple such seats, they sit in the seat with the lowest number. If no one is in the room, then the student sits at seat number 0.

# Design a class that simulates the mentioned exam room.

# Implement the ExamRoom class:

# ExamRoom(int n) Initializes the object of the exam room with the number of the seats n.
# int seat() Returns the label of the seat at which the next student will set.
# void leave(int p) Indicates that the student sitting at seat p will leave the room. It is guaranteed that there will be a student sitting at seat p.


# Example 1:

# Input
# ["ExamRoom", "seat", "seat", "seat", "seat", "leave", "seat"]
# [[10], [], [], [], [], [4], []]
# Output
# [null, 0, 9, 4, 2, null, 5]

# Explanation
# ExamRoom examRoom = new ExamRoom(10);
# examRoom.seat(); // return 0, no one is in the room, then the student sits at seat number 0.
# examRoom.seat(); // return 9, the student sits at the last seat number 9.
# examRoom.seat(); // return 4, the student sits at the last seat number 4.
# examRoom.seat(); // return 2, the student sits at the last seat number 2.
# examRoom.leave(4);
# examRoom.seat(); // return 5, the student sits at the last seat number 5.



# Constraints:

# 1 <= n <= 109
# It is guaranteed that there is a student sitting at seat p.
# At most 104 calls will be made to seat and leave.
#
#
#
#
#
#
#
#
# Brute force:
class ExamRoom:

    def __init__(self, n: int):
        self.n = n
        self.students = []

    def seat(self) -> int:
        if not self.students:
            self.students.append(0)
            return 0

        best_seat = 0
        best_dist = self.students[0]

        for i in range(len(self.students) - 1):
            left = self.students[i]
            right = self.students[i + 1]

            dist = (right - left) // 2

            if dist > best_dist:
                best_dist = dist
                best_seat = left + dist

        last_dist = self.n - 1 - self.students[-1]

        if last_dist > best_dist:
            best_seat = self.n - 1

        self.students.append(best_seat)
        self.students.sort()

        return best_seat

    def leave(self, p: int) -> None:
        self.students.remove(p)








# Optimal:
import heapq

class ExamRoom:

    def __init__(self, n: int):
        self.n = n
        self.students = set()
        self.heap = []

    def _distance(self, left, right):
        if left == -1:
            return right
        if right == self.n:
            return self.n - 1 - left
        return (right - left) // 2

    def _add_interval(self, left, right):
        if right - left <= 1:
            return

        dist = self._distance(left, right)

        heapq.heappush(
            self.heap,
            (-dist, left, right)
        )

    def _valid(self, left, right):
        if left != -1 and left not in self.students:
            return False

        if right != self.n and right not in self.students:
            return False

        return True

    def seat(self) -> int:

        # First student
        if not self.students:
            self.students.add(0)
            return 0

        # Clean invalid intervals
        while self.heap:
            neg_dist, left, right = self.heap[0]

            if self._valid(left, right):
                break

            heapq.heappop(self.heap)

        # If heap is empty, rebuild intervals
        if not self.heap:
            seats = sorted(self.students)

            self._add_interval(-1, seats[0])

            for i in range(len(seats) - 1):
                self._add_interval(seats[i], seats[i + 1])

            self._add_interval(seats[-1], self.n)

        while self.heap:
            neg_dist, left, right = heapq.heappop(self.heap)

            if not self._valid(left, right):
                continue

            if left == -1:
                seat = 0
            elif right == self.n:
                seat = self.n - 1
            else:
                seat = (left + right) // 2

            self.students.add(seat)

            self._add_interval(left, seat)
            self._add_interval(seat, right)

            return seat

    def leave(self, p: int) -> None:
        self.students.remove(p)

        # Empty room
        if not self.students:
            self.heap.clear()
            return

        # Rebuild intervals
        self.heap.clear()

        seats = sorted(self.students)

        self._add_interval(-1, seats[0])

        for i in range(len(seats) - 1):
            self._add_interval(seats[i], seats[i + 1])

        self._add_interval(seats[-1], self.n)
