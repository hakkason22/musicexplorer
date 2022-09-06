from datetime import datetime
from common.libs.Database import db
from sqlalchemy.dialects.mysql import MEDIUMINT as Mediumint

class User(db.Model): 
        __tablename__ = 'users'

        id = db.Column(
                Mediumint(unsigned=True), 
                primary_key=True,
                autoincrement=True)
        spotify_id = db.Column(
                db.String(255), 
                nullable=False)
        token = db.Column(
                db.String(255), 
                nullable=False)
        name = db.Column(
                db.String(255), 
                nullable=False)
        image_url = db.Column(
                db.String(255), 
                nullable=True)
        created_at = db.Column(
                db.DateTime, 
                nullable=False, 
                default=datetime.now)
        updated_at = db.Column(
                db.DateTime, 
                default=datetime.now, 
                nullable=False,
                onupdate=datetime.now)