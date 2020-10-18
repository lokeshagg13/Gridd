class Node:
    def __init__(self):
        self.gridX = 0
        self.gridY = 0
        self.walkable = False
        self.gcost = 0
        self.hcost = 0
        self.parent = None

# please add create Node function here according to __init__
    def __init__(self, gx, gy, walkable):
        self.gridX = gx
        self.gridY = gy
        self.walkable = walkable
        self.parent = None
        self.gcost = 0
        self.hcost = 0

    @property
    def fcost(self):
        return self.gcost + self.hcost

    