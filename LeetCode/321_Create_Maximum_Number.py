# You are given two integer arrays nums1 and nums2 of lengths m and n respectively. nums1 and nums2 represent the digits of two numbers. You are also given an integer k.

# Create the maximum number of length k <= m + n from digits of the two numbers. The relative order of the digits from the same array must be preserved.

# Return an array of the k digits representing the answer.

 

# Example 1:

# Input: nums1 = [3,4,6,5], nums2 = [9,1,2,5,8,3], k = 5
# Output: [9,8,6,5,3]
# Example 2:

# Input: nums1 = [6,7], nums2 = [6,0,4], k = 5
# Output: [6,7,6,0,4]
# Example 3:

# Input: nums1 = [3,9], nums2 = [8,9], k = 3
# Output: [9,8,9]
 

# Constraints:

# m == nums1.length
# n == nums2.length
# 1 <= m, n <= 500
# 0 <= nums1[i], nums2[i] <= 9
# 1 <= k <= m + n
# nums1 and nums2 do not have leading zeros.






# Brute force:
class Solution:
    def maxNumber(self, nums1, nums2, k):

        def generate(nums, length):
            result = []

            def backtrack(index, path):
                if len(path) == length:
                    result.append(path[:])
                    return

                if len(nums) - index < length - len(path):
                    return

                # Take current digit
                path.append(nums[index])
                backtrack(index + 1, path)
                path.pop()

                # Skip current digit
                backtrack(index + 1, path)

            backtrack(0, [])
            return result

        def merge(a, b):
            result = []

            while a or b:
                if a > b:
                    result.append(a[0])
                    a = a[1:]
                else:
                    result.append(b[0])
                    b = b[1:]

            return result

        answer = []

        # i digits from nums1
        for i in range(k + 1):

            j = k - i

            if i > len(nums1) or j > len(nums2):
                continue

            list1 = generate(nums1, i)
            list2 = generate(nums2, j)

            # Try every possible pair
            for a in list1:
                for b in list2:
                    candidate = merge(a, b)

                    if candidate > answer:
                        answer = candidate

        return answer







# Optimal:
class Solution:
    def maxNumber(self, nums1, nums2, k):

        def max_subsequence(nums, length):
            remove = len(nums) - length
            stack = []

            for num in nums:
                while stack and remove > 0 and stack[-1] < num:
                    stack.pop()
                    remove -= 1

                stack.append(num)

            return stack[:length]

        def merge(a, b):
            result = []

            while a or b:
                # Lexicographically larger remaining sequence
                if a > b:
                    result.append(a.pop(0))
                else:
                    result.append(b.pop(0))

            return result

        def greater(a, i, b, j):
            while i < len(a) and j < len(b):
                if a[i] != b[j]:
                    return a[i] > b[j]

                i += 1
                j += 1

            return (len(a) - i) > (len(b) - j)

        def merge_optimal(a, b):
            result = []
            i = 0
            j = 0

            while i < len(a) or j < len(b):
                if greater(a, i, b, j):
                    result.append(a[i])
                    i += 1
                else:
                    result.append(b[j])
                    j += 1

            return result

        answer = []

        start = max(0, k - len(nums2))
        end = min(k, len(nums1))

        for i in range(start, end + 1):

            part1 = max_subsequence(nums1, i)
            part2 = max_subsequence(nums2, k - i)

            candidate = merge_optimal(part1, part2)

            if greater(candidate, 0, answer, 0):
                answer = candidate

        return answer