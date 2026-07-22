# You are given a binary string s of length n, where:

# '1' represents an active section.
# '0' represents an inactive section.
# You can perform at most one trade to maximize the number of active sections in s. In a trade, you:

# Convert a contiguous block of '1's that is surrounded by '0's to all '0's.
# Afterward, convert a contiguous block of '0's that is surrounded by '1's to all '1's.
# Additionally, you are given a 2D array queries, where queries[i] = [li, ri] represents a substring s[li...ri].

# For each query, determine the maximum possible number of active sections in s after making the optimal trade on the substring s[li...ri].

# Return an array answer, where answer[i] is the result for queries[i].

# Note

# For each query, treat s[li...ri] as if it is augmented with a '1' at both ends, forming t = '1' + s[li...ri] + '1'. The augmented '1's do not contribute to the final count.
# The queries are independent of each other.
 

# Example 1:

# Input: s = "01", queries = [[0,1]]

# Output: [1]

# Explanation:

# Because there is no block of '1's surrounded by '0's, no valid trade is possible. The maximum number of active sections is 1.

# Example 2:

# Input: s = "0100", queries = [[0,3],[0,2],[1,3],[2,3]]

# Output: [4,3,1,1]

# Explanation:

# Query [0, 3] → Substring "0100" → Augmented to "101001"
# Choose "0100", convert "0100" → "0000" → "1111".
# The final string without augmentation is "1111". The maximum number of active sections is 4.

# Query [0, 2] → Substring "010" → Augmented to "10101"
# Choose "010", convert "010" → "000" → "111".
# The final string without augmentation is "1110". The maximum number of active sections is 3.

# Query [1, 3] → Substring "100" → Augmented to "11001"
# Because there is no block of '1's surrounded by '0's, no valid trade is possible. The maximum number of active sections is 1.

# Query [2, 3] → Substring "00" → Augmented to "1001"
# Because there is no block of '1's surrounded by '0's, no valid trade is possible. The maximum number of active sections is 1.

# Example 3:

# Input: s = "1000100", queries = [[1,5],[0,6],[0,4]]

# Output: [6,7,2]

# Explanation:

# Query [1, 5] → Substring "00010" → Augmented to "1000101"
# Choose "00010", convert "00010" → "00000" → "11111".
# The final string without augmentation is "1111110". The maximum number of active sections is 6.

# Query [0, 6] → Substring "1000100" → Augmented to "110001001"
# Choose "000100", convert "000100" → "000000" → "111111".
# The final string without augmentation is "1111111". The maximum number of active sections is 7.

# Query [0, 4] → Substring "10001" → Augmented to "1100011"
# Because there is no block of '1's surrounded by '0's, no valid trade is possible. The maximum number of active sections is 2.

# Example 4:

# Input: s = "01010", queries = [[0,3],[1,4],[1,3]]

# Output: [4,4,2]

# Explanation:

# Query [0, 3] → Substring "0101" → Augmented to "101011"
# Choose "010", convert "010" → "000" → "111".
# The final string without augmentation is "11110". The maximum number of active sections is 4.

# Query [1, 4] → Substring "1010" → Augmented to "110101"
# Choose "010", convert "010" → "000" → "111".
# The final string without augmentation is "01111". The maximum number of active sections is 4.

# Query [1, 3] → Substring "101" → Augmented to "11011"
# Because there is no block of '1's surrounded by '0's, no valid trade is possible. The maximum number of active sections is 2.

 

# Constraints:

# 1 <= n == s.length <= 105
# 1 <= queries.length <= 105
# s[i] is either '0' or '1'.
# queries[i] = [li, ri]
# 0 <= li <= ri < n




# Brute Force:
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: list[list[int]]) -> list[int]:
        # Calculate the base number of 1s in the entire string
        total_1s = s.count('1')
        ans = []
        
        for li, ri in queries:
            # Extract the substring for the current query
            sub = s[li:ri+1]
            
            # Splitting by '1' naturally gives us all blocks of '0's.
            blocks_of_0s = [len(x) for x in sub.split('1') if x]
            
            # We need at least 2 blocks of 0s to perform a valid trade
            if len(blocks_of_0s) < 2:
                ans.append(total_1s)
            else:
                # Find the maximum sum of any two adjacent blocks of 0s
                max_gain = max(blocks_of_0s[i] + blocks_of_0s[i+1] for i in range(len(blocks_of_0s) - 1))
                ans.append(total_1s + max_gain)
                
        return ans







# Optimal Code:
import bisect
import math

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: list[list[int]]) -> list[int]:
        total_1s = s.count('1')
        n = len(s)
        
        # Step 1: Extract all contiguous blocks of '0's
        Z = []
        i = 0
        while i < n:
            if s[i] == '0':
                j = i
                while j < n and s[j] == '0':
                    j += 1
                Z.append((i, j - 1))
                i = j
            else:
                i += 1
                
        K = len(Z)
        if K == 0:
            return [total_1s] * len(queries)
            
        Starts = [z[0] for z in Z]
        Ends = [z[1] for z in Z]
        L = [z[1] - z[0] + 1 for z in Z]
        
        # Step 2: Precalculate adjacent sums of 0-blocks
        S = [L[i] + L[i+1] for i in range(K - 1)]
            
        # Step 3: Build a Sparse Table over S for O(1) Range Maximum Queries
        st = []
        if S:
            max_log = math.floor(math.log2(len(S))) + 1
            st = [[0] * max_log for _ in range(len(S))]
            for i in range(len(S)):
                st[i][0] = S[i]
            for j in range(1, max_log):
                for i in range(len(S) - (1 << j) + 1):
                    st[i][j] = max(st[i][j-1], st[i + (1 << (j-1))][j-1])
                    
        log_table = [0] * (len(S) + 1)
        for i in range(2, len(S) + 1):
            log_table[i] = log_table[i // 2] + 1
            
        # Step 4: Answer Queries efficiently
        ans = []
        for li, ri in queries:
            # Find the range of 0-blocks that intersect with [li, ri]
            a = bisect.bisect_left(Ends, li)
            b = bisect.bisect_right(Starts, ri) - 1
            
            # Less than 2 blocks of 0s exist in the range
            if a >= b:
                ans.append(total_1s)
            else:
                # Calculate the visible lengths of the boundary blocks
                V_first = min(ri, Ends[a]) - max(li, Starts[a]) + 1
                V_last = min(ri, Ends[b]) - max(li, Starts[b]) + 1
                
                # If there are exactly 2 blocks
                if b == a + 1:
                    gain = V_first + V_last
                else:
                    gain = max(V_first + L[a+1], L[b-1] + V_last)
                    
                    # Range Maximum Query for strictly internal adjacent pairs
                    if b - 2 >= a + 1:
                        L_idx = a + 1
                        R_idx = b - 2
                        W = R_idx - L_idx + 1
                        j_log = log_table[W]
                        mx_S = max(st[L_idx][j_log], st[R_idx - (1 << j_log) + 1][j_log])
                        gain = max(gain, mx_S)
                        
                ans.append(total_1s + gain)
                
        return ans
