# You are given an array of positive integers nums and a positive integer k. You are also given a 2D array queries, where queries[i] = [indexi, valuei, starti, xi].

# You are allowed to perform an operation once on nums, where you can remove any suffix from nums such that nums remains non-empty.

# The x-value of nums for a given x is defined as the number of ways to perform this operation so that the product of the remaining elements leaves a remainder of x modulo k.

# For each query in queries you need to determine the x-value of nums for xi after performing the following actions:

# Update nums[indexi] to valuei. Only this step persists for the rest of the queries.
# Remove the prefix nums[0..(starti - 1)] (where nums[0..(-1)] will be used to represent the empty prefix).
# Return an array result of size queries.length where result[i] is the answer for the ith query.

# A prefix of an array is a subarray that starts from the beginning of the array and extends to any point within it.

# A suffix of an array is a subarray that starts at any point within the array and extends to the end of the array.

# Note that the prefix and suffix to be chosen for the operation can be empty.

# Note that x-value has a different definition in this version.



# Example 1:

# Input: nums = [1,2,3,4,5], k = 3, queries = [[2,2,0,2],[3,3,3,0],[0,1,0,1]]

# Output: [2,2,2]

# Explanation:

# For query 0, nums becomes [1, 2, 2, 4, 5], and the empty prefix must be removed. The possible operations are:
# Remove the suffix [2, 4, 5]. nums becomes [1, 2].
# Remove the empty suffix. nums becomes [1, 2, 2, 4, 5] with a product 80, which gives remainder 2 when divided by 3.
# For query 1, nums becomes [1, 2, 2, 3, 5], and the prefix [1, 2, 2] must be removed. The possible operations are:
# Remove the empty suffix. nums becomes [3, 5].
# Remove the suffix [5]. nums becomes [3].
# For query 2, nums becomes [1, 2, 2, 3, 5], and the empty prefix must be removed. The possible operations are:
# Remove the suffix [2, 2, 3, 5]. nums becomes [1].
# Remove the suffix [3, 5]. nums becomes [1, 2, 2].
# Example 2:

# Input: nums = [1,2,4,8,16,32], k = 4, queries = [[0,2,0,2],[0,2,0,1]]

# Output: [1,0]

# Explanation:

# For query 0, nums becomes [2, 2, 4, 8, 16, 32]. The only possible operation is:
# Remove the suffix [2, 4, 8, 16, 32].
# For query 1, nums becomes [2, 2, 4, 8, 16, 32]. There is no possible way to perform the operation.
# Example 3:

# Input: nums = [1,1,2,1,1], k = 2, queries = [[2,1,0,1]]

# Output: [5]



# Constraints:

# 1 <= nums[i] <= 109
# 1 <= nums.length <= 105
# 1 <= k <= 5
# 1 <= queries.length <= 2 * 104
# queries[i] == [indexi, valuei, starti, xi]
# 0 <= indexi <= nums.length - 1
# 1 <= valuei <= 109
# 0 <= starti <= nums.length - 1
# 0 <= xi <= k - 1
#
#
#
#
#
#
#
#
# Brute Force

class Solution:
    def resultArray(self, nums, k, queries):
        ans = []

        for index, value, start, x in queries:
            nums[index] = value

            prod = 1
            count = 0

            for i in range(start, len(nums)):
                prod = (prod * nums[i]) % k

                if prod == x:
                    count += 1

            ans.append(count)

        return ans









# Optimal - Segment Tree

class Solution:
    def resultArray(self, nums, k, queries):
        n = len(nums)

        tree = [[0] * k for _ in range(4 * n)]
        mul = [1] * (4 * n)

        def merge(node):
            left = node * 2
            right = left + 1

            lp = mul[left]
            rp = mul[right]

            mul[node] = (lp * rp) % k

            res = [0] * k

            for i in range(k):
                res[i] += tree[left][i]

            for i in range(k):
                if tree[right][i]:
                    res[(lp * i) % k] += tree[right][i]

            tree[node] = res

        def build(node, l, r):
            if l == r:
                p = nums[l] % k
                mul[node] = p
                tree[node][p] = 1
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            merge(node)

        def update(node, l, r, idx, value):
            if l == r:
                p = value % k
                mul[node] = p
                tree[node] = [0] * k
                tree[node][p] = 1
                return

            mid = (l + r) // 2

            if idx <= mid:
                update(node * 2, l, mid, idx, value)
            else:
                update(node * 2 + 1, mid + 1, r, idx, value)

            merge(node)

        def query(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                return mul[node], tree[node]

            mid = (l + r) // 2

            if qr <= mid:
                return query(node * 2, l, mid, ql, qr)

            if ql > mid:
                return query(node * 2 + 1, mid + 1, r, ql, qr)

            lp, lc = query(node * 2, l, mid, ql, qr)
            rp, rc = query(node * 2 + 1, mid + 1, r, ql, qr)

            res = lc[:]

            for i in range(k):
                res[(lp * i) % k] += rc[i]

            return (lp * rp) % k, res

        build(1, 0, n - 1)

        ans = []

        for index, value, start, x in queries:
            nums[index] = value

            update(1, 0, n - 1, index, value)

            _, counts = query(1, 0, n - 1, start, n - 1)

            ans.append(counts[x])

        return ans
