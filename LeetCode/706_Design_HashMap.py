# Design a HashMap without using any built-in hash table libraries.

# Implement the MyHashMap class:

# MyHashMap() initializes the object with an empty map.
# void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
# int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
# void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
 

# Example 1:

# Input
# ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
# [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
# Output
# [null, null, null, 1, -1, null, 1, null, -1]

# Explanation
# MyHashMap myHashMap = new MyHashMap();
# myHashMap.put(1, 1); // The map is now [[1,1]]
# myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
# myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
# myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
# myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
# myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
# myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
# myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]
 

# Constraints:

# 0 <= key, value <= 106
# At most 104 calls will be made to put, get, and remove.







# Brute force:
class MyHashMap:

    def __init__(self):
        self.data = []

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.data)):
            if self.data[i][0] == key:
                self.data[i][1] = value
                return

        self.data.append([key, value])

    def get(self, key: int) -> int:
        for k, v in self.data:
            if k == key:
                return v

        return -1

    def remove(self, key: int) -> None:
        for i in range(len(self.data)):
            if self.data[i][0] == key:
                self.data.pop(i)
                return








# Optimal:
class MyHashMap:

    def __init__(self):
        self.size = 1009
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        index = self._hash(key)

        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return

        self.table[index].append([key, value])

    def get(self, key: int) -> int:
        index = self._hash(key)

        for k, v in self.table[index]:
            if k == key:
                return v

        return -1

    def remove(self, key: int) -> None:
        index = self._hash(key)

        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                self.table[index].pop(i)
                return
