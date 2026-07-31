# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

# Example 1:

# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# Example 2:

# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
# Example 3:

# Input: candidates = [2], target = 1
# Output: []
 

# Constraints:

# 1 <= candidates.length <= 30
# 2 <= candidates[i] <= 40
# All elements of candidates are distinct.
# 1 <= target <= 40




# Brute Force:
class Solution:
    def combinationSum(self, candidates, target):

        ans = []

        def dfs(index, target, path):

            # Valid answer
            if target == 0:
                ans.append(path[:])
                return

            # Out of range
            if index == len(candidates):
                return

            # Take current number
            if candidates[index] <= target:
                path.append(candidates[index])
                dfs(index, target - candidates[index], path)
                path.pop()

            # Skip current number
            dfs(index + 1, target, path)

        dfs(0, target, [])

        return ans






# Optimal:
class Solution:
    def combinationSum(self, candidates, target):

        candidates.sort()

        ans = []

        def backtrack(start, target, path):

            if target == 0:
                ans.append(path[:])
                return

            for i in range(start, len(candidates)):

                # Pruning
                if candidates[i] > target:
                    break

                path.append(candidates[i])

                # Same index because unlimited use allowed
                backtrack(i, target - candidates[i], path)

                path.pop()

        backtrack(0, target, [])

        return ans