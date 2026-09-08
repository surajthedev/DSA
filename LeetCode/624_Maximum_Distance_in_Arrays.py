# You are given m arrays, where each array is sorted in ascending order.

# You can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a - b|.

# Return the maximum distance.

 

# Example 1:

# Input: arrays = [[1,2,3],[4,5],[1,2,3]]
# Output: 4
# Explanation: One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
# Example 2:

# Input: arrays = [[1],[1]]
# Output: 0
 

# Constraints:

# m == arrays.length
# 2 <= m <= 105
# 1 <= arrays[i].length <= 500
# -104 <= arrays[i][j] <= 104
# arrays[i] is sorted in ascending order.
# There will be at most 105 integers in all the arrays.












# Brute force:
class Solution:
    def maxDistance(self, arrays):
        ans = 0

        for i in range(len(arrays)):
            for j in range(i + 1, len(arrays)):
                ans = max(
                    ans,
                    abs(arrays[i][0] - arrays[j][-1]),
                    abs(arrays[i][-1] - arrays[j][0])
                )

        return ans








# Optimal:
class Solution:
    def maxDistance(self, arrays):
        ans = 0

        min_val = arrays[0][0]
        max_val = arrays[0][-1]

        for i in range(1, len(arrays)):
            ans = max(
                ans,
                max_val - arrays[i][0],
                arrays[i][-1] - min_val
            )

            min_val = min(min_val, arrays[i][0])
            max_val = max(max_val, arrays[i][-1])

        return ans