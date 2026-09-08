# You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.

# Return the minimum number of CPU intervals required to complete all tasks.

 

# Example 1:

# Input: tasks = ["A","A","A","B","B","B"], n = 2

# Output: 8

# Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

# After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th interval, you can do A again as 2 intervals have passed.

# Example 2:

# Input: tasks = ["A","C","A","B","D","B"], n = 1

# Output: 6

# Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.

# With a cooling interval of 1, you can repeat a task after just one other task.

# Example 3:

# Input: tasks = ["A","A","A", "B","B","B"], n = 3

# Output: 10

# Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.

# There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.

 

# Constraints:

# 1 <= tasks.length <= 104
# tasks[i] is an uppercase English letter.
# 0 <= n <= 100










# BRute force:
class Solution:
    def leastInterval(self, tasks, n):
        from collections import Counter

        freq = Counter(tasks)
        time = 0

        while freq:
            available = sorted(freq, key=freq.get, reverse=True)
            used = 0

            for task in available:
                if used == n + 1:
                    break

                if freq[task] > 0:
                    freq[task] -= 1
                    used += 1

                    if freq[task] == 0:
                        del freq[task]

            time += n + 1 if freq else used

        return time








# Optimal:
class Solution:
    def leastInterval(self, tasks, n):
        from collections import Counter

        freq = Counter(tasks)
        max_freq = max(freq.values())

        max_count = sum(1 for v in freq.values() if v == max_freq)

        return max(
            len(tasks),
            (max_freq - 1) * (n + 1) + max_count
        )