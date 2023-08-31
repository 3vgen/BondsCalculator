import requests
import json
from datetime import date
from calculate_coupon_frequency import get_month_of_payments


class BondModel:
    def __init__(self, sec_id: str):
        url = f"https://iss.moex.com/iss/engines/stock/markets/bonds/securities/{sec_id}.json?iss.meta=off&iss.only=securities"
        response = requests.get(url)
        data = response.json()

        self.sec_id = sec_id
        self.name = data['securities']['data'][0][2]
        if data['securities']['data'][0][8] is not None:
            self.current_price = 10 * data['securities']['data'][0][8] #может быть более интелектуальным и считать при разных номиналах
        else:
            self.current_price = 10 * data['securities']['data'][1][8]
        self.coupon_value = data['securities']['data'][0][5]
        self.__next_coupon = date.fromisoformat(data['securities']['data'][0][6])
        self.__coupon_period = data['securities']['data'][0][15]
        self.coupon_frequency = len(get_month_of_payments(self.__next_coupon, self.__coupon_period))

    def get_coupon_frequency(self):

        return get_month_of_payments(self.__next_coupon, self.__coupon_period)

    def show_full_info(self):
        print(self.sec_id, self.name, self.current_price, self.coupon_value)
