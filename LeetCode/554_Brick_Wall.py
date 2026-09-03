# There is a rectangular brick wall in front of you with n rows of bricks. The ith row has some number of bricks each of the same height (i.e., one unit) but they can be of different widths. The total width of each row is the same.

# Draw a vertical line from the top to the bottom and cross the least bricks. If your line goes through the edge of a brick, then the brick is not considered as crossed. You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.

# Given the 2D array wall that contains the information about the wall, return the minimum number of crossed bricks after drawing such a vertical line.

 

# Example 1:


# Input: wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
# Output: 2
# Example 2:

# Input: wall = [[1],[1],[1]]
# Output: 3
 

# Constraints:

# n == wall.length
# 1 <= n <= 104
# 1 <= wall[i].length <= 104
# 1 <= sum(wall[i].length) <= 2 * 104
# sum(wall[i]) is the same for each row i.
# 1 <= wall[i][j] <= 231 - 1






# Brute force:
class Solution {
public:
    int leastBricks(vector<vector<int>>& wall) {
        long long width = 0;

        for (long long x : wall[0]) {
            width += x;
        }

        int ans = wall.size();

        for (long long pos = 1; pos < width; pos++) {
            int crossed = 0;

            for (auto& row : wall) {
                long long sum = 0;
                bool edge = false;

                for (long long brick : row) {
                    sum += brick;

                    if (sum == pos) {
                        edge = true;
                        break;
                    }

                    if (sum > pos) {
                        crossed++;
                        break;
                    }
                }
            }

            ans = min(ans, crossed);
        }

        return ans;
    }
};













# Optimal:
class Solution {
public:
    int leastBricks(vector<vector<int>>& wall) {
        unordered_map<long long, int> edges;

        for (auto& row : wall) {
            long long sum = 0;

            for (int i = 0; i < (int)row.size() - 1; i++) {
                sum += (long long)row[i];
                edges[sum]++;
            }
        }

        int maxEdges = 0;

        for (auto& [pos, count] : edges) {
            maxEdges = max(maxEdges, count);
        }

        return (int)wall.size() - maxEdges;
    }
};