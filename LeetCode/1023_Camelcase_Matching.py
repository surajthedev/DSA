# Given an array of strings queries and a string pattern, return a boolean array answer where answer[i] is true if queries[i] matches pattern, and false otherwise.

# A query word queries[i] matches pattern if you can insert lowercase English letters into the pattern so that it equals the query. You may insert a character at any position in pattern or you may choose not to insert any characters at all.



# Example 1:

# Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"
# Output: [true,false,true,true,false]
# Explanation: "FooBar" can be generated like this "F" + "oo" + "B" + "ar".
# "FootBall" can be generated like this "F" + "oot" + "B" + "all".
# "FrameBuffer" can be generated like this "F" + "rame" + "B" + "uffer".
# Example 2:

# Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa"
# Output: [true,false,true,false,false]
# Explanation: "FooBar" can be generated like this "Fo" + "o" + "Ba" + "r".
# "FootBall" can be generated like this "Fo" + "ot" + "Ba" + "ll".
# Example 3:

# Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBaT"
# Output: [false,true,false,false,false]
# Explanation: "FooBarTest" can be generated like this "Fo" + "o" + "Ba" + "r" + "T" + "est".


# Constraints:

# 1 <= pattern.length, queries.length <= 100
# 1 <= queries[i].length <= 100
# queries[i] and pattern consist of English letters.
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
# ### Brute Force

python
```

class Solution:
    def camelMatch(self, queries: list[str], pattern: str) -> list[bool]:
        ans = []

        for query in queries:
            i = 0
            valid = True

            for ch in query:
                if i < len(pattern) and ch == pattern[i]:
                    i += 1
                elif ch.isupper():
                    valid = False
                    break

            ans.append(valid and i == len(pattern))

        return ans
```

### Optimal — Two Pointers

python
```

class Solution:
    def camelMatch(self, queries: list[str], pattern: str) -> list[bool]:
        def match(query):
            i = 0
            j = 0

            while i < len(query):
                if j < len(pattern) and query[i] == pattern[j]:
                    j += 1
                elif query[i].isupper():
                    return False

                i += 1

            return j == len(pattern)

        return [match(query) for query in queries]
```
