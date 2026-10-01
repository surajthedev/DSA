# Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.



# Example 1:

# Input: arr = [3,1,2,4]
# Output: 17
# Explanation:
# Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
# Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
# Sum is 17.
# Example 2:

# Input: arr = [11,81,94,43,3]
# Output: 444


# Constraints:

# 1 <= arr.length <= 3 * 104
# 1 <= arr[i] <= 3 * 104
#
#
#
#
#
#
#
#
#
#
# Brute force:
class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        ans = 0
        n = len(arr)

        for i in range(n):
            minimum = float('inf')

            for j in range(i, n):
                minimum = min(minimum, arr[j])
                ans = (ans + minimum) % MOD

        return ans















# Optimal:
class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)

        left = [0] * n
        right = [0] * n

        # Previous smaller element
        stack = []

        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()

            if stack:
                left[i] = i - stack[-1]
            else:
                left[i] = i + 1

            stack.append(i)

        # Next smaller or equal element
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()

            if stack:
                right[i] = stack[-1] - i
            else:
                right[i] = n - i

            stack.append(i)

        ans = 0

        for i in range(n):
            ans = (ans + arr[i] * left[i] * right[i]) % MOD

        return ans
