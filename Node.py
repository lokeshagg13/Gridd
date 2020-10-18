class Node:
    def __init__(self):
        gridX = 0
        gridY = 0
        walkable = False
        gcost = 0
        hcost = 0
        parent = None

    @property
    def fcost(self):
        return self.gcost + self.hcost

    