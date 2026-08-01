# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.

 

# Example 1:

# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# Example 2:

# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]
 

# Constraints:

# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30




# Brute Force:
class Solution:
    def combinationSum2(self, candidates, target):
        n = len(candidates)
        candidates.sort()

        ans = set()

        def solve(index, curr, total):
            if index == n:
                if total == target:
                    ans.add(tuple(curr))
                return

            # Include
            solve(index + 1,
                  curr + [candidates[index]],
                  total + candidates[index])

            # Exclude
            solve(index + 1,
                  curr,
                  total)

        solve(0, [], 0)

        return [list(x) for x in ans]





# Optimal:
class Solution:
    def combinationSum2(self, candidates, target):

        candidates.sort()

        ans = []
        path = []

        def backtrack(start, remain):

            if remain == 0:
                ans.append(path[:])
                return

            if remain < 0:
                return

            for i in range(start, len(candidates)):

                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                path.append(candidates[i])

                backtrack(i + 1, remain - candidates[i])

                path.pop()

        backtrack(0, target)

        return ans