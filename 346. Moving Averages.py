from queue import Queue
class MovingAverage:

    def __init__(self, size):
        self.queue = Queue()
        self.maxSize = size
        self.totalSum = 0

    def next(self, val):
        if self.queue.qsize() == self.maxSize:
            self.totalSum -= self.queue.get()

        self.queue.put(val)
        self.totalSum += val
        return self.totalSum / self.queue.qsize()
