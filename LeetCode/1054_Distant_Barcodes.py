# In a warehouse, there is a row of barcodes, where the ith barcode is barcodes[i].

# Rearrange the barcodes so that no two adjacent barcodes are equal. You may return any answer, and it is guaranteed an answer exists.



# Example 1:

# Input: barcodes = [1,1,1,2,2,2]
# Output: [2,1,2,1,2,1]
# Example 2:

# Input: barcodes = [1,1,1,1,2,2,3,3]
# Output: [1,3,1,3,1,2,1,2]


# Constraints:

# 1 <= barcodes.length <= 10000
# 1 <= barcodes[i] <= 10000
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
from collections import Counter

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        freq = Counter(barcodes)
        result = []

        while len(result) < len(barcodes):
            for num in sorted(freq, key=lambda x: freq[x], reverse=True):
                if freq[num] > 0 and (not result or result[-1] != num):
                    result.append(num)
                    freq[num] -= 1
                    break

        return result
```

### Optimal (Greedy + Max Heap)

python
```
from typing import List
from collections import Counter
import heapq

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        freq = Counter(barcodes)
        heap = [(-count, num) for num, count in freq.items()]
        heapq.heapify(heap)

        result = []
        prev_count, prev_num = 0, None

        while heap:
            count, num = heapq.heappop(heap)
            result.append(num)

            if prev_count < 0:
                heapq.heappush(heap, (prev_count, prev_num))

            freq[num] -= 1
            prev_count, prev_num = count + 1, num

        return result
```
