# You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.

# The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

# The 1st place athlete's rank is "Gold Medal".
# The 2nd place athlete's rank is "Silver Medal".
# The 3rd place athlete's rank is "Bronze Medal".
# For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
# Return an array answer of size n where answer[i] is the rank of the ith athlete.

 

# Example 1:

# Input: score = [5,4,3,2,1]
# Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
# Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].
# Example 2:

# Input: score = [10,3,8,9,4]
# Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
# Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th].

 

# Constraints:

# n == score.length
# 1 <= n <= 104
# 0 <= score[i] <= 106
# All the values in score are unique.





# Brute force:
class Solution:
    def findRelativeRanks(self, score):
        n = len(score)
        answer = []

        for i in range(n):
            rank = 1

            for j in range(n):
                if score[j] > score[i]:
                    rank += 1

            if rank == 1:
                answer.append("Gold Medal")
            elif rank == 2:
                answer.append("Silver Medal")
            elif rank == 3:
                answer.append("Bronze Medal")
            else:
                answer.append(str(rank))

        return answer









# Optimal:
class Solution:
    def findRelativeRanks(self, score):
        sorted_scores = sorted(score, reverse=True)

        rank = {}

        for i, s in enumerate(sorted_scores):
            position = i + 1

            if position == 1:
                rank[s] = "Gold Medal"
            elif position == 2:
                rank[s] = "Silver Medal"
            elif position == 3:
                rank[s] = "Bronze Medal"
            else:
                rank[s] = str(position)

        answer = []

        for s in score:
            answer.append(rank[s])

        return answer