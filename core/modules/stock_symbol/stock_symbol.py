from core.database.redis_configuration import r_cli
from datetime import datetime


class GetStockInfoRedisConnector:
    def __init__(self, stock):
        self._stock = stock
        self._info = self._get_stock_info()
        self._split_info()

    def _get_stock_info(self):
        info = r_cli.get(f'price:{self._stock}')
        return info.decode()

    def _split_info(self):
        if self._info:
            info_list = self._info.split(':')
            description = info_list.pop(0)
            price = info_list.pop(0)
            time = info_list
            self._description = description
            self._price = float(price)
            self.unformated_time = time
        else:
            self._description = None
            self._price = None
            self.unformated_time = None

    def get_price(self):
        return self._price

    def get_description(self):
        return self._description

    def get_time(self):
        time = ''
        time_info = self.unformated_time
        while time_info:
            time += ':' + time_info.pop(0)
        return datetime.strptime(time[1:], '%Y-%m-%d %H:%M:%S').strftime('%d/%m/%Y %H:%M:%S')