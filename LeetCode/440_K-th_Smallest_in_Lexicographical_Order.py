# Given two integers n and k, return the kth lexicographically smallest integer in the range [1, n].

 

# Example 1:

# Input: n = 13, k = 2
# Output: 10
# Explanation: The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.
# Example 2:

# Input: n = 1, k = 1
# Output: 1
 

# Constraints:

# 1 <= k <= n <= 109






# Brute force:
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:

        nums = list(range(1, n + 1))

        nums.sort(key=str)

        return nums[k - 1]





# Optimal:
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:

        def count_steps(prefix):
            steps = 0

            first = prefix
            next_prefix = prefix + 1

            while first <= n:
                steps += min(n + 1, next_prefix) - first

                first *= 10
                next_prefix *= 10

            return steps

        curr = 1
        k -= 1

        while k > 0:

            steps = count_steps(curr)

            if steps <= k:
                # Current prefix ka poora subtree skip
                curr += 1
                k -= steps

            else:
                # Current prefix ke andar jao
                curr *= 10
                k -= 1

        return curr