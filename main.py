from flask import Flask
from flask_restful import Api
from core.configurations.configurations import API_SECRET
from core.endpoints.b3_get_stock_list_endpoint import GetStockList
from core.endpoints.b3_get_current_stock_data_endpoint import GetStockData
from core.endpoints.stock_symbol_endpoint import StockSymbol
from core.configurations.configurations import GET_STOCK_LIST_ENDPOINT
from core.configurations.configurations import GET_STOCK_DATA_ENDPOINT
from core.configurations.configurations import STOCK_SYMBOL_ENDPOINT


app = Flask(__name__)
app.config['SECRET-KEY'] = API_SECRET
api_server = Api(app)

api_server.add_resource(GetStockList, GET_STOCK_LIST_ENDPOINT)
api_server.add_resource(GetStockData, GET_STOCK_DATA_ENDPOINT)
api_server.add_resource(StockSymbol, STOCK_SYMBOL_ENDPOINT)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
