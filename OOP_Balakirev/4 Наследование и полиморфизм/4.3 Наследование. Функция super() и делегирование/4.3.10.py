class ItemAttrs:

    def __init__(self,*args):
        self.lst = list(args)

    def __getitem__(self,key):
        return self.lst[key]

    def __setitem__(self,key,value):
        self.lst[key] = value

class Point(ItemAttrs):
    pass

pt = Point(1, 2.5)
x = pt[0]   # 1
y = pt[1]   # 2.5
pt[0] = 10