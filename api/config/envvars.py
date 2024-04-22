import os

DJANGO_DEBUG = os.environ.get("DJANGO_DEBUG")
DJANGO_SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")
DB_ENGINE = os.environ.get("DB_ENGINE")
DB_DATABASE = os.environ.get("DB_DATABASE")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
