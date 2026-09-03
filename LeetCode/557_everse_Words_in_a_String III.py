# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

# Example 1:

# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Example 2:

# Input: s = "Mr Ding"
# Output: "rM gniD"
 

# Constraints:

# 1 <= s.length <= 5 * 104
# s contains printable ASCII characters.
# s does not contain any leading or trailing spaces.
# There is at least one word in s.
# All the words in s are separated by a single space.








# Brute force:
class Solution {
public:
    string reverseWords(string s) {
        string ans = "";
        string word = "";

        for (char c : s) {
            if (c == ' ') {
                reverse(word.begin(), word.end());
                ans += word;
                ans += ' ';
                word = "";
            } else {
                word += c;
            }
        }

        reverse(word.begin(), word.end());
        ans += word;

        return ans;
    }
};







# Optimal:
class Solution {
public:
    string reverseWords(string s) {
        int start = 0;

        for (int i = 0; i <= s.size(); i++) {
            if (i == s.size() || s[i] == ' ') {
                reverse(s.begin() + start, s.begin() + i);
                start = i + 1;
            }
        }

        return s;
    }
};