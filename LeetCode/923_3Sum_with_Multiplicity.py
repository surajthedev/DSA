# Given an integer array arr, and an integer target, return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.

# As the answer can be very large, return it modulo 109 + 7.



# Example 1:

# Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
# Output: 20
# Explanation:
# Enumerating by the values (arr[i], arr[j], arr[k]):
# (1, 2, 5) occurs 8 times;
# (1, 3, 4) occurs 8 times;
# (2, 2, 4) occurs 2 times;
# (2, 3, 3) occurs 2 times.
# Example 2:

# Input: arr = [1,1,2,2,2,2], target = 5
# Output: 12
# Explanation:
# arr[i] = 1, arr[j] = arr[k] = 2 occurs 12 times:
# We choose one 1 from [1,1] in 2 ways,
# and two 2s from [2,2,2,2] in 6 ways.
# Example 3:

# Input: arr = [2,1,3], target = 6
# Output: 1
# Explanation: (1, 2, 3) occured one time in the array so we return 1.


# Constraints:

# 3 <= arr.length <= 3000
# 0 <= arr[i] <= 100
# 0 <= target <= 300
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
    def threeSumMulti(self, arr: list[int], target: int) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        ans = 0

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if arr[i] + arr[j] + arr[k] == target:
                        ans += 1

        return ans % MOD











# Optimal:
class Solution:
    def threeSumMulti(self, arr: list[int], target: int) -> int:
        MOD = 10**9 + 7

        freq = [0] * 101

        for x in arr:
            freq[x] += 1

        ans = 0

        for a in range(101):
            if freq[a] == 0:
                continue

            for b in range(a, 101):
                c = target - a - b

                if c < b or c > 100:
                    continue

                if freq[b] == 0 or freq[c] == 0:
                    continue

                if a == b == c:
                    ans += freq[a] * (freq[a] - 1) * (freq[a] - 2) // 6

                elif a == b:
                    ans += freq[a] * (freq[a] - 1) // 2 * freq[c]

                elif b == c:
                    ans += freq[a] * freq[b] * (freq[b] - 1) // 2

                else:
                    ans += freq[a] * freq[b] * freq[c]

        return ans % MOD
