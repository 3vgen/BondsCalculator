from datetime import date

dictionary = {1: 'january', 2: 'february', 3: 'march',
              4: 'april', 5: 'may', 6: 'june', 7: 'july',
              8: 'august', 9: 'september', 10: 'october', 11: 'november', 12: 'december'}


def minus_days(some_date: date, num_of_days: int) -> date:
    for x in range(0, num_of_days):
        some_date -= date.resolution
    return some_date


def plus_days(some_date: date, num_of_days: int) -> date:
    for x in range(0, num_of_days):
        some_date += date.resolution
    return some_date


def get_month_of_payments(next_coupon: date, coupon_period: int) -> list: #по купонному периоду и дате следующего купона получить выплаты за год
    current_year = date.today().year
    months_of_payments = []

    current_date = next_coupon

    months_of_payments.append(next_coupon.month)

    while True:
        current_date = plus_days(current_date, coupon_period)
        if current_date.year != current_year:
            break
        months_of_payments.append(current_date.month)

    current_date = next_coupon

    while True:
        current_date = minus_days(current_date, coupon_period)
        if current_date.year != current_year:
            break
        months_of_payments.append(current_date.month)

    months_of_payments.sort()
    unique_month = list(set(months_of_payments))
    month_str = [dictionary[i] for i in unique_month]

    return month_str
