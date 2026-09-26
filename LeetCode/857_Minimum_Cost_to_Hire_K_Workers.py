# There are n workers. You are given two integer arrays quality and wage where quality[i] is the quality of the ith worker and wage[i] is the minimum wage expectation for the ith worker.

# We want to hire exactly k workers to form a paid group. To hire a group of k workers, we must pay them according to the following rules:

# Every worker in the paid group must be paid at least their minimum wage expectation.
# In the group, each worker's pay must be directly proportional to their quality. This means if a worker’s quality is double that of another worker in the group, then they must be paid twice as much as the other worker.
# Given the integer k, return the least amount of money needed to form a paid group satisfying the above conditions. Answers within 10-5 of the actual answer will be accepted.



# Example 1:

# Input: quality = [10,20,5], wage = [70,50,30], k = 2
# Output: 105.00000
# Explanation: We pay 70 to 0th worker and 35 to 2nd worker.
# Example 2:

# Input: quality = [3,1,10,10,1], wage = [4,8,2,2,7], k = 3
# Output: 30.66667
# Explanation: We pay 4 to 0th worker, 13.33333 to 2nd and 3rd workers separately.


# Constraints:

# n == quality.length == wage.length
# 1 <= k <= n <= 104
# 1 <= quality[i], wage[i] <= 104
#
#
#
#
#
#
#
#
# Brute force:
import itertools

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        ans = float('inf')

        for group in itertools.combinations(range(n), k):
            ratio = max(wage[i] / quality[i] for i in group)
            cost = sum(quality[i] for i in group) * ratio
            ans = min(ans, cost)

        return ans









# Optimal:
import heapq

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = sorted(
            (w / q, q)
            for q, w in zip(quality, wage)
        )

        max_heap = []
        quality_sum = 0
        ans = float('inf')

        for ratio, q in workers:
            heapq.heappush(max_heap, -q)
            quality_sum += q

            if len(max_heap) > k:
                quality_sum += heapq.heappop(max_heap)

            if len(max_heap) == k:
                ans = min(ans, quality_sum * ratio)

        return ans
