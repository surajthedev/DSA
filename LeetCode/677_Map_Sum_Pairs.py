# Design a map that allows you to do the following:

# Maps a string key to a given value.
# Returns the sum of the values that have a key with a prefix equal to a given string.
# Implement the MapSum class:

# MapSum() Initializes the MapSum object.
# void insert(String key, int val) Inserts the key-val pair into the map. If the key already existed, the original key-value pair will be overridden to the new one.
# int sum(string prefix) Returns the sum of all the pairs' value whose key starts with the prefix.
 

# Example 1:

# Input
# ["MapSum", "insert", "sum", "insert", "sum"]
# [[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
# Output
# [null, null, 3, null, 5]

# Explanation
# MapSum mapSum = new MapSum();
# mapSum.insert("apple", 3);  
# mapSum.sum("ap");           // return 3 (apple = 3)
# mapSum.insert("app", 2);    
# mapSum.sum("ap");           // return 5 (apple + app = 3 + 2 = 5)
 

# Constraints:

# 1 <= key.length, prefix.length <= 50
# key and prefix consist of only lowercase English letters.
# 1 <= val <= 1000
# At most 50 calls will be made to insert and sum.







# Brute force:
class MapSum:

    def __init__(self):
        self.mp = {}

    def insert(self, key, val):
        self.mp[key] = val

    def sum(self, prefix):
        total = 0

        for key, val in self.mp.items():
            if key.startswith(prefix):
                total += val

        return total










# Optimal:
class TrieNode:

    def __init__(self):
        self.children = {}
        self.value = 0


class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.values = {}

    def insert(self, key, val):
        diff = val - self.values.get(key, 0)
        self.values[key] = val

        node = self.root

        for ch in key:
            if ch not in node.children:
                node.children[ch] = TrieNode()

            node = node.children[ch]
            node.value += diff

    def sum(self, prefix):
        node = self.root

        for ch in prefix:
            if ch not in node.children:
                return 0

            node = node.children[ch]

        return node.value