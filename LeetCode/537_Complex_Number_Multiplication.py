# A complex number can be represented as a string on the form "real+imaginaryi" where:

# real is the real part and is an integer in the range [-100, 100].
# imaginary is the imaginary part and is an integer in the range [-100, 100].
# i2 == -1.
# Given two complex numbers num1 and num2 as strings, return a string of the complex number that represents their multiplications.

 

# Example 1:

# Input: num1 = "1+1i", num2 = "1+1i"
# Output: "0+2i"
# Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
# Example 2:

# Input: num1 = "1+-1i", num2 = "1+-1i"
# Output: "0+-2i"
# Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
 

# Constraints:

# num1 and num2 are valid complex numbers.







# Brute force:
class Solution:
    def complexNumberMultiply(self, num1, num2):
        a, b = num1[:-1].split("+")
        c, d = num2[:-1].split("+")

        a, b, c, d = int(a), int(b), int(c), int(d)

        real = a * c - b * d
        imag = a * d + b * c

        return str(real) + "+" + str(imag) + "i"








# Optimal:
class Solution:
    def complexNumberMultiply(self, num1, num2):
        a, b = map(int, num1[:-1].split("+"))
        c, d = map(int, num2[:-1].split("+"))

        return f"{a*c - b*d}+{a*d + b*c}i"