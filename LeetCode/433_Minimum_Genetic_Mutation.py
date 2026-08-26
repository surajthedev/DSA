# A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

# Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is defined as one single character changed in the gene string.

# For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
# There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

# Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed to mutate from startGene to endGene. If there is no such a mutation, return -1.

# Note that the starting point is assumed to be valid, so it might not be included in the bank.

 

# Example 1:

# Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
# Output: 1
# Example 2:

# Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
# Output: 2
 

# Constraints:

# 0 <= bank.length <= 10
# startGene.length == endGene.length == bank[i].length == 8
# startGene, endGene, and bank[i] consist of only the characters ['A', 'C', 'G', 'T'].






# Brute force:
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:

        bank = set(bank)

        if endGene not in bank:
            return -1

        visited = set()
        visited.add(startGene)

        chars = ['A', 'C', 'G', 'T']

        ans = float('inf')

        def dfs(gene, mutations):
            nonlocal ans

            if gene == endGene:
                ans = min(ans, mutations)
                return

            # Already current best se worse hai
            if mutations >= ans:
                return

            for i in range(8):
                original = gene[i]

                for ch in chars:
                    if ch == original:
                        continue

                    new_gene = gene[:i] + ch + gene[i + 1:]

                    if new_gene in bank and new_gene not in visited:
                        visited.add(new_gene)

                        dfs(new_gene, mutations + 1)

                        visited.remove(new_gene)

        dfs(startGene, 0)

        return -1 if ans == float('inf') else ans







# Optimal:
from collections import deque


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:

        bank = set(bank)

        # End gene valid hi nahi hai
        if endGene not in bank:
            return -1

        queue = deque([(startGene, 0)])

        visited = {startGene}

        chars = ['A', 'C', 'G', 'T']

        while queue:

            gene, mutations = queue.popleft()

            if gene == endGene:
                return mutations

            for i in range(8):
                for ch in chars:

                    if ch == gene[i]:
                        continue

                    new_gene = gene[:i] + ch + gene[i + 1:]

                    # Sirf valid aur unvisited genes
                    if new_gene in bank and new_gene not in visited:
                        visited.add(new_gene)

                        queue.append(
                            (new_gene, mutations + 1)
                        )

        return -1