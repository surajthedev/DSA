# You are given two strings s and target, each of length n, consisting of lowercase English letters.

# Return the lexicographically smallest string that is both a palindromic permutation of s and strictly greater than target. If no such permutation exists, return an empty string.

 

# Example 1:

# Input: s = "baba", target = "abba"

# Output: "baab"

# Explanation:

# The palindromic permutations of s (in lexicographical order) are "abba" and "baab".
# The lexicographically smallest permutation that is strictly greater than target is "baab".
# Example 2:

# Input: s = "baba", target = "bbaa"

# Output: ""

# Explanation:

# The palindromic permutations of s (in lexicographical order) are "abba" and "baab".
# None of them is lexicographically strictly greater than target. Therefore, the answer is "".
# Example 3:

# Input: s = "abc", target = "abb"

# Output: ""

# Explanation:

# s has no palindromic permutations. Therefore, the answer is "".

# Example 4:

# Input: s = "aac", target = "abb"

# Output: "aca"

# Explanation:

# The only palindromic permutation of s is "aca".
# "aca" is strictly greater than target. Therefore, the answer is "aca".
 

# Constraints:

# 1 <= n == s.length == target.length <= 300
# s and target consist of only lowercase English letters.




# Brute force:
class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # Count frequencies
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        # Check whether palindrome is possible
        odd = 0
        middle = ""

        for i in range(26):
            if cnt[i] % 2:
                odd += 1
                middle = chr(i + ord('a'))

        if odd > 1:
            return ""

        # Build counts for left half
        half_cnt = [x // 2 for x in cnt]
        half_len = n // 2

        ans = None
        half = []

        def build_palindrome():
            left = "".join(half)
            return left + middle + left[::-1]

        def backtrack():
            nonlocal ans

            if len(half) == half_len:
                pal = build_palindrome()

                if pal > target:
                    if ans is None or pal < ans:
                        ans = pal

                return

            for c in range(26):
                if half_cnt[c] == 0:
                    continue

                half_cnt[c] -= 1
                half.append(chr(c + ord('a')))

                backtrack()

                half.pop()
                half_cnt[c] += 1

        backtrack()

        return ans if ans is not None else ""






# Optimal:
class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # --------------------------------------------------
        # Step 1: Count characters
        # --------------------------------------------------
        cnt = [0] * 26

        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        # --------------------------------------------------
        # Step 2: Check if palindrome is possible
        # --------------------------------------------------
        middle = ""

        for i in range(26):
            if cnt[i] % 2:
                if middle:
                    # More than one odd frequency
                    return ""

                middle = chr(ord('a') + i)

        # --------------------------------------------------
        # Step 3: Counts available for the left half
        # --------------------------------------------------
        half_cnt = [x // 2 for x in cnt]

        half_len = n // 2
        prefix = []

        # --------------------------------------------------
        # Build the maximum possible palindrome using
        # current prefix + remaining characters.
        # --------------------------------------------------
        def max_palindrome():
            # Use largest available characters first
            remaining = []

            for c in range(25, -1, -1):
                remaining.extend(
                    [chr(ord('a') + c)] * half_cnt[c]
                )

            left = "".join(prefix) + "".join(remaining)

            return left + middle + left[::-1]

        # --------------------------------------------------
        # Greedily construct the smallest possible left half
        # --------------------------------------------------
        for pos in range(half_len):

            chosen = False

            # Try smallest character first
            for c in range(26):

                if half_cnt[c] == 0:
                    continue

                ch = chr(ord('a') + c)

                # Temporarily choose this character
                prefix.append(ch)
                half_cnt[c] -= 1

                # Is there ANY valid completion?
                if max_palindrome() > target:
                    chosen = True
                    break

                # This character cannot lead to an answer
                half_cnt[c] += 1
                prefix.pop()

            if not chosen:
                return ""

        # --------------------------------------------------
        # Construct final palindrome
        # --------------------------------------------------
        left = "".join(prefix)

        answer = left + middle + left[::-1]

        return answer if answer > target else ""