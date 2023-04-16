import datetime as dt

class Calculator:
    def __init__(self, limit):
        self.records = []
        self.limit = limit
        
    def add_record(self, rec):
        self.records.append(rec)


    def get_today_stats(self):
        amount = 0
        for rec in self.records:
            if rec.date == dt.datetime.now().date():
                amount +=rec.amount
        return amount

    def get_week_stats(self):
        amount = 0
        for rec in self.records:
            if dt.datetime.now().date() - dt.timedelta(6) < rec.date <= dt.datetime.now().date():
                amount +=rec.amount
        return amount

class Record:
    def __init__(self, amount, comment, date = ''):
        if date == '':
            self.date = dt.datetime.now().date()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
        self.amount = amount
        self.comment = comment




class CaloriesCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)

    def get_calories_remained(self):
        amount = self.get_today_stats()
        if amount < self.limit:
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {self.limit - amount} кКал'
        else:
            return f'Хватит есть!'


class CashCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)

    USD_RATE = 80
    EURO_RATE = 85
    RUB_RATE = 1

    cur = {'usd': (USD_RATE, 'USD'), 
           'eur': (EURO_RATE, 'Euro'), 
           'rub': (RUB_RATE, 'руб')}
    
    def get_today_cash_remained(self, currency):
        amount = self.get_today_stats()
        if amount < self.limit:
            return f'На сегодня осталось {(self.limit-amount)*self.cur[currency][0]} {self.cur[currency][1]}'
        elif amount == self.limit:
            return f'Денег нет, держись'     
        else:
            return f'Денег нет, держись: твой долг - {(self.limit - amount)*self.cur[currency][0]} {self.cur[currency][1]}'    



if __name__ == '__main__':
    
    # создадим калькулятор денег с дневным лимитом 1000
    cash_calculator = CashCalculator(1000)
            
    # дата в параметрах не указана, 
    # так что по умолчанию к записи должна автоматически добавиться сегодняшняя дата
    cash_calculator.add_record(Record(amount=145, comment="кофе")) 
    # и к этой записи тоже дата должна добавиться автоматически
    cash_calculator.add_record(Record(amount=300, comment="Серёге за обед"))
    # а тут пользователь указал дату, сохраняем её
    cash_calculator.add_record(Record(amount=3000, comment="бар в Танин др", date="08.11.2019"))
                    
    print(cash_calculator.get_today_cash_remained("rub"))
    # должно напечататься
    # На сегодня осталось 555 руб
