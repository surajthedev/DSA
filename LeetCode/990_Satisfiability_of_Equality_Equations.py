# You are given an array of strings equations that represent relationships between variables where each string equations[i] is of length 4 and takes one of two different forms: "xi==yi" or "xi!=yi".Here, xi and yi are lowercase letters (not necessarily different) that represent one-letter variable names.

# Return true if it is possible to assign integers to variable names so as to satisfy all the given equations, or false otherwise.



# Example 1:

# Input: equations = ["a==b","b!=a"]
# Output: false
# Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.
# There is no way to assign the variables to satisfy both equations.
# Example 2:

# Input: equations = ["b==a","a==b"]
# Output: true
# Explanation: We could assign a = 1 and b = 1 to satisfy both equations.


# Constraints:

# 1 <= equations.length <= 500
# equations[i].length == 4
# equations[i][0] is a lowercase letter.
# equations[i][1] is either '=' or '!'.
# equations[i][2] is '='.
# equations[i][3] is a lowercase letter.
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
# ## Brute Force — Group/Component Check

```
class Solution:
    def equationsPossible(self, equations):
        graph = {chr(i + 97): [] for i in range(26)}

        for eq in equations:
            if eq[1] == '=':
                a, b = eq[0], eq[3]
                graph[a].append(b)
                graph[b].append(a)

        def connected(a, b):
            stack = [a]
            visited = set()

            while stack:
                node = stack.pop()

                if node == b:
                    return True

                if node in visited:
                    continue

                visited.add(node)

                for nei in graph[node]:
                    if nei not in visited:
                        stack.append(nei)

            return False

        for eq in equations:
            if eq[1] == '!':
                a, b = eq[0], eq[3]

                if connected(a, b):
                    return False

        return True
```

## Optimal — Union Find

```
class Solution:
    def equationsPossible(self, equations):
        parent = list(range(26))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            root_a = find(a)
            root_b = find(b)

            if root_a != root_b:
                parent[root_b] = root_a

        for eq in equations:
            if eq[1] == '=':
                a = ord(eq[0]) - ord('a')
                b = ord(eq[3]) - ord('a')
                union(a, b)

        for eq in equations:
            if eq[1] == '!':
                a = ord(eq[0]) - ord('a')
                b = ord(eq[3]) - ord('a')

                if find(a) == find(b):
                    return False

        return True
```
