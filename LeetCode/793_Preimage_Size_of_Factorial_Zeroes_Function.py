# Let f(x) be the number of zeroes at the end of x!. Recall that x! = 1 * 2 * 3 * ... * x and by convention, 0! = 1.

# For example, f(3) = 0 because 3! = 6 has no zeroes at the end, while f(11) = 2 because 11! = 39916800 has two zeroes at the end.
# Given an integer k, return the number of non-negative integers x have the property that f(x) = k.

 

# Example 1:

# Input: k = 0
# Output: 5
# Explanation: 0!, 1!, 2!, 3!, and 4! end with k = 0 zeroes.
# Example 2:

# Input: k = 5
# Output: 0
# Explanation: There is no x such that x! ends in k = 5 zeroes.
# Example 3:

# Input: k = 3
# Output: 5
 

# Constraints:

# 0 <= k <= 109











# Brute Force
class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        count = 0
        x = 0

        while x <= 5 * k + 5:
            zeros = 0
            n = x

            while n:
                n //= 5
                zeros += n

            if zeros == k:
                count += 1
            elif zeros > k:
                break

            x += 1

        return count














# Optimal - Binary Search
class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def zeros(n):
            count = 0
            while n:
                n //= 5
                count += n
            return count

        left, right = 0, 5 * (k + 1)

        while left <= right:
            mid = (left + right) // 2
            z = zeros(mid)

            if z < k:
                left = mid + 1
            else:
                right = mid - 1

        start = left

        left, right = 0, 5 * (k + 1)

        while left <= right:
            mid = (left + right) // 2
            z = zeros(mid)

            if z <= k:
                left = mid + 1
            else:
                right = mid - 1

        end = right

        return end - start + 1