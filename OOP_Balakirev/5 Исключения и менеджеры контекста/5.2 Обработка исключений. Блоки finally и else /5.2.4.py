a = '5 6'
a = a.split()
try:
    a = (int(a[0]) + int(a[1]))
except:
    a = a[0] + a[1]
finally:
    print(a)
