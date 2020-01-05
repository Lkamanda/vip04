import redis


# 连接池
pool = redis.ConnectionPool(host='127.0.0.1', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)
r.set('book', '西游记')
print(r.get('book'))

# 常规连接
r = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True, db='')
r.set('name', 'shuke')
print(r.get('name'))