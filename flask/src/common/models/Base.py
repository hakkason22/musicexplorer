from common.libs.Database import db
from sqlalchemy.dialects.mysql import MEDIUMINT as Mediumint

class FavoriteMusic(db.Model):

    def __init__(self) -> None:
        super().__init__()
        self.__table_args__=({"mysql_charset": "utf8mb4"})
        self.__tablename__ = 'favorite_musics'
        self.Column = db.Column
        self.Mediumint = Mediumint
        self.String = db.String
        self.Float = db.Float
        self.DataTime = db.DataTime
        self.db = db