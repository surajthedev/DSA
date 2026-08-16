# Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.

# The test cases are generated such that the output values fit in a 32-bit integer and the number of different results does not exceed 104.

 

# Example 1:

# Input: expression = "2-1-1"
# Output: [0,2]
# Explanation:
# ((2-1)-1) = 0 
# (2-(1-1)) = 2
# Example 2:

# Input: expression = "2*3-4*5"
# Output: [-34,-14,-10,-10,10]
# Explanation:
# (2*(3-(4*5))) = -34 
# ((2*3)-(4*5)) = -14 
# ((2*(3-4))*5) = -10 
# (2*((3-4)*5)) = -10 
# (((2*3)-4)*5) = 10
 

# Constraints:

# 1 <= expression.length <= 20
# expression consists of digits and the operator '+', '-', and '*'.
# All the integer values in the input expression are in the range [0, 99].
# The integer values in the input expression do not have a leading '-' or '+' denoting the sign.




# Brute force:
class Solution:
    def diffWaysToCompute(self, expression):
        
        def solve(expr):
            results = []

            for i, ch in enumerate(expr):

                if ch in "+-*":
                    left = solve(expr[:i])
                    right = solve(expr[i + 1:])

                    for a in left:
                        for b in right:

                            if ch == "+":
                                results.append(a + b)

                            elif ch == "-":
                                results.append(a - b)

                            else:
                                results.append(a * b)

            # Agar koi operator nahi mila,
            # iska matlab expression ek number hai
            if not results:
                results.append(int(expr))

            return results

        return solve(expression)






# Optimal:
class Solution:
    def diffWaysToCompute(self, expression):

        memo = {}

        def solve(expr):
            if expr in memo:
                return memo[expr]

            results = []

            for i, ch in enumerate(expr):

                if ch not in "+-*":
                    continue

                left = solve(expr[:i])
                right = solve(expr[i + 1:])

                for a in left:
                    for b in right:

                        if ch == "+":
                            results.append(a + b)

                        elif ch == "-":
                            results.append(a - b)

                        else:
                            results.append(a * b)

            # Expression is just a number
            if not results:
                results.append(int(expr))

            memo[expr] = results
            return results

        return solve(expression)