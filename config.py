import os


class Config:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{Config.BASE_DIR}/hotdogs.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

