# You are given a 0-indexed string s. You are also given a 0-indexed string queryCharacters of length k and a 0-indexed array of integer indices queryIndices of length k, both of which are used to describe k queries.

# The ith query updates the character in s at index queryIndices[i] to the character queryCharacters[i].

# Return an array lengths of length k where lengths[i] is the length of the longest substring of s consisting of only one repeating character after the ith query is performed.

 

# Example 1:

# Input: s = "babacc", queryCharacters = "bcb", queryIndices = [1,3,3]
# Output: [3,3,4]
# Explanation: 
# - 1st query updates s = "bbbacc". The longest substring consisting of one repeating character is "bbb" with length 3.
# - 2nd query updates s = "bbbccc". 
#   The longest substring consisting of one repeating character can be "bbb" or "ccc" with length 3.
# - 3rd query updates s = "bbbbcc". The longest substring consisting of one repeating character is "bbbb" with length 4.
# Thus, we return [3,3,4].
# Example 2:

# Input: s = "abyzz", queryCharacters = "aa", queryIndices = [2,1]
# Output: [2,3]
# Explanation:
# - 1st query updates s = "abazz". The longest substring consisting of one repeating character is "zz" with length 2.
# - 2nd query updates s = "aaazz". The longest substring consisting of one repeating character is "aaa" with length 3.
# Thus, we return [2,3].
 

# Constraints:

# 1 <= s.length <= 105
# s consists of lowercase English letters.
# k == queryCharacters.length == queryIndices.length
# 1 <= k <= 105
# queryCharacters consists of lowercase English letters.
# 0 <= queryIndices[i] < s.length







# Brute force:
class Solution:
    def longestRepeating(self, s, queryCharacters, queryIndices):
        s = list(s)
        ans = []

        for ch, idx in zip(queryCharacters, queryIndices):
            # Update
            s[idx] = ch

            # Find longest repeating substring
            max_len = 1
            curr_len = 1

            for i in range(1, len(s)):
                if s[i] == s[i - 1]:
                    curr_len += 1
                else:
                    curr_len = 1

                max_len = max(max_len, curr_len)

            ans.append(max_len)

        return ans







# Optimal:
class Solution:
    def longestRepeating(self, s, queryCharacters, queryIndices):
        n = len(s)

        # Segment tree node:
        # [left_char, right_char, prefix, suffix, best, length]
        tree = [None] * (4 * n)

        def build(node, left, right):
            if left == right:
                tree[node] = [
                    s[left],  # left_char
                    s[left],  # right_char
                    1,        # prefix
                    1,        # suffix
                    1,        # best
                    1         # length
                ]
                return

            mid = (left + right) // 2

            build(node * 2, left, mid)
            build(node * 2 + 1, mid + 1, right)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        def merge(a, b):
            left_char = a[0]
            right_char = b[1]

            prefix = a[2]
            suffix = b[3]

            best = max(a[4], b[4])

            # Boundary characters are same,
            # so suffix of left + prefix of right can combine.
            if a[1] == b[0]:
                best = max(best, a[3] + b[2])

                # If entire left segment has same character
                if a[2] == a[5]:
                    prefix = a[5] + b[2]

                # If entire right segment has same character
                if b[3] == b[5]:
                    suffix = b[5] + a[3]

            length = a[5] + b[5]

            return [
                left_char,
                right_char,
                prefix,
                suffix,
                best,
                length
            ]

        def update(node, left, right, idx, ch):
            if left == right:
                tree[node] = [
                    ch,
                    ch,
                    1,
                    1,
                    1,
                    1
                ]
                return

            mid = (left + right) // 2

            if idx <= mid:
                update(node * 2, left, mid, idx, ch)
            else:
                update(node * 2 + 1, mid + 1, right, idx, ch)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        # Build initial segment tree
        build(1, 0, n - 1)

        ans = []

        for ch, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, ch)

            # Root contains answer for entire string
            ans.append(tree[1][4])

        return ans