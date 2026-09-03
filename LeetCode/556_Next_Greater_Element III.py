# Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.

# Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.

 

# Example 1:

# Input: n = 12
# Output: 21
# Example 2:

# Input: n = 21
# Output: -1
 

# Constraints:

# 1 <= n <= 231 - 1







# Brute force:
class Solution {
public:
    int nextGreaterElement(int n) {
        string s = to_string(n);
        sort(s.begin(), s.end());

        long long limit = INT_MAX;

        do {
            long long num = stoll(s);

            if (num > n && num <= limit)
                return (int)num;

        } while (next_permutation(s.begin(), s.end()));

        return -1;
    }
};





# Optimal:
class Solution {
public:
    int nextGreaterElement(int n) {
        string s = to_string(n);

        int i = s.size() - 2;

        while (i >= 0 && s[i] >= s[i + 1]) {
            i--;
        }

        if (i < 0)
            return -1;

        int j = s.size() - 1;

        while (s[j] <= s[i]) {
            j--;
        }

        swap(s[i], s[j]);

        reverse(s.begin() + i + 1, s.end());

        long long ans = stoll(s);

        if (ans > INT_MAX)
            return -1;

        return (int)ans;
    }
};