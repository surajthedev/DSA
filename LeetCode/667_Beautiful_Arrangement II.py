# Given two integers n and k, construct a list answer that contains n different positive integers ranging from 1 to n and obeys the following requirement:

# Suppose this list is answer = [a1, a2, a3, ... , an], then the list [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] has exactly k distinct integers.
# Return the list answer. If there multiple valid answers, return any of them.

 

# Example 1:

# Input: n = 3, k = 1
# Output: [1,2,3]
# Explanation: The [1,2,3] has three different positive integers ranging from 1 to 3, and the [1,1] has exactly 1 distinct integer: 1
# Example 2:

# Input: n = 3, k = 2
# Output: [1,3,2]
# Explanation: The [1,3,2] has three different positive integers ranging from 1 to 3, and the [2,1] has exactly 2 distinct integers: 1 and 2.
 

# Constraints:

# 1 <= k < n <= 104








# Brute force:
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        from itertools import permutations

        for p in permutations(range(1, n + 1)):
            diffs = set()

            for i in range(n - 1):
                diffs.add(abs(p[i] - p[i + 1]))

            if len(diffs) == k:
                return list(p)

        return []








# Optimal:
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        ans = []

        # First k + 1 elements create differences:
        # k, k-1, ..., 1
        left, right = 1, k + 1

        while left <= right:
            if left == right:
                ans.append(left)
            elif len(ans) % 2 == 0:
                ans.append(left)
                left += 1
                continue
            else:
                ans.append(right)
                right -= 1
                continue

            break

        # Append remaining numbers in increasing order
        for x in range(k + 2, n + 1):
            ans.append(x)

        return ans