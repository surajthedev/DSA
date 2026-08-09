# A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

# For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
# Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

 

# Example 1:

# Input: s = "25525511135"
# Output: ["255.255.11.135","255.255.111.35"]
# Example 2:

# Input: s = "0000"
# Output: ["0.0.0.0"]
# Example 3:

# Input: s = "101023"
# Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
 

# Constraints:

# 1 <= s.length <= 20
# s consists of digits only.




# Brute force:
class Solution:
    def restoreIpAddresses(self, s):
        n = len(s)
        result = []

        # 3 dots ke positions choose karna
        for i in range(1, n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):

                    part1 = s[:i]
                    part2 = s[i:j]
                    part3 = s[j:k]
                    part4 = s[k:]

                    parts = [part1, part2, part3, part4]

                    # Har part validate karo
                    valid = True

                    for part in parts:

                        # Empty part
                        if not part:
                            valid = False
                            break

                        # Leading zero
                        if len(part) > 1 and part[0] == '0':
                            valid = False
                            break

                        # 255 se bada
                        if int(part) > 255:
                            valid = False
                            break

                    if valid:
                        result.append(".".join(parts))

        return result








# Optimal:
class Solution:
    def restoreIpAddresses(self, s):
        result = []
        n = len(s)

        def backtrack(index, parts):

            # 4 parts ban gaye
            if len(parts) == 4:
                if index == n:
                    result.append(".".join(parts))
                return

            # Remaining digits
            remaining = n - index
            remaining_parts = 4 - len(parts)

            # Pruning
            if remaining < remaining_parts:
                return

            if remaining > 3 * remaining_parts:
                return

            # Current segment maximum 3 digits
            for end in range(index, min(index + 3, n)):

                # Leading zero
                if s[index] == '0' and end > index:
                    break

                segment = s[index:end + 1]

                # Value 255 se zyada
                if int(segment) > 255:
                    continue

                # Choose
                parts.append(segment)

                # Explore
                backtrack(end + 1, parts)

                # Undo
                parts.pop()

        backtrack(0, [])

        return result