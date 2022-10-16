money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

# TODO Оформить решение
delta = 0 # разница между расходами и зарплатой в начале первого месяца
while True:
    delta += spend * 1.05 ** month - salary # расходы за каждый месяц с учетом роста цен
    if money_capital - delta >= 0: # остаток на следующий месяц
        money_capital -= delta
        month += 1
    else:
       break
print(month)
