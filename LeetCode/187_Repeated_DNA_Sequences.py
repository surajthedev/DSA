# The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

# For example, "ACGAATTCCG" is a DNA sequence.
# When studying DNA, it is useful to identify repeated sequences within the DNA.

# Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

 

# Example 1:

# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# Output: ["AAAAACCCCC","CCCCCAAAAA"]
# Example 2:

# Input: s = "AAAAAAAAAAAAA"
# Output: ["AAAAAAAAAA"]
 

# Constraints:

# 1 <= s.length <= 105
# s[i] is either 'A', 'C', 'G', or 'T'.





# Brute Force:
from collections import defaultdict

class Solution:
    def findRepeatedDnaSequences(self, s):
        count = defaultdict(int)

        for i in range(len(s) - 9):
            sequence = s[i:i + 10]
            count[sequence] += 1

        result = []

        for sequence, freq in count.items():
            if freq > 1:
                result.append(sequence)

        return result










# Optimal:
class Solution:
    def findRepeatedDnaSequences(self, s):
        mapping = {
            'A': 0,
            'C': 1,
            'G': 2,
            'T': 3
        }

        seen = set()
        repeated = set()

        current = 0

        for i, ch in enumerate(s):
            current = (current << 2) | mapping[ch]

            # Keep only the last 20 bits
            current &= (1 << 20) - 1

            # First 10 characters complete
            if i >= 9:
                if current in seen:
                    repeated.add(current)
                else:
                    seen.add(current)

        # Convert encoded values back to strings
        result = []

        for code in repeated:
            sequence = []

            for _ in range(10):
                value = code & 3

                if value == 0:
                    sequence.append('A')
                elif value == 1:
                    sequence.append('C')
                elif value == 2:
                    sequence.append('G')
                else:
                    sequence.append('T')

                code >>= 2

            result.append(''.join(reversed(sequence)))

        return result