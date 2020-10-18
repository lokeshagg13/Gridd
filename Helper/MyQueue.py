class Queue:
    def __init__(self,*args):
        self._queue = []

        for arg in args:
            self._queue.append(arg)
        
        
    def enqueue(self, item):
        self._queue.append(item)

    def dequeue(self):
        if(self.size <= 0):
            return None
        return self._queue.pop(0)

    @property
    def size(self):
        return len(self._queue)

    def __str__(self):
        q = [str(x) for x in self._queue]
        return '[' + ','.join(q) + ']'
