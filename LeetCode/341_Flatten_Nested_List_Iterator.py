# You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.

# Implement the NestedIterator class:

# NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
# int next() Returns the next integer in the nested list.
# boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.
# Your code will be tested with the following pseudocode:

# initialize iterator with nestedList
# res = []
# while iterator.hasNext()
#     append iterator.next() to the end of res
# return res
# If res matches the expected flattened list, then your code will be judged as correct.

 

# Example 1:

# Input: nestedList = [[1,1],2,[1,1]]
# Output: [1,1,2,1,1]
# Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].
# Example 2:

# Input: nestedList = [1,[4,[6]]]
# Output: [1,4,6]
# Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].
 

# Constraints:

# 1 <= nestedList.length <= 500
# The values of the integers in the nested list is in the range [-106, 106].





# Brute force:
class NestedIterator:

    def __init__(self, nestedList):
        self.result = []
        self.index = 0

        self.flatten(nestedList)

    def flatten(self, nestedList):
        for item in nestedList:
            if item.isInteger():
                self.result.append(item.getInteger())
            else:
                self.flatten(item.getList())

    def next(self):
        value = self.result[self.index]
        self.index += 1
        return value

    def hasNext(self):
        return self.index < len(self.result)






# Optimal:
class NestedIterator:

    def __init__(self, nestedList):
        self.stack = nestedList[::-1]

    def next(self):
        self.hasNext()
        return self.stack.pop().getInteger()

    def hasNext(self):
        while self.stack:

            top = self.stack[-1]

            # If top is an integer, we are ready
            if top.isInteger():
                return True

            # Otherwise remove the list
            self.stack.pop()

            # Add its elements in reverse order
            for item in reversed(top.getList()):
                self.stack.append(item)

        return False