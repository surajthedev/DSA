# Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.
# 
# He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.
# 
# Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.
# 
# Example 1:
# Input: n = 4
# Output: 10
# Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.
# 
# Example 2:
# Input: n = 10
# Output: 37
# Explanation: After the 10th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37. Notice that on the 2nd Monday, Hercy only puts in $2.
# 
# Example 3:
# Input: n = 20
# Output: 96
# Explanation: After the 20th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96.
# 
# Constraints:
# 1 <= n <= 1000

# Brute Force Solution
class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        monday_val = 1
        curr_val = 1
        
        for i in range(1, n + 1):
            total += curr_val
            curr_val += 1
            if i % 7 == 0:
                monday_val += 1
                curr_val = monday_val
                
        return total

# Optimal Solution
class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        days = n % 7
        
        # First week sum is 28 (1+2+3+4+5+6+7)
        # Each subsequent week sum increases by 7
        # Total sum of full weeks is an arithmetic progression: 28, 35, 42...
        total = (weeks * (2 * 28 + (weeks - 1) * 7)) // 2
        
        # Add remaining days
        start = weeks + 1
        for i in range(days):
            total += start + i
            
        return total
