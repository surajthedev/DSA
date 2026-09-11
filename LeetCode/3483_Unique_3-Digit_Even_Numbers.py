# You are given an array of digits called digits. Your task is to determine the number of distinct three-digit even numbers that can be formed using these digits.

# Note: Each copy of a digit can only be used once per number, and there may not be leading zeros.

 

# Example 1:

# Input: digits = [1,2,3,4]

# Output: 12

# Explanation: The 12 distinct 3-digit even numbers that can be formed are 124, 132, 134, 142, 214, 234, 312, 314, 324, 342, 412, and 432. Note that 222 cannot be formed because there is only 1 copy of the digit 2.

# Example 2:

# Input: digits = [0,2,2]

# Output: 2

# Explanation: The only 3-digit even numbers that can be formed are 202 and 220. Note that the digit 2 can be used twice because it appears twice in the array.

# Example 3:

# Input: digits = [6,6,6]

# Output: 1

# Explanation: Only 666 can be formed.

# Example 4:

# Input: digits = [1,3,5]

# Output: 0

# Explanation: No even 3-digit numbers can be formed.

 

# Constraints:

# 3 <= digits.length <= 10
# 0 <= digits[i] <= 9






# Brute force:
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        nums = set()
        n = len(digits)

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i == j or j == k or i == k:
                        continue

                    if digits[i] == 0:
                        continue

                    if digits[k] % 2 != 0:
                        continue

                    num = digits[i] * 100 + digits[j] * 10 + digits[k]
                    nums.add(num)

        return len(nums)












# Optimal:
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        freq = [0] * 10

        for d in digits:
            freq[d] += 1

        ans = 0

        for first in range(1, 10):
            if freq[first] == 0:
                continue

            freq[first] -= 1

            for second in range(10):
                if freq[second] == 0:
                    continue

                freq[second] -= 1

                for last in (0, 2, 4, 6, 8):
                    if freq[last] > 0:
                        ans += 1

                freq[second] += 1

            freq[first] += 1

        return ans