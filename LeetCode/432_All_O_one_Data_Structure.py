# Design a data structure to store the strings' count with the ability to return the strings with minimum and maximum counts.

# Implement the AllOne class:

# AllOne() Initializes the object of the data structure.
# inc(String key) Increments the count of the string key by 1. If key does not exist in the data structure, insert it with count 1.
# dec(String key) Decrements the count of the string key by 1. If the count of key is 0 after the decrement, remove it from the data structure. It is guaranteed that key exists in the data structure before the decrement.
# getMaxKey() Returns one of the keys with the maximal count. If no element exists, return an empty string "".
# getMinKey() Returns one of the keys with the minimum count. If no element exists, return an empty string "".
# Note that each function must run in O(1) average time complexity.

 

# Example 1:

# Input
# ["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
# [[], ["hello"], ["hello"], [], [], ["leet"], [], []]
# Output
# [null, null, null, "hello", "hello", null, "hello", "leet"]

# Explanation
# AllOne allOne = new AllOne();
# allOne.inc("hello");
# allOne.inc("hello");
# allOne.getMaxKey(); // return "hello"
# allOne.getMinKey(); // return "hello"
# allOne.inc("leet");
# allOne.getMaxKey(); // return "hello"
# allOne.getMinKey(); // return "leet"
 

# Constraints:

# 1 <= key.length <= 10
# key consists of lowercase English letters.
# It is guaranteed that for each call to dec, key is existing in the data structure.
# At most 5 * 104 calls will be made to inc, dec, getMaxKey, and getMinKey.







# Solution:
class Node:
    def __init__(self, count=0):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None


class AllOne:

    def __init__(self):
        # Dummy nodes
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

        # key -> bucket node
        self.key_to_node = {}

    # Insert new_node after prev_node
    def insert_after(self, prev_node, new_node):
        new_node.next = prev_node.next
        new_node.prev = prev_node

        prev_node.next.prev = new_node
        prev_node.next = new_node

    # Remove a node from linked list
    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def inc(self, key: str) -> None:

        # Case 1: key doesn't exist
        if key not in self.key_to_node:

            # Check if count=1 bucket already exists
            first = self.head.next

            if first != self.tail and first.count == 1:
                node = first
            else:
                node = Node(1)
                self.insert_after(self.head, node)

            node.keys.add(key)
            self.key_to_node[key] = node

        # Case 2: key already exists
        else:
            curr = self.key_to_node[key]
            next_node = curr.next

            # count + 1 bucket already exists
            if next_node != self.tail and next_node.count == curr.count + 1:
                new_node = next_node

            # Create count + 1 bucket
            else:
                new_node = Node(curr.count + 1)
                self.insert_after(curr, new_node)

            # Move key
            curr.keys.remove(key)
            new_node.keys.add(key)

            self.key_to_node[key] = new_node

            # Current bucket empty
            if not curr.keys:
                self.remove_node(curr)

    def dec(self, key: str) -> None:

        curr = self.key_to_node[key]

        # count becomes 0 -> remove key
        if curr.count == 1:

            del self.key_to_node[key]
            curr.keys.remove(key)

            if not curr.keys:
                self.remove_node(curr)

        else:
            prev_node = curr.prev

            # count - 1 bucket already exists
            if prev_node != self.head and prev_node.count == curr.count - 1:
                new_node = prev_node

            # Create count - 1 bucket
            else:
                new_node = Node(curr.count - 1)
                self.insert_after(prev_node, new_node)

            # Move key
            curr.keys.remove(key)
            new_node.keys.add(key)

            self.key_to_node[key] = new_node

            # Current bucket empty
            if not curr.keys:
                self.remove_node(curr)

    def getMaxKey(self) -> str:

        if self.tail.prev == self.head:
            return ""

        max_node = self.tail.prev

        return next(iter(max_node.keys))

    def getMinKey(self) -> str:

        if self.head.next == self.tail:
            return ""

        min_node = self.head.next

        return next(iter(min_node.keys))
