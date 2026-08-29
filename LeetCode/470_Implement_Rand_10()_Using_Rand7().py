# Given the API rand7() that generates a uniform random integer in the range [1, 7], write a function rand10() that generates a uniform random integer in the range [1, 10]. You can only call the API rand7(), and you shouldn't call any other API. Please do not use a language's built-in random API.

# Each test case will have one internal argument n, the number of times that your implemented function rand10() will be called while testing. Note that this is not an argument passed to rand10().

 

# Example 1:

# Input: n = 1
# Output: [2]
# Example 2:

# Input: n = 2
# Output: [2,8]
# Example 3:

# Input: n = 3
# Output: [3,8,10]
 

# Constraints:

# 1 <= n <= 105
 






# Brute force:
class Solution:
    def rand10(self):
        while True:
            num = (rand7() - 1) * 7 + rand7()

            if num <= 40:
                return (num - 1) % 10 + 1






# Optimal:
class Solution:
    def rand10(self):

        while True:

            # Generate uniform number from 1 to 49
            num = (rand7() - 1) * 7 + rand7()

            # Use 1 to 40
            if num <= 40:
                return (num - 1) % 10 + 1

            # 41 to 49 -> 9 values
            num = (num - 41) * 7 + rand7()

            # Now num is 1 to 63
            if num <= 60:
                return (num - 1) % 10 + 1

            # 61 to 63 -> 3 values
            num = (num - 61) * 7 + rand7()

            # Now num is 1 to 21
            if num <= 20:
                return (num - 1) % 10 + 1

            # If num == 21, retry