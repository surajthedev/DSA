# Suppose we have a class:

# public class Foo {
#   public void first() { print("first"); }
#   public void second() { print("second"); }
#   public void third() { print("third"); }
# }
# The same instance of Foo will be passed to three different threads. Thread A will call first(), thread B will call second(), and thread C will call third(). Design a mechanism and modify the program to ensure that second() is executed after first(), and third() is executed after second().

# Note:

# We do not know how the threads will be scheduled in the operating system, even though the numbers in the input seem to imply the ordering. The input format you see is mainly to ensure our tests' comprehensiveness.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: "firstsecondthird"
# Explanation: There are three threads being fired asynchronously. The input [1,2,3] means thread A calls first(), thread B calls second(), and thread C calls third(). "firstsecondthird" is the correct output.
# Example 2:

# Input: nums = [1,3,2]
# Output: "firstsecondthird"
# Explanation: The input [1,3,2] means thread A calls first(), thread B calls third(), and thread C calls second(). "firstsecondthird" is the correct output.
 

# Constraints:

# nums is a permutation of [1, 2, 3].




# Brute force:
from threading import Lock

class Foo:

    def __init__(self):
        self.first_done = False
        self.second_done = False

    def first(self, printFirst) -> None:
        printFirst()
        self.first_done = True

    def second(self, printSecond) -> None:
        while not self.first_done:
            pass

        printSecond()
        self.second_done = True

    def third(self, printThird) -> None:
        while not self.second_done:
            pass

        printThird()





# Optimal:
from threading import Event

class Foo:

    def __init__(self):
        self.first_done = Event()
        self.second_done = Event()

    def first(self, printFirst) -> None:
        printFirst()
        self.first_done.set()

    def second(self, printSecond) -> None:
        self.first_done.wait()

        printSecond()
        self.second_done.set()

    def third(self, printThird) -> None:
        self.second_done.wait()

        printThird()