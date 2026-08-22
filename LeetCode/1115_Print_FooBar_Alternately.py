# from threading import Event

# class Foo:

#     def __init__(self):
#         self.first_done = Event()
#         self.second_done = Event()

#     def first(self, printFirst) -> None:
#         printFirst()
#         self.first_done.set()

#     def second(self, printSecond) -> None:
#         self.first_done.wait()

#         printSecond()
#         self.second_done.set()

#     def third(self, printThird) -> None:
#         self.second_done.wait()

#         printThird()





# Brute force:
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

class FooBar:

    def __init__(self, n):
        self.n = n
        self.foo_event = Event()
        self.bar_event = Event()

        # foo ko initially run karne dena hai
        self.foo_event.set()

    def foo(self, printFoo) -> None:
        for i in range(self.n):
            self.foo_event.wait()
            self.foo_event.clear()

            printFoo()

            self.bar_event.set()

    def bar(self, printBar) -> None:
        for i in range(self.n):
            self.bar_event.wait()
            self.bar_event.clear()

            printBar()

            self.foo_event.set()