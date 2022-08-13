from common.models.FavoriteMusic import FavoriteMusic

class FavoriteMusicService:
    def __init__(self) -> None:
        pass

    def CheckExist(user_id:str,music_id:str):
        result = FavoriteMusic.query.filter_by(user_id = user_id,music_id = music_id).first()
        if not result:
            return False
        return True