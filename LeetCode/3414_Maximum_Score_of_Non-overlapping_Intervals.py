# You are given a 2D integer array intervals, where intervals[i] = [li, ri, weighti]. Interval i starts at position li and ends at ri, and has a weight of weighti. You can choose up to 4 non-overlapping intervals. The score of the chosen intervals is defined as the total sum of their weights.

# Return the lexicographically smallest array of at most 4 indices from intervals with maximum score, representing your choice of non-overlapping intervals.

# Two intervals are said to be non-overlapping if they do not share any points. In particular, intervals sharing a left or right boundary are considered overlapping.

 

# Example 1:

# Input: intervals = [[1,3,2],[4,5,2],[1,5,5],[6,9,3],[6,7,1],[8,9,1]]

# Output: [2,3]

# Explanation:

# You can choose the intervals with indices 2, and 3 with respective weights of 5, and 3.

# Example 2:

# Input: intervals = [[5,8,1],[6,7,7],[4,7,3],[9,10,6],[7,8,2],[11,14,3],[3,5,5]]

# Output: [1,3,5,6]

# Explanation:

# You can choose the intervals with indices 1, 3, 5, and 6 with respective weights of 7, 6, 3, and 5.

 

# Constraints:

# 1 <= intevals.length <= 5 * 104
# intervals[i].length == 3
# intervals[i] = [li, ri, weighti]
# 1 <= li <= ri <= 109
# 1 <= weighti <= 109








# Brute force:
from typing import List

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        ans_score = 0
        ans = []

        def dfs(pos, selected, score):
            nonlocal ans_score, ans

            if len(selected) > 4:
                return

            if score > ans_score or (score == ans_score and sorted(selected) < ans):
                ans_score = score
                ans = sorted(selected)

            if len(selected) == 4:
                return

            for i in range(pos, n):
                l, r, w = intervals[i]

                if not selected or all(
                    intervals[j][1] < l or intervals[j][0] > r
                    for j in selected
                ):
                    dfs(i + 1, selected + [i], score + w)

        dfs(0, [], 0)
        return ans










# Optimal:
from typing import List
from bisect import bisect_left

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)

        arr = sorted(
            [(l, r, w, i) for i, (l, r, w) in enumerate(intervals)]
        )

        starts = [x[0] for x in arr]

        # dp[k][i] = best result using intervals from i onward
        dp = [[(0, ()) for _ in range(n + 1)] for _ in range(5)]

        for k in range(1, 5):
            for i in range(n - 1, -1, -1):
                l, r, w, idx = arr[i]

                j = bisect_left(starts, r + 1, i + 1)

                take_score = w + dp[k - 1][j][0]
                take_indices = tuple(sorted((idx,) + dp[k - 1][j][1]))

                skip_score = dp[k][i + 1][0]
                skip_indices = dp[k][i + 1][1]

                if take_score > skip_score:
                    dp[k][i] = (take_score, take_indices)
                elif take_score < skip_score:
                    dp[k][i] = (skip_score, skip_indices)
                else:
                    dp[k][i] = (
                        take_score,
                        min(take_indices, skip_indices)
                    )

        return list(dp[4][0][1])