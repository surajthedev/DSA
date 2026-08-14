# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:

# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

 

# Example 1:

# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]

# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4
 

# Constraints:

# 1 <= capacity <= 3000
# 0 <= key <= 104
# 0 <= value <= 105
# At most 2 * 105 calls will be made to get and put.





# Brute force:
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = []

    def get(self, key: int) -> int:
        for i, (k, v) in enumerate(self.cache):
            if k == key:
                # Recently used, so end mein move karo
                self.cache.pop(i)
                self.cache.append((k, v))
                return v

        return -1

    def put(self, key: int, value: int) -> None:
        # Check if key already exists
        for i, (k, v) in enumerate(self.cache):
            if k == key:
                self.cache.pop(i)
                self.cache.append((key, value))
                return

        # New key
        self.cache.append((key, value))

        # Capacity exceed ho gayi
        if len(self.cache) > self.capacity:
            self.cache.pop(0)








# Optimal:
class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        # key -> Node
        self.cache = {}

        # Dummy nodes
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    # Node ko linked list se remove karo
    def remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    # Node ko tail se pehle add karo
    # Yaani MRU position
    def add_to_end(self, node):
        prev_node = self.tail.prev

        prev_node.next = node
        node.prev = prev_node

        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Recently used -> MRU position
        self.remove(node)
        self.add_to_end(node)

        return node.value

    def put(self, key: int, value: int) -> None:

        # Key already exists
        if key in self.cache:

            node = self.cache[key]

            # Value update
            node.value = value

            # MRU position par move karo
            self.remove(node)
            self.add_to_end(node)

            return

        # New node
        node = Node(key, value)

        self.cache[key] = node
        self.add_to_end(node)

        # Capacity exceed
        if len(self.cache) > self.capacity:

            # Head ke immediately baad wala = LRU
            lru = self.head.next

            self.remove(lru)

            del self.cache[lru.key]