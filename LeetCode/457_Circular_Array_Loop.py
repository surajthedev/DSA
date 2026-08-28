# You are playing a game involving a circular array of non-zero integers nums. Each nums[i] denotes the number of indices forward/backward you must move if you are located at index i:

# If nums[i] is positive, move nums[i] steps forward, and
# If nums[i] is negative, move abs(nums[i]) steps backward.
# Since the array is circular, you may assume that moving forward from the last element puts you on the first element, and moving backwards from the first element puts you on the last element.

# A cycle in the array consists of a sequence of indices seq of length k where:

# Following the movement rules above results in the repeating index sequence seq[0] -> seq[1] -> ... -> seq[k - 1] -> seq[0] -> ...
# Every nums[seq[j]] is either all positive or all negative.
# k > 1
# Return true if there is a cycle in nums, or false otherwise.

 

# Example 1:


# Input: nums = [2,-1,1,2,2]
# Output: true
# Explanation: The graph shows how the indices are connected. White nodes are jumping forward, while red is jumping backward.
# We can see the cycle 0 --> 2 --> 3 --> 0 --> ..., and all of its nodes are white (jumping in the same direction).
# Example 2:


# Input: nums = [-1,-2,-3,-4,-5,6]
# Output: false
# Explanation: The graph shows how the indices are connected. White nodes are jumping forward, while red is jumping backward.
# The only cycle is of size 1, so we return false.
# Example 3:


# Input: nums = [1,-1,5,1,4]
# Output: true
# Explanation: The graph shows how the indices are connected. White nodes are jumping forward, while red is jumping backward.
# We can see the cycle 0 --> 1 --> 0 --> ..., and while it is of size > 1, it has a node jumping forward and a node jumping backward, so it is not a cycle.
# We can see the cycle 3 --> 4 --> 3 --> ..., and all of its nodes are white (jumping in the same direction).
 

# Constraints:

# 1 <= nums.length <= 5000
# -1000 <= nums[i] <= 1000
# nums[i] != 0







# Brute force:
class Solution:
    def circularArrayLoop(self, nums):
        n = len(nums)

        for start in range(n):
            direction = nums[start] > 0
            curr = start
            visited = set()

            while True:
                if (nums[curr] > 0) != direction:
                    break

                if curr in visited:
                    if len(visited) > 1:
                        return True
                    break

                visited.add(curr)
                curr = (curr + nums[curr]) % n

        return False





# Optimal:
class Solution:
    def circularArrayLoop(self, nums):
        n = len(nums)

        def next_index(i):
            return (i + nums[i]) % n

        for i in range(n):
            direction = nums[i] > 0

            slow = i
            fast = i

            while True:
                # slow next
                if (nums[slow] > 0) != direction:
                    break

                slow = next_index(slow)

                # fast next
                if (nums[fast] > 0) != direction:
                    break

                fast = next_index(fast)

                if (nums[fast] > 0) != direction:
                    break

                fast = next_index(fast)

                if slow == fast:
                    # Check cycle is not self-loop
                    if slow == next_index(slow):
                        break
                    return True

        return False