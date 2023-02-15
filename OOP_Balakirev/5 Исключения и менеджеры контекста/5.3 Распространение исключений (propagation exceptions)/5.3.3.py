def input_int_numbers(inp):
    inp = inp.strip().split()
    try:
        return tuple(map(int, inp))
    except:
        raise TypeError('все числа должны быть целыми')

x = input()
while True:
    try:
        x = input_int_numbers(x)
        print(' '.join(map(str, x)))
        break
    except TypeError:
        x = input()

