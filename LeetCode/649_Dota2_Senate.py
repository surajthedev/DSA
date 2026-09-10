# In the world of Dota2, there are two parties: the Radiant and the Dire.

# The Dota2 senate consists of senators coming from two parties. Now the Senate wants to decide on a change in the Dota2 game. The voting for this change is a round-based procedure. In each round, each senator can exercise one of the two rights:

# Ban one senator's right: A senator can make another senator lose all his rights in this and all the following rounds.
# Announce the victory: If this senator found the senators who still have rights to vote are all from the same party, he can announce the victory and decide on the change in the game.
# Given a string senate representing each senator's party belonging. The character 'R' and 'D' represent the Radiant party and the Dire party. Then if there are n senators, the size of the given string will be n.

# The round-based procedure starts from the first senator to the last senator in the given order. This procedure will last until the end of voting. All the senators who have lost their rights will be skipped during the procedure.

# Suppose every senator is smart enough and will play the best strategy for his own party. Predict which party will finally announce the victory and change the Dota2 game. The output should be "Radiant" or "Dire".

 

# Example 1:

# Input: senate = "RD"
# Output: "Radiant"
# Explanation: 
# The first senator comes from Radiant and he can just ban the next senator's right in round 1. 
# And the second senator can't exercise any rights anymore since his right has been banned. 
# And in round 2, the first senator can just announce the victory since he is the only guy in the senate who can vote.
# Example 2:

# Input: senate = "RDD"
# Output: "Dire"
# Explanation: 
# The first senator comes from Radiant and he can just ban the next senator's right in round 1. 
# And the second senator can't exercise any rights anymore since his right has been banned. 
# And the third senator comes from Dire and he can ban the first senator's right in round 1. 
# And in round 2, the third senator can just announce the victory since he is the only guy in the senate who can vote.
 

# Constraints:

# n == senate.length
# 1 <= n <= 104
# senate[i] is either 'R' or 'D'.








# Brute force:
# Brute Force
class Solution:
    def predictPartyVictory(self, senate):
        senate = list(senate)

        while "R" in senate and "D" in senate:
            banned_R = 0
            banned_D = 0
            next_round = []

            for senator in senate:
                if senator == "R":
                    if banned_R > 0:
                        banned_R -= 1
                    else:
                        banned_D += 1
                        next_round.append("R")
                else:
                    if banned_D > 0:
                        banned_D -= 1
                    else:
                        banned_R += 1
                        next_round.append("D")

            senate = next_round

        return "Radiant" if senate[0] == "R" else "Dire"# Brute Force
class Solution:
    def predictPartyVictory(self, senate):
        senate = list(senate)

        while "R" in senate and "D" in senate:
            banned_R = 0
            banned_D = 0
            next_round = []

            for senator in senate:
                if senator == "R":
                    if banned_R > 0:
                        banned_R -= 1
                    else:
                        banned_D += 1
                        next_round.append("R")
                else:
                    if banned_D > 0:
                        banned_D -= 1
                    else:
                        banned_R += 1
                        next_round.append("D")

            senate = next_round

        return "Radiant" if senate[0] == "R" else "Dire"









# Optimal:
# Optimal - Queue
from collections import deque

class Solution:
    def predictPartyVictory(self, senate):
        n = len(senate)

        radiant = deque()
        dire = deque()

        for i, senator in enumerate(senate):
            if senator == "R":
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
            r = radiant.popleft()
            d = dire.popleft()

            if r < d:
                radiant.append(r + n)
            else:
                dire.append(d + n)

        return "Radiant" if radiant else "Dire"