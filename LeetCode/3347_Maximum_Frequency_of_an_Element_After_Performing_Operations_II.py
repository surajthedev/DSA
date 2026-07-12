# You are given an integer array nums and two integers k and numOperations.
# 
# You must perform an operation numOperations times on nums, where you can change any element nums[i] to any integer in the range [nums[i] - k, nums[i] + k].
# 
# Return the maximum frequency of an element after performing the operations.
# 
# Example 1:
# Input: nums = [1,4,5], k = 1, numOperations = 2
# Output: 2
# Explanation: We can change nums[1] to 4 - 1 = 3 and nums[2] to 5 - 1 = 4. The array becomes [1,3,4]. The max frequency is 2.
# 
# Example 2:
# Input: nums = [5,11,20,32], k = 5, numOperations = 3
# Output: 2
# Explanation: We can change nums[0] to 5 + 5 = 10, nums[1] to 11 - 1 = 10. The max frequency is 2.
# 
# Constraints:
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^9
# 0 <= k <= 10^9
# 0 <= numOperations <= 10^5

# Brute Force Solution
class Solution:
    def maxFrequency(self, nums: list[int], k: int, numOperations: int) -> int:
        from collections import Counter
        
        # Test all possible targets within the range of min(nums) to max(nums)
        # This is extremely slow for large values
        min_val = min(nums)
        max_val = max(nums)
        max_freq = 0
        
        freq = Counter(nums)
        
        for target in range(min_val, max_val + 1):
            operations_needed = 0
            possible_freq = freq[target]
            
            for num, count in freq.items():
                if num != target and abs(num - target) <= k:
                    can_add = min(count, numOperations - operations_needed)
                    possible_freq += can_add
                    operations_needed += can_add
                    
            max_freq = max(max_freq, possible_freq)
            
        return max_freq

# Optimal Solution
class Solution:
    def maxFrequency(self, nums: list[int], k: int, numOperations: int) -> int:
        from collections import Counter
        import bisect
        
        nums.sort()
        freq = Counter(nums)
        
        # The optimal target is either an element in nums or an element +/- k
        targets = set()
        for x in nums:
            targets.add(x)
            targets.add(x - k)
            targets.add(x + k)
            
        targets = sorted(list(targets))
        max_ans = 0
        
        for t in targets:
            left = bisect.bisect_left(nums, t - k)
            right = bisect.bisect_right(nums, t + k)
            
            # total numbers that can be changed to t
            total_possible = right - left
            
            # numbers that are already t
            already_t = freq.get(t, 0)
            
            # we need to change total_possible - already_t numbers
            changes_needed = total_possible - already_t
            
            # we can only do at most numOperations changes
            valid_changes = min(changes_needed, numOperations)
            
            max_ans = max(max_ans, already_t + valid_changes)
            
        return max_ans
