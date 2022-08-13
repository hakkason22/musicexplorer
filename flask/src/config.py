import os


class Config:

    # Flask
    DEBUG = True

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}:{port}/{db}?charset=utf8mb4'.format(**{
        'user': os.getenv('DB_USER_NAME', 'root'),
        'password': os.getenv('DB_USER_PASS', ''),
        'host': os.getenv('DB_HOST_NAME', 'localhost'),
        'port':os.getenv('DB_PORT', 3306),
        'db':os.getenv('DB_NAME','')
    })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


Config = Config