# Alice and Bob take turns playing a game, with Alice starting first.

# You are given a string num of even length consisting of digits and '?' characters. On each turn, a player will do the following if there is still at least one '?' in num:

# Choose an index i where num[i] == '?'.
# Replace num[i] with any digit between '0' and '9'.
# The game ends when there are no more '?' characters in num.

# For Bob to win, the sum of the digits in the first half of num must be equal to the sum of the digits in the second half. For Alice to win, the sums must not be equal.

# For example, if the game ended with num = "243801", then Bob wins because 2+4+3 = 8+0+1. If the game ended with num = "243803", then Alice wins because 2+4+3 != 8+0+3.
# Assuming Alice and Bob play optimally, return true if Alice will win and false if Bob will win.

 

# Example 1:

# Input: num = "5023"
# Output: false
# Explanation: There are no moves to be made.
# The sum of the first half is equal to the sum of the second half: 5 + 0 = 2 + 3.
# Example 2:

# Input: num = "25??"
# Output: true
# Explanation: Alice can replace one of the '?'s with '9' and it will be impossible for Bob to make the sums equal.
# Example 3:

# Input: num = "?3295???"
# Output: false
# Explanation: It can be proven that Bob will always win. One possible outcome is:
# - Alice replaces the first '?' with '9'. num = "93295???".
# - Bob replaces one of the '?' in the right half with '9'. num = "932959??".
# - Alice replaces one of the '?' in the right half with '2'. num = "9329592?".
# - Bob replaces the last '?' in the right half with '7'. num = "93295927".
# Bob wins because 9 + 3 + 2 + 9 = 5 + 9 + 2 + 7.
 

# Constraints:

# 2 <= num.length <= 105
# num.length is even.
# num consists of only digits and '?'.





# Brute force:
class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2

        def dfs(s, alice_turn):
            # Base case:
            # Saare '?' fill ho gaye
            if '?' not in s:
                left_sum = 0
                right_sum = 0

                for i in range(half):
                    left_sum += int(s[i])

                for i in range(half, n):
                    right_sum += int(s[i])

                # True  -> Alice wins
                # False -> Bob wins
                return left_sum != right_sum

            # -------------------------
            # Alice's turn
            # -------------------------
            if alice_turn:

                # Alice ko sirf ek winning move chahiye
                for i in range(n):

                    if s[i] == '?':

                        # Try digits 0 to 9
                        for digit in '0123456789':

                            new_s = (
                                s[:i]
                                + digit
                                + s[i + 1:]
                            )

                            # Agar is move ke baad
                            # Alice eventually jeet sakti hai
                            if dfs(new_s, False):
                                return True

                # Alice ke paas koi winning move nahi
                return False

            # -------------------------
            # Bob's turn
            # -------------------------
            else:

                # Bob ko sirf ek aisi move chahiye
                # jisme Alice haar jaaye
                for i in range(n):

                    if s[i] == '?':

                        for digit in '0123456789':

                            new_s = (
                                s[:i]
                                + digit
                                + s[i + 1:]
                            )

                            # Agar Bob is move ke baad
                            # Alice ko hara sakta hai
                            if not dfs(new_s, True):
                                return False

                # Bob ke paas Alice ko harane wali
                # koi move nahi hai
                return True

        # Alice first move karti hai
        return dfs(num, True)






# Optimal:
class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2

        left_sum = 0
        right_sum = 0

        left_q = 0
        right_q = 0

        # Left half
        for i in range(half):
            if num[i] == '?':
                left_q += 1
            else:
                left_sum += int(num[i])

        # Right half
        for i in range(half, n):
            if num[i] == '?':
                right_q += 1
            else:
                right_sum += int(num[i])

        # Odd number of '?' -> Alice gets the last move
        if (left_q + right_q) % 2 == 1:
            return True

        # Bob can win only if the fixed sum difference
        # can be exactly compensated by the '?'s.
        return left_sum - right_sum != 9 * (right_q - left_q) // 2