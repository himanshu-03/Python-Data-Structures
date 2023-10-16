# Program Name: priority_queue.py
# Implementing a priority queue using heapq

import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.index = 0

    def push(self, item, priority):
        heapq.heappush(self.heap, (-priority, self.index, item))
        self.index += 1

    def pop(self):
        _, _, item = heapq.heappop(self.heap)
        return item

# Usage
pq = PriorityQueue()
pq.push("Task 1", 3)
pq.push("Task 2", 1)
pq.push("Task 3", 2)
print(pq.pop())
print(pq.pop())
