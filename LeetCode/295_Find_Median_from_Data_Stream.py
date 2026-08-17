# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

# For example, for arr = [2,3,4], the median is 3.
# For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
# Implement the MedianFinder class:

# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 

# Example 1:

# Input
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# Output
# [null, null, null, 1.5, null, 2.0]

# Explanation
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0
 

# Constraints:

# -105 <= num <= 105
# There will be at least one element in the data structure before calling findMedian.
# At most 5 * 104 calls will be made to addNum and findMedian.






# Brute force:
class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num):
        self.nums.append(num)

    def findMedian(self):
        self.nums.sort()

        n = len(self.nums)

        if n % 2 == 1:
            return self.nums[n // 2]

        return (self.nums[n // 2 - 1] + self.nums[n // 2]) / 2






# Optimal:
import heapq

class MedianFinder:

    def __init__(self):
        # Max heap
        # Negative values store karenge
        self.small = []

        # Min heap
        self.large = []

    def addNum(self, num):

        # Pehle small mein add karo
        heapq.heappush(self.small, -num)

        # Ensure:
        # max(small) <= min(large)

        if self.small and self.large:
            if -self.small[0] > self.large[0]:
                value = -heapq.heappop(self.small)
                heapq.heappush(self.large, value)

        # Size difference maximum 1 hona chahiye
        if len(self.small) > len(self.large) + 1:
            value = -heapq.heappop(self.small)
            heapq.heappush(self.large, value)

        elif len(self.large) > len(self.small) + 1:
            value = heapq.heappop(self.large)
            heapq.heappush(self.small, -value)

    def findMedian(self):

        if len(self.small) > len(self.large):
            return -self.small[0]

        if len(self.large) > len(self.small):
            return self.large[0]

        return (-self.small[0] + self.large[0]) / 2