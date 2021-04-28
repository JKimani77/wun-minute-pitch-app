import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ###

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql://jyqlpahkwjrgjv:ae32f1746e4daf0960b1b747a687fae63e4d86be8194ab06c5b18dab6fcdc47d@ec2-18-214-140-149.compute-1.amazonaws.com:5432/d1e78f8dhtcjna?sslmode=require'
    


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:Ivonne1236987@localhost:5432/peach'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}