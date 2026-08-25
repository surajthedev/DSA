# A password is considered strong if the below conditions are all met:

# It has at least 6 characters and at most 20 characters.
# It contains at least one lowercase letter, at least one uppercase letter, and at least one digit.
# It does not contain three repeating characters in a row (i.e., "Baaabb0" is weak, but "Baaba0" is strong).
# Given a string password, return the minimum number of steps required to make password strong. if password is already strong, return 0.

# In one step, you can:

# Insert one character to password,
# Delete one character from password, or
# Replace one character of password with another character.
 

# Example 1:

# Input: password = "a"
# Output: 5
# Example 2:

# Input: password = "aA1"
# Output: 3
# Example 3:

# Input: password = "1337C0d3"
# Output: 0
 

# Constraints:

# 1 <= password.length <= 50
# password consists of letters, digits, dot '.' or exclamation mark '!'.






# Solution:
class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)

        # 1. Count missing character types
        missing = 0

        if not any(c.islower() for c in password):
            missing += 1

        if not any(c.isupper() for c in password):
            missing += 1

        if not any(c.isdigit() for c in password):
            missing += 1

        # 2. Find repeating groups
        groups = []

        i = 0

        while i < n:
            j = i

            while j < n and password[j] == password[i]:
                j += 1

            length = j - i

            if length >= 3:
                groups.append(length)

            i = j

        # Number of replacements without deletions
        replacements = sum(length // 3 for length in groups)

        # Case 1: Too short
        if n < 6:
            return max(6 - n, missing)

        # Case 2: Valid length
        if n <= 20:
            return max(missing, replacements)

        # Case 3: Too long
        deletions = n - 20

        # ---------------------------------
        # First priority:
        # length % 3 == 0
        #
        # 1 deletion saves 1 replacement
        # ---------------------------------
        for i in range(len(groups)):
            if deletions == 0:
                break

            if groups[i] % 3 == 0:
                groups[i] -= 1
                deletions -= 1
                replacements -= 1

        # ---------------------------------
        # Second priority:
        # length % 3 == 1
        #
        # 2 deletions save 1 replacement
        # ---------------------------------
        for i in range(len(groups)):
            if deletions < 2:
                break

            if groups[i] % 3 == 1:
                use = min(2, deletions)

                groups[i] -= use
                deletions -= use

                replacements -= use // 2

        # ---------------------------------
        # Remaining deletions:
        #
        # 3 deletions save 1 replacement
        # ---------------------------------
        for i in range(len(groups)):
            if deletions < 3:
                break

            if groups[i] >= 3:
                use = min(
                    deletions,
                    groups[i] - 2
                )

                groups[i] -= use
                deletions -= use

                replacements -= use // 3

        return (n - 20) + max(missing, replacements)