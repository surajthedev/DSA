# Given a string s containing an out-of-order English representation of digits 0-9, return the digits in ascending order.

 

# Example 1:

# Input: s = "owoztneoer"
# Output: "012"
# Example 2:

# Input: s = "fviefuro"
# Output: "45"
 

# Constraints:

# 1 <= s.length <= 105
# s[i] is one of the characters ["e","g","f","i","h","o","n","s","r","u","t","w","v","x","z"].
# s is guaranteed to be valid.




# Brute force:
from collections import Counter

class Solution:
    def originalDigits(self, s):
        count = Counter(s)

        ans = [0] * 10

        # Unique characters
        ans[0] = count['z']          # zero
        ans[2] = count['w']          # two
        ans[4] = count['u']          # four
        ans[6] = count['x']          # six
        ans[8] = count['g']          # eight

        # Remove their contribution
        count['o'] -= ans[0] + ans[2]
        count['f'] -= ans[4]
        count['s'] -= ans[6]
        count['h'] -= ans[8]

        # Remaining digits
        ans[1] = count['o']          # one
        ans[3] = count['h']          # three
        ans[5] = count['f']          # five
        ans[7] = count['s']          # seven

        count['i'] -= ans[5] + ans[6] + ans[8]
        ans[9] = count['i']          # nine

        return ''.join(str(i) * ans[i] for i in range(10))






# Optimal:
from collections import Counter

class Solution:
    def originalDigits(self, s):
        count = Counter(s)

        digits = [0] * 10

        # Unique characters
        digits[0] = count['z']  # zero
        digits[2] = count['w']  # two
        digits[4] = count['u']  # four
        digits[6] = count['x']  # six
        digits[8] = count['g']  # eight

        # Remaining digits
        digits[1] = count['o'] - digits[0] - digits[2] - digits[4]
        digits[3] = count['h'] - digits[8]
        digits[5] = count['f'] - digits[4]
        digits[7] = count['s'] - digits[6]

        digits[9] = count['i'] - digits[5] - digits[6] - digits[8]

        return ''.join(str(i) * digits[i] for i in range(10))