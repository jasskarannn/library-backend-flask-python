import os
from dotenv import load_dotenv
from pathlib import Path


environment = os.getenv("ENVIRONMENT", "development")
config_path = os.path.dirname(os.path.abspath(__file__))

if environment == "docker":
    load_dotenv(Path(config_path + "/.env-docker"))
elif environment == "integration":
    load_dotenv(Path(config_path + "/.env-integration"))
elif environment == "production":
    load_dotenv(Path(config_path + "/.env-production"))
else:
    load_dotenv(Path(config_path + "/.env-development"))

DEBUG = os.getenv("DEBUG")
TESTING = os.getenv("TESTING")

# Database - phase 2 implementation
SQLALCHEMY_DATABASE_URI_TESTING = "sqlite:///data.db"
SQLALCHEMY_DATABASE_URI = os.getenv("postgresql://{0}:{1}@{2}:5432/{3}".format(
    os.getenv("POSTGRES_USER"),
    os.getenv("POSTGRES_PASSWORD"),
    os.getenv("POSTGRES_SERVER"),
    os.getenv("POSTGRES_DB"),
), SQLALCHEMY_DATABASE_URI_TESTING)


POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_SERVER = os.getenv("POSTGRES_SERVER")

# Redis Cache - phase 3 implementation
REDIS_HOST_URL = os.getenv("REDIS_HOST_URL")
CACHE_TYPE = os.getenv("CACHE_TYPE")

