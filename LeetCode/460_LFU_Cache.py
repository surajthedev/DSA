# Design and implement a data structure for a Least Frequently Used (LFU) cache.

# Implement the LFUCache class:

# LFUCache(int capacity) Initializes the object with the capacity of the data structure.
# int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
# void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.
# To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.

# When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.

# The functions get and put must each run in O(1) average time complexity.

 

# Example 1:

# Input
# ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, 3, null, -1, 3, 4]

# Explanation
# // cnt(x) = the use counter for key x
# // cache=[] will show the last used order for tiebreakers (leftmost element is  most recent)
# LFUCache lfu = new LFUCache(2);
# lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
# lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
# lfu.get(1);      // return 1
#                  // cache=[1,2], cnt(2)=1, cnt(1)=2
# lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
#                  // cache=[3,1], cnt(3)=1, cnt(1)=2
# lfu.get(2);      // return -1 (not found)
# lfu.get(3);      // return 3
#                  // cache=[3,1], cnt(3)=2, cnt(1)=2
# lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
#                  // cache=[4,3], cnt(4)=1, cnt(3)=2
# lfu.get(1);      // return -1 (not found)
# lfu.get(3);      // return 3
#                  // cache=[3,4], cnt(4)=1, cnt(3)=3
# lfu.get(4);      // return 4
#                  // cache=[4,3], cnt(4)=2, cnt(3)=3
 

# Constraints:

# 1 <= capacity <= 104
# 0 <= key <= 105
# 0 <= value <= 109
# At most 2 * 105 calls will be made to get and put.




# Brute force:
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.time = 0

        # key -> [value, frequency, last_used_time]
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        value, freq, _ = self.cache[key]

        self.time += 1

        # Increase frequency and update recent time
        self.cache[key] = [value, freq + 1, self.time]

        return value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        self.time += 1

        # Key already exists
        if key in self.cache:
            _, freq, _ = self.cache[key]

            self.cache[key] = [value, freq + 1, self.time]
            return

        # Cache full -> evict LFU/LRU
        if len(self.cache) == self.capacity:

            # Find key with:
            # 1. smallest frequency
            # 2. oldest last_used_time in case of tie
            lfu_key = min(
                self.cache,
                key=lambda k: (self.cache[k][1], self.cache[k][2])
            )

            del self.cache[lfu_key]

        # New key starts with frequency 1
        self.cache[key] = [value, 1, self.time]







# Optimal:
class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        # Dummy nodes
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.size = 0

    def add_first(self, node):
        """
        Add node right after head.
        This means node becomes MRU.
        """

        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

        self.size += 1

    def remove(self, node):
        """
        Remove a specific node.
        """

        node.prev.next = node.next
        node.next.prev = node.prev

        self.size -= 1

    def remove_last(self):
        """
        Remove and return LRU node.
        """

        if self.size == 0:
            return None

        lru = self.tail.prev
        self.remove(lru)

        return lru


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0

        # key -> Node
        self.key_to_node = {}

        # frequency -> DoublyLinkedList
        self.freq_to_list = {}

        # Minimum frequency currently present
        self.min_freq = 0

    def _increase_frequency(self, node):
        old_freq = node.freq

        # Remove node from old frequency list
        old_list = self.freq_to_list[old_freq]
        old_list.remove(node)

        # If old list becomes empty and it was min_freq,
        # increase min_freq.
        if old_freq == self.min_freq and old_list.size == 0:
            self.min_freq += 1

        # Increase node's frequency
        node.freq += 1

        new_freq = node.freq

        # Create list for new frequency if needed
        if new_freq not in self.freq_to_list:
            self.freq_to_list[new_freq] = DoublyLinkedList()

        # Add node as MRU
        self.freq_to_list[new_freq].add_first(node)

    def get(self, key: int) -> int:

        # Key doesn't exist
        if key not in self.key_to_node:
            return -1

        node = self.key_to_node[key]

        # Using the key increases its frequency
        self._increase_frequency(node)

        return node.value

    def put(self, key: int, value: int) -> None:

        if self.capacity == 0:
            return

        # Key already exists
        if key in self.key_to_node:

            node = self.key_to_node[key]

            # Update value
            node.value = value

            # put() also counts as usage
            self._increase_frequency(node)

            return

        # Cache is full
        if self.size == self.capacity:

            # Get list of minimum frequency
            min_list = self.freq_to_list[self.min_freq]

            # Remove LRU node from that frequency
            lru_node = min_list.remove_last()

            # Remove from hashmap
            del self.key_to_node[lru_node.key]

            self.size -= 1

        # Create new node
        new_node = Node(key, value)

        # New key always starts with frequency 1
        self.key_to_node[key] = new_node

        # Create frequency-1 list if necessary
        if 1 not in self.freq_to_list:
            self.freq_to_list[1] = DoublyLinkedList()

        # New node is MRU in frequency-1 list
        self.freq_to_list[1].add_first(new_node)

        # New minimum frequency is 1
        self.min_freq = 1

        self.size += 1