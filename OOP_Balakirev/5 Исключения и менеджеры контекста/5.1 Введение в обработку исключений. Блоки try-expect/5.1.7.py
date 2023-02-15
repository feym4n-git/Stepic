# считывание строки и разбиение ее по пробелам
# lst_in = input().split()
lst_in = 'hello 1 world -2 4.5 True'.split()

def check(value):
    try:
        return int(value)
    except:
        try:
            return float(value)
        except:
            return value


lst_out = list(map(check, filter(check, lst_in)))
print(lst_out)
