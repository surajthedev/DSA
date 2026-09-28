# You are given two integer arrays nums1 and nums2 both of the same length. The advantage of nums1 with respect to nums2 is the number of indices i for which nums1[i] > nums2[i].

# Return any permutation of nums1 that maximizes its advantage with respect to nums2.



# Example 1:

# Input: nums1 = [2,7,11,15], nums2 = [1,10,4,11]
# Output: [2,11,7,15]
# Example 2:

# Input: nums1 = [12,24,8,32], nums2 = [13,25,32,11]
# Output: [24,32,8,12]


# Constraints:

# 1 <= nums1.length <= 105
# nums2.length == nums1.length
# 0 <= nums1[i], nums2[i] <= 109
#
#
#
#
#
#
#
#
#
#
# Brute force:
class Solution:
    def advantageCount(self, nums1: list[int], nums2: list[int]) -> list[int]:
        n = len(nums1)
        used = [False] * n
        ans = [0] * n

        for i in range(n):
            best = -1

            for j in range(n):
                if not used[j] and nums1[j] > nums2[i]:
                    if best == -1 or nums1[j] < nums1[best]:
                        best = j

            if best == -1:
                for j in range(n):
                    if not used[j]:
                        best = j
                        break

            ans[i] = nums1[best]
            used[best] = True

        return ans









# Optimal:
class Solution:
    def advantageCount(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1.sort()
        n = len(nums2)

        indexed_nums2 = sorted((value, i) for i, value in enumerate(nums2))

        ans = [0] * n
        left = 0
        right = n - 1

        for x in nums1:
            if x > indexed_nums2[left][0]:
                ans[indexed_nums2[left][1]] = x
                left += 1
            else:
                ans[indexed_nums2[right][1]] = x
                right -= 1

        return ans
