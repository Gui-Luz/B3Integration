from flask_restful import Resource, reqparse
from core.modules.b3_get_stock_list.main import lambda_handler
from core.configurations.configurations import API_SECRET


parser = reqparse.RequestParser()
parser.add_argument('token', type=str, default=None)


class GetStockList(Resource):

    def __init__(self):
        args = parser.parse_args()
        self.token = args.get('token')

    def post(self):
        if self.token == API_SECRET:
            result = lambda_handler()
            return {'Code': 200, 'Alert': 'Success', 'Data': result}
        else:
            return {'Code': 400, 'Alert': 'Fail'}
