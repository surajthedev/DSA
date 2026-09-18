# You are given an integer array arr of length n that represents a permutation of the integers in the range [0, n - 1].

# We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.

# Return the largest number of chunks we can make to sort the array.

 

# Example 1:

# Input: arr = [4,3,2,1,0]
# Output: 1
# Explanation:
# Splitting into two or more chunks will not return the required result.
# For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.
# Example 2:

# Input: arr = [1,0,2,3,4]
# Output: 4
# Explanation:
# We can split into two chunks, such as [1, 0], [2, 3, 4].
# However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.
 

# Constraints:

# n == arr.length
# 1 <= n <= 10
# 0 <= arr[i] < n
# All the elements of arr are unique.











# Brute Force

class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        n = len(arr)

        def dfs(index):
            if index == n:
                return 0

            ans = 0
            max_val = -1

            for j in range(index, n):
                max_val = max(max_val, arr[j])

                if max_val == j:
                    ans = max(ans, 1 + dfs(j + 1))

            return ans

        return dfs(0)












# Optimal - O(n)

class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        chunks = 0
        max_val = 0

        for i, num in enumerate(arr):
            max_val = max(max_val, num)

            if max_val == i:
                chunks += 1

        return chunks