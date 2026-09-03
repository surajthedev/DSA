# You are given several boxes with different colors represented by different positive numbers.

# You may experience several rounds to remove boxes until there is no box left. Each time you can choose some continuous boxes with the same color (i.e., composed of k boxes, k >= 1), remove them and get k * k points.

# Return the maximum points you can get.

 

# Example 1:

# Input: boxes = [1,3,2,2,2,3,4,3,1]
# Output: 23
# Explanation:
# [1, 3, 2, 2, 2, 3, 4, 3, 1] 
# ----> [1, 3, 3, 4, 3, 1] (3*3=9 points) 
# ----> [1, 3, 3, 3, 1] (1*1=1 points) 
# ----> [1, 1] (3*3=9 points) 
# ----> [] (2*2=4 points)
# Example 2:

# Input: boxes = [1,1,1]
# Output: 9
# Example 3:

# Input: boxes = [1]
# Output: 1
 

# Constraints:

# 1 <= boxes.length <= 100
# 1 <= boxes[i] <= 100








# Brute force:
class Solution:
    def removeBoxes(self, boxes):
        from functools import lru_cache

        @lru_cache(None)
        def dp(arr):
            arr = list(arr)

            if not arr:
                return 0

            ans = 0
            n = len(arr)

            for i in range(n):
                j = i
                while j < n and arr[j] == arr[i]:
                    j += 1

                k = j - i
                remaining = tuple(arr[:i] + arr[j:])

                ans = max(ans, k * k + dp(remaining))

            return ans

        return dp(tuple(boxes))







# Optimal:
class Solution:
    def removeBoxes(self, boxes):
        from functools import lru_cache

        n = len(boxes)

        @lru_cache(None)
        def dp(l, r, k):
            if l > r:
                return 0

            while l < r and boxes[l] == boxes[l + 1]:
                l += 1
                k += 1

            ans = (k + 1) * (k + 1) + dp(l + 1, r, 0)

            for m in range(l + 1, r + 1):
                if boxes[m] == boxes[l]:
                    ans = max(
                        ans,
                        dp(l + 1, m - 1, 0) +
                        dp(m, r, k + 1)
                    )

            return ans

        return dp(0, n - 1, 0)