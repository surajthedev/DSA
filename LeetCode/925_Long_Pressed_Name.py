# Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

# You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.



# Example 1:

# Input: name = "alex", typed = "aaleex"
# Output: true
# Explanation: 'a' and 'e' in 'alex' were long pressed.
# Example 2:

# Input: name = "saeed", typed = "ssaaedd"
# Output: false
# Explanation: 'e' must have been pressed twice, but it was not in the typed output.


# Constraints:

# 1 <= name.length, typed.length <= 1000
# name and typed consist of only lowercase English letters.
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
# Brute force:
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        j = 0

        while i < len(name):
            if j >= len(typed) or name[i] != typed[j]:
                return False

            count = 1
            j += 1

            while j < len(typed) and typed[j] == name[i]:
                count += 1
                j += 1

            if i + 1 < len(name) and name[i + 1] == name[i]:
                i += 1
                continue

            i += 1

        return j == len(typed)











# Optimal:
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = j = 0

        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                i += 1
            elif j == 0 or typed[j] != typed[j - 1]:
                return False

            j += 1

        return i == len(name)
