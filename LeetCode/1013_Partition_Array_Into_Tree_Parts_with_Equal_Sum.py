# Given an array of integers arr, return true if we can partition the array into three non-empty parts with equal sums.

# Formally, we can partition the array if we can find indexes i + 1 < j with (arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length - 1])



# Example 1:

# Input: arr = [0,2,1,-6,6,-7,9,1,2,0,1]
# Output: true
# Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
# Example 2:

# Input: arr = [0,2,1,-6,6,7,9,-1,2,0,1]
# Output: false
# Example 3:

# Input: arr = [3,3,6,5,-2,2,5,1,-9,4]
# Output: true
# Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4


# Constraints:

# 3 <= arr.length <= 5 * 104
# -104 <= arr[i] <= 104
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
#
#
#
#
#
#
#
#
# ### Brute Force

python
```
class Solution:
    def canThreePartsEqualSum(self, arr: list[int]) -> bool:
        n = len(arr)
        total = sum(arr)

        if total % 3 != 0:
            return False

        target = total // 3

        for i in range(n - 2):
            if sum(arr[:i + 1]) != target:
                continue

            for j in range(i + 2, n):
                if sum(arr[i + 1:j]) == target and sum(arr[j:]) == target:
                    return True

        return False
```

### Optimal

python
```
class Solution:
    def canThreePartsEqualSum(self, arr: list[int]) -> bool:
        total = sum(arr)

        if total % 3 != 0:
            return False

        target = total // 3
        current_sum = 0
        parts = 0

        for num in arr[:-1]:
            current_sum += num

            if current_sum == target:
                parts += 1
                current_sum = 0

                if parts == 2:
                    return True

        return False
```
