import math
from MyQueue import Queue
class PriorityQueue(Queue):
    def __init__(self, _sortFunction = None, _ascending = True, _initialElements = []):
        super().__init__()
        self.ascending = _ascending
        setattr(PriorityQueue, "sortFunction", _sortFunction)
        if(_sortFunction is None):
            self.sortFunction = self.defaultsortFunction
        for el in _initialElements:
            self.enqueue(el)

    def defaultsortFunction(self, item1, item2):
        # item1 must be at a lower level in tree than item2
        if(self.ascending):
            return item1 < item2
        else: 
            return item1 > item2

    def topDownHeapify(self, i):
        focus = i
        left = 2 * i + 1
        right = 2 * i + 2
        arr = self._queue

        if(left < self.size and self.sortFunction(arr[left], arr[focus])):
            focus = left
        
        if(right < self.size and self.sortFunction(arr[right], arr[focus])):
            focus = right

        if(focus != i):
            arr[i], arr[focus] = arr[focus], arr[i]
            self.topDownHeapify(focus)

    def bottomUpHeapify(self):
        i = self.size - 1
        arr = self._queue
        while(i > 0):
            parent_idx = math.floor((i-1)/2) 
            if(self.sortFunction(arr[i],arr[parent_idx])):
                arr[i], arr[parent_idx] = arr[parent_idx], arr[i]
            i = parent_idx
        self._queue = arr

    def enqueue(self, item):
        super().enqueue(item)
        self.bottomUpHeapify()

    def dequeue(self):
        # Replace the top element with last element
        self._queue[0] = self._queue[self.size-1]
        self.topDownHeapify(0)
        return self._queue.pop()

    def __str__(self):
        q = [str(x) for x in self._queue]
        return '[' + ','.join(q) + ']'

def MysortFunction(pq, item1, item2):
    # item1 must be at a lower level in tree than item2
    if(pq.ascending):
        return item1['roll'] < item2['roll']
    else: 
        return item1['roll'] > item2['roll']

pq = PriorityQueue(_ascending=False, _initialElements=[9,12,13,22,29,56,85,90]) 
print(pq)
pq.dequeue()
pq.dequeue()
pq.dequeue()
pq.dequeue()
pq.dequeue()
pq.dequeue()
pq.dequeue()
pq.dequeue()
print(pq.size)
# pq.enqueue({"roll":9, "name": 'U'})
# pq.enqueue({"roll":12, "name": 'Y'})
# pq.enqueue({"roll":13, "name": 'E'})
# pq.enqueue({"roll":21, "name": 'V'})
# pq.enqueue({"roll":22, "name": '0'})
# pq.enqueue({"roll":45, "name": '0'})
# pq.enqueue({"roll":86, "name": 'L'})
# pq.enqueue({"roll":90, "name": 'I'})
print(pq)



