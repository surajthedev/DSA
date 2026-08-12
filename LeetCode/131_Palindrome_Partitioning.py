# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

 

# Example 1:

# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
# Example 2:

# Input: s = "a"
# Output: [["a"]]
 

# Constraints:

# 1 <= s.length <= 16
# s contains only lowercase English letters.





# brute force:
class Solution:
    def partition(self, s):
        result = []

        def is_palindrome(word):
            return word == word[::-1]

        def generate(index, path):
            if index == len(s):
                # Check complete partition
                for word in path:
                    if not is_palindrome(word):
                        return

                result.append(path[:])
                return

            # Try every possible next substring
            for end in range(index + 1, len(s) + 1):
                substring = s[index:end]

                path.append(substring)
                generate(end, path)
                path.pop()

        generate(0, [])

        return result







# Optimal:
class Solution:
    def partition(self, s):
        result = []
        path = []

        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False

                left += 1
                right -= 1

            return True

        def backtrack(start):
            # Entire string partition ho gayi
            if start == len(s):
                result.append(path[:])
                return

            # Try every possible substring
            for end in range(start, len(s)):

                if is_palindrome(start, end):

                    # Choose
                    path.append(s[start:end + 1])

                    # Explore
                    backtrack(end + 1)

                    # Undo
                    path.pop()

        backtrack(0)

        return result