# You have the four functions:

# printFizz that prints the word "fizz" to the console,
# printBuzz that prints the word "buzz" to the console,
# printFizzBuzz that prints the word "fizzbuzz" to the console, and
# printNumber that prints a given integer to the console.
# You are given an instance of the class FizzBuzz that has four functions: fizz, buzz, fizzbuzz and number. The same instance of FizzBuzz will be passed to four different threads:

# Thread A: calls fizz() that should output the word "fizz".
# Thread B: calls buzz() that should output the word "buzz".
# Thread C: calls fizzbuzz() that should output the word "fizzbuzz".
# Thread D: calls number() that should only output the integers.
# Modify the given class to output the series [1, 2, "fizz", 4, "buzz", ...] where the ith token (1-indexed) of the series is:

# "fizzbuzz" if i is divisible by 3 and 5,
# "fizz" if i is divisible by 3 and not 5,
# "buzz" if i is divisible by 5 and not 3, or
# i if i is not divisible by 3 or 5.
# Implement the FizzBuzz class:

# FizzBuzz(int n) Initializes the object with the number n that represents the length of the sequence that should be printed.
# void fizz(printFizz) Calls printFizz to output "fizz".
# void buzz(printBuzz) Calls printBuzz to output "buzz".
# void fizzbuzz(printFizzBuzz) Calls printFizzBuzz to output "fizzbuzz".
# void number(printNumber) Calls printnumber to output the numbers.
 

# Example 1:

# Input: n = 15
# Output: [1,2,"fizz",4,"buzz","fizz",7,8,"fizz","buzz",11,"fizz",13,14,"fizzbuzz"]
# Example 2:

# Input: n = 5
# Output: [1,2,"fizz",4,"buzz"]
 

# Constraints:

# 1 <= n <= 50





# Brute force:
class FizzBuzz:

    def __init__(self, n):
        self.n = n
        self.current = 1

    def fizz(self, printFizz):
        while self.current <= self.n:

            if self.current % 3 == 0 and self.current % 5 != 0:
                printFizz()
                self.current += 1

    def buzz(self, printBuzz):
        while self.current <= self.n:

            if self.current % 5 == 0 and self.current % 3 != 0:
                printBuzz()
                self.current += 1

    def fizzbuzz(self, printFizzBuzz):
        while self.current <= self.n:

            if self.current % 15 == 0:
                printFizzBuzz()
                self.current += 1

    def number(self, printNumber):
        while self.current <= self.n:

            if self.current % 3 != 0 and self.current % 5 != 0:
                printNumber(self.current)
                self.current += 1








# Optimal:
from threading import Condition

class FizzBuzz:

    def __init__(self, n):
        self.n = n
        self.current = 1
        self.condition = Condition()

    def fizz(self, printFizz):
        while True:
            with self.condition:

                while (
                    self.current <= self.n
                    and not (
                        self.current % 3 == 0
                        and self.current % 5 != 0
                    )
                ):
                    self.condition.wait()

                if self.current > self.n:
                    self.condition.notify_all()
                    return

                printFizz()

                self.current += 1
                self.condition.notify_all()

    def buzz(self, printBuzz):
        while True:
            with self.condition:

                while (
                    self.current <= self.n
                    and not (
                        self.current % 5 == 0
                        and self.current % 3 != 0
                    )
                ):
                    self.condition.wait()

                if self.current > self.n:
                    self.condition.notify_all()
                    return

                printBuzz()

                self.current += 1
                self.condition.notify_all()

    def fizzbuzz(self, printFizzBuzz):
        while True:
            with self.condition:

                while (
                    self.current <= self.n
                    and self.current % 15 != 0
                ):
                    self.condition.wait()

                if self.current > self.n:
                    self.condition.notify_all()
                    return

                printFizzBuzz()

                self.current += 1
                self.condition.notify_all()

    def number(self, printNumber):
        while True:
            with self.condition:

                while (
                    self.current <= self.n
                    and (
                        self.current % 3 == 0
                        or self.current % 5 == 0
                    )
                ):
                    self.condition.wait()

                if self.current > self.n:
                    self.condition.notify_all()
                    return

                printNumber(self.current)

                self.current += 1
                self.condition.notify_all()