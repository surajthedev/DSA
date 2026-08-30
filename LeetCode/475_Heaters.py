# Winter is coming! During the contest, your first job is to design a standard heater with a fixed warm radius to warm all the houses.

# Every house can be warmed, as long as the house is within the heater's warm radius range. 

# Given the positions of houses and heaters on a horizontal line, return the minimum radius standard of heaters so that those heaters could cover all houses.

# Notice that all the heaters follow your radius standard, and the warm radius will be the same.

 

# Example 1:

# Input: houses = [1,2,3], heaters = [2]
# Output: 1
# Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.
# Example 2:

# Input: houses = [1,2,3,4], heaters = [1,4]
# Output: 1
# Explanation: The two heaters were placed at positions 1 and 4. We need to use a radius 1 standard, then all the houses can be warmed.
# Example 3:

# Input: houses = [1,5], heaters = [2]
# Output: 3
 

# Constraints:

# 1 <= houses.length, heaters.length <= 3 * 104
# 1 <= houses[i], heaters[i] <= 109







# Brute force:
class Solution:
    def findRadius(self, houses, heaters):
        ans = 0

        for house in houses:
            min_dist = float('inf')

            for heater in heaters:
                min_dist = min(min_dist, abs(house - heater))

            ans = max(ans, min_dist)

        return ans







# Optimal:
class Solution:
    def findRadius(self, houses, heaters):
        heaters.sort()
        ans = 0

        for house in houses:
            left, right = 0, len(heaters) - 1

            while left <= right:
                mid = (left + right) // 2

                if heaters[mid] < house:
                    left = mid + 1
                else:
                    right = mid - 1

            dist_left = abs(house - heaters[right]) if right >= 0 else float('inf')
            dist_right = abs(house - heaters[left]) if left < len(heaters) else float('inf')

            ans = max(ans, min(dist_left, dist_right))

        return ans