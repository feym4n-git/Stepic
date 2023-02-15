from datetime import datetime

class DateError(Exception):

    def __init__(self, message):
        super().__init__(message)

class DateString:

    def __init__(self, date):
        try:
            self.date = datetime.strptime(date, '%d.%m.%Y').strftime('%d.%m.%Y')
        except ValueError:
            raise DateError(f'Invalid date: {date}')

# date_string = input()
date_string = '02.2.12020'

try:
    a = DateString(date_string)
    print(a.date)
except:
    print('Неверный формат даты')
