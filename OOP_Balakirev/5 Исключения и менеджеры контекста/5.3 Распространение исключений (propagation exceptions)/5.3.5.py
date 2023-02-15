class Test:

    def __init__(self, descr):
        if not 10 <= len(descr) <= 100:
            raise ValueError('формулировка теста должна быть от 10 до 10 000 символов')
        self.descr = descr


    def run(self):
        raise NotImplementedError


class TestAnsDigit(Test):

    def __init__(self, descr, ans_digit: int, max_error_digit=0.01):
        super().__init__(descr)
        self.ans_digit = ans_digit
        self.max_error_digit = max_error_digit
        self.check()

    def check(self):
        if type(self.ans_digit) not in (int,float):
            raise ValueError('недопустимые значения аргументов теста')
        if type(self.max_error_digit) not in (int,float) or self.max_error_digit < 0:
            raise ValueError('недопустимые значения аргументов теста')

    def run(self):
        ans = float(input())
        if self.ans_digit - self.max_error_digit <= ans <= self.ans_digit + self.max_error_digit:
            return True
        return False


descr, ans = map(str.strip, input().split('|'))  # например: Какое значение получится при вычислении 2+2? | 4
ans = float(ans) # здесь для простоты полагаем, что ans точно число и ошибок в преобразовании быть не может
try:
    x = TestAnsDigit(descr, ans)
    print(x.run())
except Exception as e:
    print(e)
