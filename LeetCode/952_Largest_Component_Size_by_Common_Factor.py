# You are given an integer array of unique positive integers nums. Consider the following graph:

# There are nums.length nodes, labeled nums[0] to nums[nums.length - 1],
# There is an undirected edge between nums[i] and nums[j] if nums[i] and nums[j] share a common factor greater than 1.
# Return the size of the largest connected component in the graph.



# Example 1:


# Input: nums = [4,6,15,35]
# Output: 4
# Example 2:


# Input: nums = [20,50,9,63]
# Output: 2
# Example 3:


# Input: nums = [2,3,6,7,4,12,21,39]
# Output: 8


# Constraints:

# 1 <= nums.length <= 2 * 104
# 1 <= nums[i] <= 105
# All the values of nums are unique.
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
#
#
#
#
# Brute force:
class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        n = len(nums)
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            pa, pb = find(a), find(b)
            if pa != pb:
                parent[pb] = pa

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        for i in range(n):
            for j in range(i + 1, n):
                if gcd(nums[i], nums[j]) > 1:
                    union(i, j)

        count = {}
        ans = 0

        for i in range(n):
            root = find(i)
            count[root] = count.get(root, 0) + 1
            ans = max(ans, count[root])

        return ans













# Optimal:
class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        n = len(nums)

        parent = list(range(n))
        size = [1] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            pa = find(a)
            pb = find(b)

            if pa == pb:
                return

            if size[pa] < size[pb]:
                pa, pb = pb, pa

            parent[pb] = pa
            size[pa] += size[pb]

        factor_to_index = {}

        for i, num in enumerate(nums):
            x = num
            factor = 2

            while factor * factor <= x:
                if x % factor == 0:
                    if factor in factor_to_index:
                        union(i, factor_to_index[factor])
                    else:
                        factor_to_index[factor] = i

                    while x % factor == 0:
                        x //= factor

                factor += 1

            if x > 1:
                if x in factor_to_index:
                    union(i, factor_to_index[x])
                else:
                    factor_to_index[x] = i

        return max(size[find(i)] for i in range(n))
