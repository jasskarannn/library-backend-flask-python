from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
from flask_migrate import Migrate
from flask_caching import Cache

db = SQLAlchemy()
redis_client = FlaskRedis(config_prefix="REDIS_HOST_URL")
migrate = Migrate()
cache = Cache()

