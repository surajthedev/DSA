# You have a function printNumber that can be called with an integer parameter and prints it to the console.

# For example, calling printNumber(7) prints 7 to the console.
# You are given an instance of the class ZeroEvenOdd that has three functions: zero, even, and odd. The same instance of ZeroEvenOdd will be passed to three different threads:

# Thread A: calls zero() that should only output 0's.
# Thread B: calls even() that should only output even numbers.
# Thread C: calls odd() that should only output odd numbers.
# Modify the given class to output the series "010203040506..." where the length of the series must be 2n.

# Implement the ZeroEvenOdd class:

# ZeroEvenOdd(int n) Initializes the object with the number n that represents the numbers that should be printed.
# void zero(printNumber) Calls printNumber to output one zero.
# void even(printNumber) Calls printNumber to output one even number.
# void odd(printNumber) Calls printNumber to output one odd number.
 

# Example 1:

# Input: n = 2
# Output: "0102"
# Explanation: There are three threads being fired asynchronously.
# One of them calls zero(), the other calls even(), and the last one calls odd().
# "0102" is the correct output.
# Example 2:

# Input: n = 5
# Output: "0102030405"
 

# Constraints:

# 1 <= n <= 1000



# Brute force:
class ZeroEvenOdd:

    def __init__(self, n):
        self.n = n

        self.zero_turn = True
        self.odd_turn = False
        self.even_turn = False

    def zero(self, printNumber):
        for i in range(1, self.n + 1):

            # Wait until it is zero's turn
            while not self.zero_turn:
                pass

            printNumber(0)

            self.zero_turn = False

            if i % 2 == 1:
                self.odd_turn = True
            else:
                self.even_turn = True

    def even(self, printNumber):
        for i in range(2, self.n + 1, 2):

            while not self.even_turn:
                pass

            printNumber(i)

            self.even_turn = False
            self.zero_turn = True

    def odd(self, printNumber):
        for i in range(1, self.n + 1, 2):

            while not self.odd_turn:
                pass

            printNumber(i)

            self.odd_turn = False
            self.zero_turn = True







# Optimal:
from threading import Semaphore

class ZeroEvenOdd:

    def __init__(self, n):
        self.n = n

        self.zero_sem = Semaphore(1)
        self.odd_sem = Semaphore(0)
        self.even_sem = Semaphore(0)

    def zero(self, printNumber):
        for i in range(1, self.n + 1):

            self.zero_sem.acquire()

            printNumber(0)

            if i % 2 == 1:
                self.odd_sem.release()
            else:
                self.even_sem.release()

    def even(self, printNumber):
        for i in range(2, self.n + 1, 2):

            self.even_sem.acquire()

            printNumber(i)

            self.zero_sem.release()

    def odd(self, printNumber):
        for i in range(1, self.n + 1, 2):

            self.odd_sem.acquire()

            printNumber(i)

            self.zero_sem.release()