# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

# You may return the answer in any order.

 

# Example 1:

# Input: n = 4, k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
# Explanation: There are 4 choose 2 = 6 total combinations.
# Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
# Example 2:

# Input: n = 1, k = 1
# Output: [[1]]
# Explanation: There is 1 choose 1 = 1 total combination.
 

# Constraints:

# 1 <= n <= 20
# 1 <= k <= n



# Brute force:
class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:

        all_results = []

        def generate(path):

            if len(path) == k:
                all_results.append(path[:])
                return

            for num in range(1, n + 1):

                # Same number ko ek combination
                # mein repeat nahi karna
                if num not in path:
                    path.append(num)

                    generate(path)

                    path.pop()

        generate([])

        # [1,2] aur [2,1] ko same maan kar
        # duplicates remove karna
        unique = set()

        for arr in all_results:
            unique.add(tuple(sorted(arr)))

        return [list(x) for x in unique]






# Optimal solution:
class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:

        result = []
        path = []

        def backtrack(start):

            # k numbers choose ho gaye
            if len(path) == k:
                result.append(path[:])
                return

            # start se numbers choose karo
            for num in range(start, n + 1):

                path.append(num)

                # Next number current num se bada hona chahiye
                backtrack(num + 1)

                # Backtrack
                path.pop()

        backtrack(1)

        return result