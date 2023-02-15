class Point:

    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y


a = '5 6'
a = a.split()
print(a)
try:
    a = Point(int(a[0]), int(a[1]))
except:
    try:
        a = Point(float(a[0]), float(a[1]))
    except:
        a = Point()
finally:
    print(f"Point: x = {a._x}, y = {a._y}")
