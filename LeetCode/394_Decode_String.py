# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

# The test cases are generated so that the length of the output will never exceed 105.

 

# Example 1:

# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
# Example 2:

# Input: s = "3[a2[c]]"
# Output: "accaccacc"
# Example 3:

# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"
 

# Constraints:

# 1 <= s.length <= 30
# s consists of lowercase English letters, digits, and square brackets '[]'.
# s is guaranteed to be a valid input.
# All the integers in s are in the range [1, 300].






# Brute force:
class Solution:
    def decodeString(self, s: str) -> str:

        def decode(i):
            result = []
            num = 0

            while i < len(s) and s[i] != ']':
                if s[i].isdigit():
                    num = 0

                    while i < len(s) and s[i].isdigit():
                        num = num * 10 + int(s[i])
                        i += 1

                elif s[i] == '[':
                    # Decode everything inside []
                    decoded, i = decode(i + 1)

                    result.append(decoded * num)
                    num = 0

                else:
                    result.append(s[i])
                    i += 1

            return ''.join(result), i + 1

        return decode(0)[0]





# Optimal:
class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        string_stack = []

        current = ""
        num = 0

        for char in s:

            # Build the number
            if char.isdigit():
                num = num * 10 + int(char)

            # Save current state
            elif char == '[':
                num_stack.append(num)
                string_stack.append(current)

                num = 0
                current = ""

            # Decode current bracket
            elif char == ']':
                repeat = num_stack.pop()
                previous = string_stack.pop()

                current = previous + current * repeat

            # Normal character
            else:
                current += char

        return current