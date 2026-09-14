# Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
# A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
# If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

# Implement the MyLinkedList class:

# MyLinkedList() Initializes the MyLinkedList object.
# int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
# void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
# void addAtTail(int val) Append a node of value val as the last element of the linked list.
# void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
# void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
 

# Example 1:

# Input
# ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
# [[], [1], [3], [1, 2], [1], [1], [1]]
# Output
# [null, null, null, null, 2, null, 3]

# Explanation
# MyLinkedList myLinkedList = new MyLinkedList();
# myLinkedList.addAtHead(1);
# myLinkedList.addAtTail(3);
# myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
# myLinkedList.get(1);              // return 2
# myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
# myLinkedList.get(1);              // return 3
 

# Constraints:

# 0 <= index, val <= 1000
# Please do not use the built-in LinkedList library.
# At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and deleteAtIndex.







# Brute force:
class MyLinkedList:

    def __init__(self):
        self.data = []

    def get(self, index: int) -> int:
        if index < 0 or index >= len(self.data):
            return -1
        return self.data[index]

    def addAtHead(self, val: int) -> None:
        self.data.insert(0, val)

    def addAtTail(self, val: int) -> None:
        self.data.append(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            index = 0

        if index <= len(self.data):
            self.data.insert(index, val)

    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < len(self.data):
            self.data.pop(index)









# Optimal:
class Node:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        curr = self.head

        for _ in range(index):
            curr = curr.next

        return curr.val

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
        else:
            curr = self.head

            while curr.next:
                curr = curr.next

            curr.next = new_node

        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            index = 0

        if index > self.size:
            return

        if index == 0:
            self.addAtHead(val)
            return

        new_node = Node(val)
        curr = self.head

        for _ in range(index - 1):
            curr = curr.next

        new_node.next = curr.next
        curr.next = new_node

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return

        curr = self.head

        for _ in range(index - 1):
            curr = curr.next

        curr.next = curr.next.next
        self.size -= 1
