# You are given an integer array arr.

# We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.

# Return the largest number of chunks we can make to sort the array.

 

# Example 1:

# Input: arr = [5,4,3,2,1]
# Output: 1
# Explanation:
# Splitting into two or more chunks will not return the required result.
# For example, splitting into [5, 4], [3, 2, 1] will result in [4, 5, 1, 2, 3], which isn't sorted.
# Example 2:

# Input: arr = [2,1,3,4,4]
# Output: 4
# Explanation:
# We can split into two chunks, such as [2, 1], [3, 4, 4].
# However, splitting into [2, 1], [3], [4], [4] is the highest number of chunks possible.
 

# Constraints:

# 1 <= arr.length <= 2000
# 0 <= arr[i] <= 108












# Brute Force

class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        n = len(arr)
        target = sorted(arr)

        def can_split(start, chunks):
            if start == n:
                return chunks

            for end in range(start, n):
                chunk = sorted(arr[start:end + 1])

                if chunk == target[start:end + 1]:
                    result = can_split(end + 1, chunks + 1)
                    if result:
                        return result

            return 0

        return can_split(0, 0)












# Optimal - O(n log n)

class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        sorted_arr = sorted(arr)

        count = 0
        balance = 0

        from collections import Counter

        diff = Counter()

        for i in range(len(arr)):
            diff[arr[i]] += 1
            diff[sorted_arr[i]] -= 1

            if diff[arr[i]] == 0:
                del diff[arr[i]]

            if diff.get(sorted_arr[i], 0) == 0:
                diff.pop(sorted_arr[i], None)

            if not diff:
                count += 1

        return count