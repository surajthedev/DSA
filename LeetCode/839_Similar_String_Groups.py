# Two strings, X and Y, are considered similar if either they are identical or we can make them equivalent by swapping at most two letters (in distinct positions) within the string X.

# For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".

# Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group even though they are not similar.  Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.

# We are given a list strs of strings where every string in strs is an anagram of every other string in strs. How many groups are there?



# Example 1:

# Input: strs = ["tars","rats","arts","star"]
# Output: 2
# Example 2:

# Input: strs = ["omv","ovm"]
# Output: 1


# Constraints:

# 1 <= strs.length <= 300
# 1 <= strs[i].length <= 300
# strs[i] consists of lowercase letters only.
# All words in strs have the same length and are anagrams of each other.
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
    def numSimilarGroups(self, strs: list[str]) -> int:
        n = len(strs)

        def similar(a, b):
            diff = []

            for i in range(len(a)):
                if a[i] != b[i]:
                    diff.append(i)

                    if len(diff) > 2:
                        return False

            return len(diff) == 0 or (
                len(diff) == 2 and
                a[diff[0]] == b[diff[1]] and
                a[diff[1]] == b[diff[0]]
            )

        visited = [False] * n
        groups = 0

        def dfs(i):
            visited[i] = True

            for j in range(n):
                if not visited[j] and similar(strs[i], strs[j]):
                    dfs(j)

        for i in range(n):
            if not visited[i]:
                groups += 1
                dfs(i)

        return groups













# Optimal:
class Solution:
    def numSimilarGroups(self, strs: list[str]) -> int:
        n = len(strs)
        parent = list(range(n))
        groups = n

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            nonlocal groups

            pa = find(a)
            pb = find(b)

            if pa != pb:
                parent[pb] = pa
                groups -= 1

        def similar(a, b):
            diff = []

            for i in range(len(a)):
                if a[i] != b[i]:
                    diff.append(i)

                    if len(diff) > 2:
                        return False

            if len(diff) == 0:
                return True

            if len(diff) != 2:
                return False

            i, j = diff
            return a[i] == b[j] and a[j] == b[i]

        for i in range(n):
            for j in range(i + 1, n):
                if similar(strs[i], strs[j]):
                    union(i, j)

        return groups
