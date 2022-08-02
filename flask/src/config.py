import os


class Config:

    # Flask
    DEBUG = True

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/musicexplorer?charset=utf8'.format(**{
        'user': os.getenv('DB_USER_NAME', 'root'),
        'password': os.getenv('DB_USER_PASS', ''),
        'host': 'localhost',
        # 'host': os.getenv('DB_HOST_NAME', 'localhost'),
    })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


Config = Config