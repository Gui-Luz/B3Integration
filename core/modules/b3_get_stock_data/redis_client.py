from core.database.redis_configuration import r_cli


def set_stock_price_and_description(stock, description, price, time):
    r_cli.set(f'price:{stock}', str(description) + ':' + str(price) + ':' + str(time))