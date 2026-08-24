# Given a 32-bit integer num, return a string representing its hexadecimal representation. For negative integers, two’s complement method is used.

# All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.

# Note: You are not allowed to use any built-in library method to directly solve this problem.

 

# Example 1:

# Input: num = 26
# Output: "1a"
# Example 2:

# Input: num = -1
# Output: "ffffffff"
 

# Constraints:

# -231 <= num <= 231 - 1






# Solution:
class Solution:
    def toHex(self, num: int) -> str:

        if num == 0:
            return "0"

        # Convert negative number to 32-bit
        # two's complement representation
        if num < 0:
            num &= 0xffffffff

        hex_chars = "0123456789abcdef"
        result = []

        while num > 0:
            # Get last 4 bits
            digit = num & 15

            # Convert 0-15 to hex character
            result.append(hex_chars[digit])

            # Remove last 4 bits
            num >>= 4

        # We extracted digits from right to left
        result.reverse()

        return "".join(result)