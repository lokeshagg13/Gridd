
class PriorityQueue(Queue):
    def __init__(self, list = [], _ascending = True, _sortFunc = None):
        super().__init__(*list)
        self.ascending = _ascending
        if(_sortFunc is None):
            _sortFunc = self.defaultSortFunc

    def defaultSortFunc(self):
        pass

    def enqueue(self, item):
        self.queue.append(item)


# q = Queue(53,46,100,98,96,82,16,4,13,82)
# q.enqueue(1)
# q.enqueue(-1)
# q.dequeue()
# print(q.size)
# print(q)