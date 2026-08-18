# You are playing the Bulls and Cows game with your friend.

# You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

# The number of "bulls", which are digits in the guess that are in the correct position.
# The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
# Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

# The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.

 

# Example 1:

# Input: secret = "1807", guess = "7810"
# Output: "1A3B"
# Explanation: Bulls are connected with a '|' and cows are underlined:
# "1807"
#   |
# "7810"
# Example 2:

# Input: secret = "1123", guess = "0111"
# Output: "1A1B"
# Explanation: Bulls are connected with a '|' and cows are underlined:
# "1123"        "1123"
#   |      or     |
# "0111"        "0111"
# Note that only one of the two unmatched 1s is counted as a cow since the non-bull digits can only be rearranged to allow one 1 to be a bull.
 

# Constraints:

# 1 <= secret.length, guess.length <= 1000
# secret.length == guess.length
# secret and guess consist of digits only.





# Brute force:
class Solution:
    def getHint(self, secret, guess):
        bulls = 0
        cows = 0

        used_secret = [False] * len(secret)
        used_guess = [False] * len(guess)

        # Step 1: Bulls
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
                used_secret[i] = True
                used_guess[i] = True

        # Step 2: Cows
        for i in range(len(guess)):
            if used_guess[i]:
                continue

            for j in range(len(secret)):
                if not used_secret[j] and guess[i] == secret[j]:
                    cows += 1
                    used_secret[j] = True
                    break

        return str(bulls) + "A" + str(cows) + "B"







# Optimal:
class Solution:
    def getHint(self, secret, guess):
        bulls = 0
        cows = 0

        count = [0] * 10

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                count[int(secret[i])] += 1
                count[int(guess[i])] -= 1

        for x in count:
            if x > 0:
                cows += x

        # Better calculate cows using minimum frequencies
        count_secret = [0] * 10
        count_guess = [0] * 10

        for i in range(len(secret)):
            if secret[i] != guess[i]:
                count_secret[int(secret[i])] += 1
                count_guess[int(guess[i])] += 1

        cows = sum(min(count_secret[i], count_guess[i]) for i in range(10))

        return str(bulls) + "A" + str(cows) + "B"