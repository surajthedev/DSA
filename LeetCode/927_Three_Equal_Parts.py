# You are given an array arr which consists of only zeros and ones, divide the array into three non-empty parts such that all of these parts represent the same binary value.

# If it is possible, return any [i, j] with i + 1 < j, such that:

# arr[0], arr[1], ..., arr[i] is the first part,
# arr[i + 1], arr[i + 2], ..., arr[j - 1] is the second part, and
# arr[j], arr[j + 1], ..., arr[arr.length - 1] is the third part.
# All three parts have equal binary values.
# If it is not possible, return [-1, -1].

# Note that the entire part is used when considering what binary value it represents. For example, [1,1,0] represents 6 in decimal, not 3. Also, leading zeros are allowed, so [0,1,1] and [1,1] represent the same value.



# Example 1:

# Input: arr = [1,0,1,0,1]
# Output: [0,3]
# Example 2:

# Input: arr = [1,1,0,1,1]
# Output: [-1,-1]
# Example 3:

# Input: arr = [1,1,0,0,1]
# Output: [0,2]


# Constraints:

# 3 <= arr.length <= 3 * 104
# arr[i] is 0 or 1














# Brute force:
class Solution:
    def threeEqualParts(self, arr: list[int]) -> list[int]:
        n = len(arr)

        def value(start, end):
            while start < end and arr[start] == 0:
                start += 1

            if start == end:
                return 0

            result = 0
            for i in range(start, end):
                result = result * 2 + arr[i]

            return result

        for i in range(n - 2):
            for j in range(i + 2, n):
                if value(0, i + 1) == value(i + 1, j) == value(j, n):
                    return [i, j]

        return [-1, -1]













# Optimal:
class Solution:
    def threeEqualParts(self, arr: list[int]) -> list[int]:
        n = len(arr)
        ones = sum(arr)

        # All parts represent 0
        if ones == 0:
            return [0, n - 1]

        # Number of 1s must be divisible by 3
        if ones % 3 != 0:
            return [-1, -1]

        k = ones // 3

        first = second = third = -1
        count = 0

        for i in range(n):
            if arr[i] == 1:
                count += 1

                if count == 1:
                    first = i
                elif count == k + 1:
                    second = i
                elif count == 2 * k + 1:
                    third = i

        # Length of the significant part
        length = n - third

        # Parts must have enough space
        if first + length > second or second + length > third:
            return [-1, -1]

        # Compare the significant binary parts
        if arr[first:first + length] != arr[second:second + length]:
            return [-1, -1]

        if arr[first:first + length] != arr[third:third + length]:
            return [-1, -1]

        return [first + length - 1, second + length]
