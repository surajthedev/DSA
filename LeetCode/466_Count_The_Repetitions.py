# We define str = [s, n] as the string str which consists of the string s concatenated n times.

# For example, str == ["abc", 3] =="abcabcabc".
# We define that string s1 can be obtained from string s2 if we can remove some characters from s2 such that it becomes s1.

# For example, s1 = "abc" can be obtained from s2 = "abdbec" based on our definition by removing the bolded underlined characters.
# You are given two strings s1 and s2 and two integers n1 and n2. You have the two strings str1 = [s1, n1] and str2 = [s2, n2].

# Return the maximum integer m such that str = [str2, m] can be obtained from str1.

 

# Example 1:

# Input: s1 = "acb", n1 = 4, s2 = "ab", n2 = 2
# Output: 2
# Example 2:

# Input: s1 = "acb", n1 = 1, s2 = "acb", n2 = 1
# Output: 1
 

# Constraints:

# 1 <= s1.length, s2.length <= 100
# s1 and s2 consist of lowercase English letters.
# 1 <= n1, n2 <= 106






# Brute force:
class Solution:
    def getMaxRepetitions(self, s1, n1, s2, n2):

        # Build the actual string
        source = s1 * n1

        i = 0
        count_s2 = 0

        for ch in source:

            if ch == s2[i]:
                i += 1

                # Complete one s2
                if i == len(s2):
                    count_s2 += 1
                    i = 0

        return count_s2 // n2






# Optimal:
class Solution:
    def getMaxRepetitions(self, s1, n1, s2, n2):

        # If s2 contains a character that doesn't exist in s1,
        # even one s2 can never be formed.
        for ch in s2:
            if ch not in s1:
                return 0

        # position in s2
        index = 0

        # Number of complete s2 copies found
        count_s2 = 0

        # Number of s1 blocks processed
        count_s1 = 0

        # index -> (count_s1, count_s2)
        seen = {}

        while count_s1 < n1:

            # Process one complete s1
            for ch in s1:

                if ch == s2[index]:
                    index += 1

                    # One complete s2 found
                    if index == len(s2):
                        index = 0
                        count_s2 += 1

            count_s1 += 1

            # Have we seen this state before?
            if index in seen:

                prev_s1, prev_s2 = seen[index]

                # Length of one cycle
                cycle_s1 = count_s1 - prev_s1
                cycle_s2 = count_s2 - prev_s2

                # How many complete cycles can we skip?
                cycles = (n1 - count_s1) // cycle_s1

                if cycles > 0:
                    count_s1 += cycles * cycle_s1
                    count_s2 += cycles * cycle_s2

            else:
                seen[index] = (count_s1, count_s2)

        return count_s2 // n2