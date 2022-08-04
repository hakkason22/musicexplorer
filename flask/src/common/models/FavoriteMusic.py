from datetime import datetime
from common.libs.Database import db
from sqlalchemy.dialects.mysql import MEDIUMINT as Mediumint

class FavoriteMusic(db.Model): 
        __table_args__=({"mysql_charset": "utf8mb4"})
        __tablename__ = 'favorite_musics'

        id = db.Column(
                Mediumint(unsigned=True), 
                primary_key=True,
                autoincrement=True)
        music_id = db.Column(
                db.String(255), 
                nullable=False,
                unique=True)
        music_name = db.Column(
                db.String(255), 
                nullable=False)
        valence = db.Column(
                db.Float(8), 
                nullable=False)
        energy = db.Column(
                db.Float(8), 
                nullable=False)
        user_id = db.Column(
                db.String(255), 
                nullable=False)
        created_at = db.Column(
                db.DateTime, 
                nullable=False, 
                default=datetime.now)
        updated_at = db.Column(
                db.DateTime, 
                default=datetime.now, 
                nullable=False,
                onupdate=datetime.now)