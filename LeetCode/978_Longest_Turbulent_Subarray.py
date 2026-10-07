# Given an integer array arr, return the length of a maximum size turbulent subarray of arr.

# A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

# More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is said to be turbulent if and only if:

# For i <= k < j:
# arr[k] > arr[k + 1] when k is odd, and
# arr[k] < arr[k + 1] when k is even.
# Or, for i <= k < j:
# arr[k] > arr[k + 1] when k is even, and
# arr[k] < arr[k + 1] when k is odd.


# Example 1:

# Input: arr = [9,4,2,10,7,8,8,1,9]
# Output: 5
# Explanation: arr[1] > arr[2] < arr[3] > arr[4] < arr[5]
# Example 2:

# Input: arr = [4,8,12,16]
# Output: 2
# Example 3:

# Input: arr = [100]
# Output: 1


# Constraints:

# 1 <= arr.length <= 4 * 104
# 0 <= arr[i] <= 109
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
#
# Brute force:
class Solution:
    def maxTurbulenceSize(self, arr: list[int]) -> int:
        n = len(arr)
        ans = 1

        for i in range(n):
            for j in range(i + 1, n):
                valid = True

                for k in range(i, j):
                    if k % 2 == 0:
                        if arr[k] >= arr[k + 1]:
                            valid = False
                            break
                    else:
                        if arr[k] <= arr[k + 1]:
                            valid = False
                            break

                if valid:
                    ans = max(ans, j - i + 1)

        return ans














# Optimal:
class Solution:
    def maxTurbulenceSize(self, arr: list[int]) -> int:
        n = len(arr)

        if n == 1:
            return 1

        ans = 1
        inc = 1
        dec = 1

        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                inc = dec + 1
                dec = 1

            elif arr[i] < arr[i - 1]:
                dec = inc + 1
                inc = 1

            else:
                inc = 1
                dec = 1

            ans = max(ans, inc, dec)

        return ans
