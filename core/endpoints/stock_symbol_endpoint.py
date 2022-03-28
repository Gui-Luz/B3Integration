from flask_restful import Resource, reqparse
from core.modules.stock_symbol.stock_symbol import GetStockInfoRedisConnector
from core.configurations.configurations import API_SECRET


parser = reqparse.RequestParser()
parser.add_argument('token', type=str, default=None)
parser.add_argument('stock_symbol', type=str, default=None)


class StockSymbol(Resource):

    def __init__(self):
        args = parser.parse_args()
        self.token = args.get('token')
        self.stock_symbol = args.get('stock_symbol')

    def post(self):
        if self.token == API_SECRET:
            connector = GetStockInfoRedisConnector(self.stock_symbol)
            time = connector.get_time()
            price = connector.get_price()
            description = connector.get_description()
            return {'Code': 200, 'Alert': 'Success', 'Stock data': {'Stock symbol': self.stock_symbol,
                                                              'Description': description, 'Time': time, 'Price': price}}
        else:
            return {'Code': 400, 'Alert': 'Fail'}
