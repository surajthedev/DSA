# A string is a valid parentheses string (denoted VPS) if and only if it consists of "(" and ")" characters only, and:

# It is the empty string, or
# It can be written as AB (A concatenated with B), where A and B are VPS's, or
# It can be written as (A), where A is a VPS.
# We can similarly define the nesting depth depth(S) of any VPS S as follows:

# depth("") = 0
# depth(A + B) = max(depth(A), depth(B)), where A and B are VPS's
# depth("(" + A + ")") = 1 + depth(A), where A is a VPS.
# For example, "", "()()", and "()(()())" are VPS's (with nesting depths 0, 1, and 2), and ")(" and "(()" are not VPS's.

# Given a VPS seq, split it into two disjoint subsequences A and B, such that A and B are VPS's (and A.length + B.length = seq.length). The subsequences may not necessarily be contiguous.

# For example, for the sequence 123456789, one possible split is:

# A = {1, 3, 5, 7, 9},

# B = {2, 4, 6, 8}.

# This corresponds to the output [0, 1, 0, 1, 0, 1, 0, 1, 0]  where 0 indicates membership in A and 1 indicates membership in B.

# Now choose any such A and B such that max(depth(A), depth(B)) is the minimum possible value.

# Return an answer array (of length seq.length) that encodes such a choice of A and B:  answer[i] = 0 if seq[i] is part of A, else answer[i] = 1.  Note that even though multiple answers may exist, you may return any of them.



# Example 1:

# Input: seq = "(()())"
# Output: [0,1,1,1,1,0]
# Example 2:

# Input: seq = "()(())()"
# Output: [0,0,0,1,1,0,1,1]


# Constraints:

# 1 <= seq.size <= 10000
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
# # Brute Force
from itertools import product

def max_depth(s):
    depth = 0
    max_d = 0

    for ch in s:
        if ch == '(':
            depth += 1
            max_d = max(max_d, depth)
        else:
            depth -= 1
            if depth < 0:
                return float('inf')

    return max_d if depth == 0 else float('inf')


def max_depth_split(seq, mask):
    A = ''.join(seq[i] for i in range(len(seq)) if mask[i] == 0)
    B = ''.join(seq[i] for i in range(len(seq)) if mask[i] == 1)
    return max(max_depth(A), max_depth(B))


def solve_bruteforce(seq):
    n = len(seq)
    best = None
    best_depth = float('inf')

    for mask in product((0, 1), repeat=n):
        d = max_depth_split(seq, mask)

        if d < best_depth:
            best_depth = d
            best = list(mask)

    return best






# Optimal - O(n) Time, O(1) Extra Space
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        ans = []
        depth = 0

        for ch in seq:
            if ch == '(':
                depth += 1
                ans.append(depth % 2)
            else:
                ans.append(depth % 2)
                depth -= 1

        return ans
