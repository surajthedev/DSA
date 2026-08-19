# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

# Example 1:

# Input: s = "IceCreAm"

# Output: "AceCreIm"

# Explanation:

# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:

# Input: s = "leetcode"

# Output: "leotcede"

 

# Constraints:

# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.






# Brute force:
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        
        chars = list(s)
        
        # Step 1: Collect vowels
        vowel_list = []

        for ch in chars:
            if ch in vowels:
                vowel_list.append(ch)

        # Step 2: Reverse vowels
        vowel_list.reverse()

        # Step 3: Put reversed vowels back
        j = 0

        for i in range(len(chars)):
            if chars[i] in vowels:
                chars[i] = vowel_list[j]
                j += 1

        return "".join(chars)







# Optimal:
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        chars = list(s)

        left = 0
        right = len(chars) - 1

        while left < right:

            # Find vowel from left
            while left < right and chars[left] not in vowels:
                left += 1

            # Find vowel from right
            while left < right and chars[right] not in vowels:
                right -= 1

            # Swap vowels
            chars[left], chars[right] = chars[right], chars[left]

            left += 1
            right -= 1

        return "".join(chars)