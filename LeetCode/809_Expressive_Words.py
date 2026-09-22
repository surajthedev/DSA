# Sometimes people repeat letters to represent extra feeling. For example:

# "hello" -> "heeellooo"
# "hi" -> "hiiii"
# In these strings like "heeellooo", we have groups of adjacent letters that are all the same: "h", "eee", "ll", "ooo".

# You are given a string s and an array of query strings words. A query word is stretchy if it can be made to be equal to s by any number of applications of the following extension operation: choose a group consisting of characters c, and add some number of characters c to the group so that the size of the group is three or more.

# For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get "helloo" since the group "oo" has a size less than three. Also, we could do another extension like "ll" -> "lllll" to get "helllllooo". If s = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = s.
# Return the number of query strings that are stretchy.



# Example 1:

# Input: s = "heeellooo", words = ["hello", "hi", "helo"]
# Output: 1
# Explanation:
# We can extend "e" and "o" in the word "hello" to get "heeellooo".
# We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.
# Example 2:

# Input: s = "zzzzzyyyyy", words = ["zzyy","zy","zyy"]
# Output: 3


# Constraints:

# 1 <= s.length, words.length <= 100
# 1 <= words[i].length <= 100
# s and words[i] consist of lowercase letters.
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
    def expressiveWords(self, s, words):
        def is_stretchy(word):
            i = j = 0

            while i < len(s) and j < len(word):
                if s[i] != word[j]:
                    return False

                si = i
                wj = j

                while i < len(s) and s[i] == s[si]:
                    i += 1

                while j < len(word) and word[j] == word[wj]:
                    j += 1

                s_count = i - si
                w_count = j - wj

                if w_count > s_count:
                    return False

                if s_count != w_count and s_count < 3:
                    return False

            return i == len(s) and j == len(word)

        count = 0

        for word in words:
            if is_stretchy(word):
                count += 1

        return count








# Optimal:
class Solution:
    def expressiveWords(self, s, words):
        def get_groups(word):
            groups = []
            i = 0

            while i < len(word):
                j = i

                while j < len(word) and word[j] == word[i]:
                    j += 1

                groups.append((word[i], j - i))
                i = j

            return groups

        s_groups = get_groups(s)
        ans = 0

        for word in words:
            w_groups = get_groups(word)

            if len(s_groups) != len(w_groups):
                continue

            valid = True

            for (sc, sn), (wc, wn) in zip(s_groups, w_groups):
                if sc != wc or wn > sn:
                    valid = False
                    break

                if sn != wn and sn < 3:
                    valid = False
                    break

            if valid:
                ans += 1

        return ans
