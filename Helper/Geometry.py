class Vector2:
    def __init__(self, _x=0, _y=0):
        self.x = _x
        self.y = _y

    @staticmethod
    def zero():
        v = Vector2(0,0)
        return v

    @staticmethod
    def one():
        v = Vector2(1,1)
        return v
        
    def __str__(self):
        return '({0},{1})'.format(self.x,self.y)

class Vector3(Vector2):
    def __init__(self, _x=0, _y=0, _z=0):
        super().__init__(_x,_y)
        self.z = _z

    @staticmethod
    def zero():
        v = Vector3(0,0,0)
        return v
        
    @staticmethod
    def one():
        v = Vector3(1,1,1)
        return v

    def __str__(self):
        return '({0},{1},{2})'.format(self.x,self.y,self.z)

v = Vector3(2,8,6)
print(v)


  