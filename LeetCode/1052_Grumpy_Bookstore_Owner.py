# There is a bookstore owner that has a store open for n minutes. You are given an integer array customers of length n where customers[i] is the number of the customers that enter the store at the start of the ith minute and all those customers leave after the end of that minute.

# During certain minutes, the bookstore owner is grumpy. You are given a binary array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.

# When the bookstore owner is grumpy, the customers entering during that minute are not satisfied. Otherwise, they are satisfied.

# The bookstore owner knows a secret technique to remain not grumpy for minutes consecutive minutes, but this technique can only be used once.

# Return the maximum number of customers that can be satisfied throughout the day.



# Example 1:

# Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3

# Output: 16

# Explanation:

# The bookstore owner keeps themselves not grumpy for the last 3 minutes.

# The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.

# Example 2:

# Input: customers = [1], grumpy = [0], minutes = 1

# Output: 1



# Constraints:

# n == customers.length == grumpy.length
# 1 <= minutes <= n <= 2 * 104
# 0 <= customers[i] <= 1000
# grumpy[i] is either 0 or 1.
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
from typing import List

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        ans = 0

        for start in range(n - minutes + 1):
            total = 0

            for i in range(n):
                if grumpy[i] == 0 or start <= i < start + minutes:
                    total += customers[i]

            ans = max(ans, total)

        return ans
```

### Optimal (Sliding Window)

python
```
from typing import List

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        satisfied = 0
        extra = 0

        for i in range(len(customers)):
            if grumpy[i] == 0:
                satisfied += customers[i]

        window = 0
        max_extra = 0
        left = 0

        for right in range(len(customers)):
            if grumpy[right] == 1:
                window += customers[right]

            if right - left + 1 > minutes:
                if grumpy[left] == 1:
                    window -= customers[left]
                left += 1

            max_extra = max(max_extra, window)

        return satisfied + max_extra
```
