salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

# TODO Оформить решение
spend_10 = spend * 1.03 ** months  #затраты ежемесячно, учитывая рост цен со второго месяца
for months in range(0, months):
    need_money += spend * 1.03 ** months - salary
print(round(need_money))
