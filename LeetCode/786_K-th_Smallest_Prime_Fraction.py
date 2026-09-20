# You are given a sorted integer array arr containing 1 and prime numbers, where all the integers of arr are unique. You are also given an integer k.

# For every i and j where 0 <= i < j < arr.length, we consider the fraction arr[i] / arr[j].

# Return the kth smallest fraction considered. Return your answer as an array of integers of size 2, where answer[0] == arr[i] and answer[1] == arr[j].

 

# Example 1:

# Input: arr = [1,2,3,5], k = 3
# Output: [2,5]
# Explanation: The fractions to be considered in sorted order are:
# 1/5, 1/3, 2/5, 1/2, 3/5, and 2/3.
# The third fraction is 2/5.
# Example 2:

# Input: arr = [1,7], k = 1
# Output: [1,7]
 

# Constraints:

# 2 <= arr.length <= 1000
# 1 <= arr[i] <= 3 * 104
# arr[0] == 1
# arr[i] is a prime number for i > 0.
# All the numbers of arr are unique and sorted in strictly increasing order.
# 1 <= k <= arr.length * (arr.length - 1) / 2












# Brute Force
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        fractions = []

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                fractions.append((arr[i] / arr[j], arr[i], arr[j]))

        fractions.sort()

        return [fractions[k - 1][1], fractions[k - 1][2]]














# Optimal - Binary Search
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        left, right = 0.0, 1.0

        while left < right:
            mid = (left + right) / 2
            count = 0
            best_num, best_den = 0, 1
            j = 1

            for i in range(n - 1):
                while j < n and arr[i] > mid * arr[j]:
                    j += 1

                if j == n:
                    break

                count += n - j

                if best_num * arr[j] < arr[i] * best_den:
                    best_num, best_den = arr[i], arr[j]

            if count == k:
                return [best_num, best_den]

            if count < k:
                left = mid
            else:
                right = mid

        return []