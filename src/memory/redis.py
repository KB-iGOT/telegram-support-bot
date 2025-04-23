import redis
from core.config import settings

# Connect to Redis
redis_client = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_INDEX)  # Adjust host and port if needed

# Define a function to store and retrieve data in Redis
def store_data(key, value):
    redis_client.set(key, value)

def retrieve_data(key):
    data_from_redis = redis_client.get(key)
    return data_from_redis.decode('utf-8') if data_from_redis is not None else None

