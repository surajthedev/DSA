# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2

# Output: [1,2]

# Example 2:

# Input: nums = [1], k = 1

# Output: [1]

# Example 3:

# Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

# Output: [1,2]

 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.





# Brute force:
import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}

        # Count frequency
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        min_heap = []

        for num, count in freq.items():
            heapq.heappush(min_heap, (count, num))

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return [num for count, num in min_heap]







# Optimal:
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}

        # Step 1: Count frequency
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Step 2: Create buckets
        buckets = [[] for _ in range(len(nums) + 1)]

        # Step 3: Put numbers into frequency buckets
        for num, count in freq.items():
            buckets[count].append(num)

        # Step 4: Traverse from highest frequency
        result = []

        for count in range(len(buckets) - 1, 0, -1):
            for num in buckets[count]:
                result.append(num)

                if len(result) == k:
                    return result

        return result