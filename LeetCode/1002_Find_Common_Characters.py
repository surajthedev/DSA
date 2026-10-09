# Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.



# Example 1:

# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]
# Example 2:

# Input: words = ["cool","lock","cook"]
# Output: ["c","o"]


# Constraints:

# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists of lowercase English letters.
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# ### Brute Force

python
```

from collections import Counter

class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        result = []
        first = list(words[0])

        for ch in first:
            if all(ch in word for word in words[1:]):
                result.append(ch)
                words = [word.replace(ch, '', 1) for word in words]

        return result
```

### Optimal — O(n × m) Time

python
```

from collections import Counter

class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        common = Counter(words[0])

        for word in words[1:]:
            common &= Counter(word)

        result = []

        for ch, count in common.items():
            result.extend([ch] * count)

        return result
```
