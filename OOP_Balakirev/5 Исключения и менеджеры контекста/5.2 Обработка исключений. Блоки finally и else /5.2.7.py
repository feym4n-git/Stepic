def get_loss(w1, w2, w3, w4):
    try:
        res = 10 * w1 // w2 - 5 * w2 * w3 + w4
    except ZeroDivisionError:
        res = 10 * w1 - 5 * w2 * w3 + w4
        return "деление на ноль"
