# An attendance record for a student can be represented as a string where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

# 'A': Absent.
# 'L': Late.
# 'P': Present.
# Any student is eligible for an attendance award if they meet both of the following criteria:

# The student was absent ('A') for strictly fewer than 2 days total.
# The student was never late ('L') for 3 or more consecutive days.
# Given an integer n, return the number of possible attendance records of length n that make a student eligible for an attendance award. The answer may be very large, so return it modulo 109 + 7.

 

# Example 1:

# Input: n = 2
# Output: 8
# Explanation: There are 8 records with length 2 that are eligible for an award:
# "PP", "AP", "PA", "LP", "PL", "AL", "LA", "LL"
# Only "AA" is not eligible because there are 2 absences (there need to be fewer than 2).
# Example 2:

# Input: n = 1
# Output: 3
# Example 3:

# Input: n = 10101
# Output: 183236316
 

# Constraints:

# 1 <= n <= 105







# Brute force:
class Solution {
public:
    int checkRecord(int n) {
        const long long MOD = 1000000007;
        long long ans = 0;

        function<void(int, int, int)> dfs = [&](int day, int a, int l) {
            if (day == n) {
                ans = (ans + 1) % MOD;
                return;
            }

            dfs(day + 1, a, 0);

            if (a == 0)
                dfs(day + 1, 1, 0);

            if (l < 2)
                dfs(day + 1, a, l + 1);
        };

        dfs(0, 0, 0);
        return ans;
    }
};





# OptiamL;
class Solution {
public:
    int checkRecord(int n) {
        const long long MOD = 1000000007;

        long long dp[2][3] = {};
        dp[0][0] = 1;

        for (int i = 0; i < n; i++) {
            long long ndp[2][3] = {};

            for (int a = 0; a < 2; a++) {
                for (int l = 0; l < 3; l++) {
                    long long cur = dp[a][l];

                    // P
                    ndp[a][0] = (ndp[a][0] + cur) % MOD;

                    // A
                    if (a == 0) {
                        ndp[1][0] = (ndp[1][0] + cur) % MOD;
                    }

                    // L
                    if (l < 2) {
                        ndp[a][l + 1] =
                            (ndp[a][l + 1] + cur) % MOD;
                    }
                }
            }

            memcpy(dp, ndp, sizeof(dp));
        }

        long long ans = 0;

        for (int a = 0; a < 2; a++) {
            for (int l = 0; l < 3; l++) {
                ans = (ans + dp[a][l]) % MOD;
            }
        }

        return ans;
    }
};