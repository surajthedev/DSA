# Given an integer array data representing the data, return whether it is a valid UTF-8 encoding (i.e. it translates to a sequence of valid UTF-8 encoded characters).

# A character in UTF8 can be from 1 to 4 bytes long, subjected to the following rules:

# For a 1-byte character, the first bit is a 0, followed by its Unicode code.
# For an n-bytes character, the first n bits are all one's, the n + 1 bit is 0, followed by n - 1 bytes with the most significant 2 bits being 10.
# This is how the UTF-8 encoding would work:

#      Number of Bytes   |        UTF-8 Octet Sequence
#                        |              (binary)
#    --------------------+-----------------------------------------
#             1          |   0xxxxxxx
#             2          |   110xxxxx 10xxxxxx
#             3          |   1110xxxx 10xxxxxx 10xxxxxx
#             4          |   11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
# x denotes a bit in the binary form of a byte that may be either 0 or 1.

# Note: The input is an array of integers. Only the least significant 8 bits of each integer is used to store the data. This means each integer represents only 1 byte of data.

 

# Example 1:

# Input: data = [197,130,1]
# Output: true
# Explanation: data represents the octet sequence: 11000101 10000010 00000001.
# It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte character.
# Example 2:

# Input: data = [235,140,4]
# Output: false
# Explanation: data represented the octet sequence: 11101011 10001100 00000100.
# The first 3 bits are all one's and the 4th bit is 0 means it is a 3-bytes character.
# The next byte is a continuation byte which starts with 10 and that's correct.
# But the second continuation byte does not start with 10, so it is invalid.
 

# Constraints:

# 1 <= data.length <= 2 * 104
# 0 <= data[i] <= 255







# Brute force:
class Solution:
    def validUtf8(self, data: list[int]) -> bool:
        i = 0

        while i < len(data):
            byte = format(data[i], '08b')

            # 1-byte character
            if byte[0] == '0':
                i += 1

            # 2-byte character
            elif byte.startswith('110'):
                if i + 1 >= len(data):
                    return False

                if not format(data[i + 1], '08b').startswith('10'):
                    return False

                i += 2

            # 3-byte character
            elif byte.startswith('1110'):
                if i + 2 >= len(data):
                    return False

                if not format(data[i + 1], '08b').startswith('10'):
                    return False

                if not format(data[i + 2], '08b').startswith('10'):
                    return False

                i += 3

            # 4-byte character
            elif byte.startswith('11110'):
                if i + 3 >= len(data):
                    return False

                if not format(data[i + 1], '08b').startswith('10'):
                    return False

                if not format(data[i + 2], '08b').startswith('10'):
                    return False

                if not format(data[i + 3], '08b').startswith('10'):
                    return False

                i += 4

            else:
                return False

        return True








# Optimal:
class Solution:
    def validUtf8(self, data: list[int]) -> bool:
        remaining = 0

        for byte in data:

            # We are expecting continuation bytes
            if remaining > 0:
                if (byte >> 6) != 0b10:
                    return False

                remaining -= 1

            # 1-byte character: 0xxxxxxx
            elif (byte >> 7) == 0:
                remaining = 0

            # 2-byte character: 110xxxxx
            elif (byte >> 5) == 0b110:
                remaining = 1

            # 3-byte character: 1110xxxx
            elif (byte >> 4) == 0b1110:
                remaining = 2

            # 4-byte character: 11110xxx
            elif (byte >> 3) == 0b11110:
                remaining = 3

            # Invalid starting byte
            else:
                return False

        # If continuation bytes are still required,
        # encoding is incomplete.
        return remaining == 0