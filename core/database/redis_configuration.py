import redis
from core.configurations.configurations import HOST, PORT

r_cli = redis.Redis(host=HOST, port=PORT)