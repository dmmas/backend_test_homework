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
                amount +=self.amount
        return amount

    def get_week_stats(self):
        amount = 0
        for rec in self.records:
            if dt.datetime.now().date() - dt.timedelta(6) < rec.date <= dt.datetime.now().date():
                amount +=self.amount
        return amount

class Record:
    date_format = '%d.%m.%Y'
    def __init__(self, amount, comment, date = dt.datetime.now().date()) -> None:
        self.date = dt.datetime.strptime(date, date_format).date()
        self.amount = amount
        self.comment = comment




class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        amount = self.get_today_stats()
        if amount < self.limit:
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {self.limit - amount} кКал'
        else:
            return f'Хватит есть!'


class CashCalculator(Calculator):
    USD_RATE = 80
    EURO_RATE = 85
    cur = {'usd': (80, 'USD'), 'eur': (85, 'Euro'), 'rub': (1, 'руб')}
    def get_today_cash_remainder(self, currency):
        amount = self.get_today_stats()
        if amount < self.limit:
            return f'На сегодня осталось {(self.limit-amount)*cur[currency][0]} {cur[currency][1]}'
        elif amount == self.limit:
            return f'Денег нет, держись'     
        else:
            return f'Денег нет, держись: твой долг - {(self.limit - amount)*cur[currency][0]} {cur[currency][1]}'    

