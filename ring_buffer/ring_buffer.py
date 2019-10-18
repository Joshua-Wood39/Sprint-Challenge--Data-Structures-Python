class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        print(f"store: {self.storage}, capacity: {self.capacity}")
        if len(self.storage) == self.capacity:
            print(f"current: {self.current}")
            self.storage[self.current] = item
            if self.current == self.capacity - 1:
                self.current = 0
            else:
                self.current += 1
        else:
            self.storage.append(item)

    def get(self):
        result = []
        for value in self.storage:
            if value != None:
                result.append(value)
        return result
