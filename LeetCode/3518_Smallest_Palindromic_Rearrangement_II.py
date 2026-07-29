# You are given a palindromic string s and an integer k.

# Return the k-th lexicographically smallest palindromic permutation of s. If there are fewer than k distinct palindromic permutations, return an empty string.

# Note: Different rearrangements that yield the same palindromic string are considered identical and are counted once.

 

# Example 1:

# Input: s = "abba", k = 2

# Output: "baab"

# Explanation:

# The two distinct palindromic rearrangements of "abba" are "abba" and "baab".
# Lexicographically, "abba" comes before "baab". Since k = 2, the output is "baab".
# Example 2:

# Input: s = "aa", k = 2

# Output: ""

# Explanation:

# There is only one palindromic rearrangement: "aa".
# The output is an empty string since k = 2 exceeds the number of possible rearrangements.
# Example 3:

# Input: s = "bacab", k = 1

# Output: "abcba"

# Explanation:

# The two distinct palindromic rearrangements of "bacab" are "abcba" and "bacab".
# Lexicographically, "abcba" comes before "bacab". Since k = 1, the output is "abcba".
 

# Constraints:

# 1 <= s.length <= 104
# s consists of lowercase English letters.
# s is guaranteed to be palindromic.
# 1 <= k <= 106




# Optimal Solution:
class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        from collections import Counter

        cnt = Counter(s)

        # Jis character ka count odd hai, wahi middle mein jayega
        odd_chars = [c for c, v in cnt.items() if v % 2 == 1]
        middle = odd_chars[0] if odd_chars else ''

        # Sirf half part ko arrange karna hai
        half_counts = {c: v // 2 for c, v in cnt.items()}
        half_len = sum(half_counts.values())

        CAP = k  # k se zyada precision kabhi nahi chahiye

        def capped_comb(n, r, cap):
            if r < 0 or r > n:
                return 0
            r = min(r, n - r)
            result = 1
            for i in range(1, r + 1):
                result = result * (n - r + i) // i
                if result > cap:
                    return cap + 1
            return result

        def count_arrangements(counts, length, cap):
            remaining = length
            total = 1
            for v in counts.values():
                if v == 0:
                    continue
                c = capped_comb(remaining, v, cap)
                total *= c
                if total > cap:
                    return cap + 1
                remaining -= v
            return total

        total = count_arrangements(half_counts, half_len, CAP)
        if k > total:
            return ""

        chars = sorted(half_counts.keys())
        result = []
        remaining = dict(half_counts)
        remaining_len = half_len
        k -= 1

        for _ in range(half_len):
            for c in chars:
                if remaining[c] == 0:
                    continue
                remaining[c] -= 1
                remaining_len -= 1
                perms = count_arrangements(remaining, remaining_len, CAP)
                if k < perms:
                    result.append(c)
                    break
                else:
                    k -= perms
                    remaining[c] += 1
                    remaining_len += 1

        half = ''.join(result)
        return half + middle + half[::-1]