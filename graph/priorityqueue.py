class PriorityQueue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)
        self.queue.sort(key=lambda x: x[0])

    def pop(self):
        if not self.queue:
            raise IndexError("pop from empty priorityqueue")

        return self.queue.pop(0)

    def __len__(self):
        return len(self.queue)
