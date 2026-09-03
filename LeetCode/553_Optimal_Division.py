# You are given an integer array nums. The adjacent integers in nums will perform the float division.

# For example, for nums = [2,3,4], we will evaluate the expression "2/3/4".
# However, you can add any number of parenthesis at any position to change the priority of operations. You want to add these parentheses such the value of the expression after the evaluation is maximum.

# Return the corresponding expression that has the maximum value in string format.

# Note: your expression should not contain redundant parenthesis.

 

# Example 1:

# Input: nums = [1000,100,10,2]
# Output: "1000/(100/10/2)"
# Explanation: 1000/(100/10/2) = 1000/((100/10)/2) = 200
# However, the bold parenthesis in "1000/((100/10)/2)" are redundant since they do not influence the operation priority.
# So you should return "1000/(100/10/2)".
# Other cases:
# 1000/(100/10)/2 = 50
# 1000/(100/(10/2)) = 50
# 1000/100/10/2 = 0.5
# 1000/100/(10/2) = 2
# Example 2:

# Input: nums = [2,3,4]
# Output: "2/(3/4)"
# Explanation: (2/(3/4)) = 8/3 = 2.667
# It can be shown that after trying all possibilities, we cannot get an expression with evaluation greater than 2.667
 

# Constraints:

# 1 <= nums.length <= 10
# 2 <= nums[i] <= 1000
# There is only one optimal division for the given input.




# Brute force:
class Solution {
public:
    pair<double, string> solve(vector<int>& nums, int l, int r) {
        if (l == r) {
            return {nums[l], to_string(nums[l])};
        }

        double best = -1;
        string bestExpr;

        for (int k = l; k < r; k++) {
            auto left = solve(nums, l, k);
            auto right = solve(nums, k + 1, r);

            double value = left.first / right.first;

            string expr = "(" + left.second + "/" + right.second + ")";

            if (value > best) {
                best = value;
                bestExpr = expr;
            }
        }

        return {best, bestExpr};
    }

    string optimalDivision(vector<int>& nums) {
        if (nums.size() == 1)
            return to_string(nums[0]);

        auto result = solve(nums, 0, nums.size() - 1);

        string s = result.second;

        return s.substr(1, s.size() - 2);
    }
};







# Optimal:
class Solution {
public:
    string optimalDivision(vector<int>& nums) {
        int n = nums.size();

        if (n == 1)
            return to_string(nums[0]);

        if (n == 2)
            return to_string(nums[0]) + "/" + to_string(nums[1]);

        string ans = to_string(nums[0]) + "/(";

        for (int i = 1; i < n; i++) {
            ans += to_string(nums[i]);

            if (i != n - 1)
                ans += "/";
        }

        ans += ")";

        return ans;
    }
};