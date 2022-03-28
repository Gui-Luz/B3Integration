import json
import urllib3
from core.configurations.configurations import B3_STOCK_INFO_URL


def get_price_description(symbol):
    url = B3_STOCK_INFO_URL + symbol
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    j = json.loads(r.data)
    try:
        price = j['Trad'][0]['scty']['SctyQtn']['curPrc']
        description = j['Trad'][0]['scty']['desc']
        time = j['Msg']['dtTm']
    except:
        price = None
        description = None
        time = None
    return j, description, price, time
