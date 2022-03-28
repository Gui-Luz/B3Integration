from datetime import datetime
from core.configurations import HOST, PORT
from core.modules.b3_get_stock_list.get_stock_list import get_symbols
from core.modules.rrcq.rrcq import RedisReadyCircularQueue


def lambda_handler():
    start = datetime.now()
    available_stocks = get_symbols()
    rrcq = RedisReadyCircularQueue(HOST, PORT)
    rrcq.set_new_queue(available_stocks, available_stocks[0])

    delta = str(datetime.now() - start)


    return {
        'statusCode': 200,
        'Stocks Available': len(available_stocks),
        'Delta': delta,
        'Stock List': available_stocks
    }