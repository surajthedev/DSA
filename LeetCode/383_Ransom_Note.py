# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

 

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true
 

# Constraints:

# 1 <= ransomNote.length, magazine.length <= 105
# ransomNote and magazine consist of lowercase English letters.




# Brute force:
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = list(magazine)

        for char in ransomNote:
            if char in letters:
                letters.remove(char)
            else:
                return False

        return True






# Optimal:
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = {}

        # Count characters in magazine
        for char in magazine:
            count[char] = count.get(char, 0) + 1

        # Use characters for ransomNote
        for char in ransomNote:
            if count.get(char, 0) == 0:
                return False

            count[char] -= 1

        return True