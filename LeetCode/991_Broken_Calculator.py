# There is a broken calculator that has the integer startValue on its display initially. In one operation, you can:

# multiply the number on display by 2, or
# subtract 1 from the number on display.
# Given two integers startValue and target, return the minimum number of operations needed to display target on the calculator.



# Example 1:

# Input: startValue = 2, target = 3
# Output: 2
# Explanation: Use double operation and then decrement operation {2 -> 4 -> 3}.
# Example 2:

# Input: startValue = 5, target = 8
# Output: 2
# Explanation: Use decrement and then double {5 -> 4 -> 8}.
# Example 3:

# Input: startValue = 3, target = 10
# Output: 3
# Explanation: Use double, decrement and double {3 -> 6 -> 5 -> 10}.


# Constraints:

# 1 <= startValue, target <= 109
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
# ## Brute Force — BFS

```
from collections import deque

class Solution:
    def brokenCalc(self, startValue, target):
        if startValue >= target:
            return startValue - target

        queue = deque([(startValue, 0)])
        visited = {startValue}

        while queue:
            value, steps = queue.popleft()

            if value == target:
                return steps

            for nxt in (value * 2, value - 1):
                if 0 < nxt <= 2 * target and nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt, steps + 1))
```

## Optimal — Greedy

```
class Solution:
    def brokenCalc(self, startValue, target):
        operations = 0

        while target > startValue:
            operations += 1

            if target % 2 == 0:
                target //= 2
            else:
                target += 1

        return operations + (startValue - target)
```

### Complexity

- **Brute Force:** `O(target)` time, `O(target)` space
- **Optimal:** `O(log(target))` time, `O(1)` space
