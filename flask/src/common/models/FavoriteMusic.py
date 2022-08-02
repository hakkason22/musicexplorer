from datetime import datetime
from common.models.Base import Base

class FavoriteMusic(Base):
    def __init__(self) -> None:
        super().__init__()
        self.id = self.Column(
            self.Mediumint(unsigned=True), 
            primary_key=True,
            autoincrement=True)
        self.music_id = self.Column(
            self.String(255), 
            nullable=False,
            unique=True)
        self.music_name = self.Column(
            self.String(255), 
            nullable=False)
        self.valence = self.Column(
            self.Float(8), 
            nullable=False)
        self.energy = self.Column(
            self.Float(8), 
            nullable=False)
        self.user_id = self.Column(
            self.String(255), 
            nullable=False)
        self.created_at = self.Column(
            self.DateTime, 
            nullable=False, 
            default=datetime.now, 
            onupdate=datetime.now)