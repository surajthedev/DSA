# In a string s of lowercase letters, these letters form consecutive groups of the same character.

# For example, a string like s = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z", and "yy".

# A group is identified by an interval [start, end], where start and end denote the start and end indices (inclusive) of the group. In the above example, "xxxx" has the interval [3,6].

# A group is considered large if it has 3 or more characters.

# Return the intervals of every large group sorted in increasing order by start index.



# Example 1:

# Input: s = "abbxxxxzzy"
# Output: [[3,6]]
# Explanation: "xxxx" is the only large group with start index 3 and end index 6.
# Example 2:

# Input: s = "abc"
# Output: []
# Explanation: We have groups "a", "b", and "c", none of which are large groups.
# Example 3:

# Input: s = "abcdddeeeeaabbbcd"
# Output: [[3,5],[6,9],[12,14]]
# Explanation: The large groups are "ddd", "eeee", and "bbb".


# Constraints:

# 1 <= s.length <= 1000
# s contains lowercase English letters only.
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
    def largeGroupPositions(self, s):
        n = len(s)
        ans = []

        for i in range(n):
            j = i

            while j < n and s[j] == s[i]:
                j += 1

            if j - i >= 3:
                ans.append([i, j - 1])

            i = j

        return ans









# Optimal:
# class Solution:
    def largeGroupPositions(self, s):
        ans = []
        start = 0

        for i in range(1, len(s) + 1):
            if i == len(s) or s[i] != s[start]:
                if i - start >= 3:
                    ans.append([start, i - 1])

                start = i

        return ans
