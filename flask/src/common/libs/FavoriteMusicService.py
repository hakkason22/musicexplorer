from common.models.FavoriteMusic import FavoriteMusic

class FavoriteMusicService:
    def __init__(self) -> None:
        pass

    def CheckExist(user_id:str,music_id:str):
        """ユーザーのお気に入り曲の重複確認

        Args:
            user_id (str): ユーザーID
            music_id (str): 楽曲のID

        Returns:
            bool: 存在していたらTrue、存在していなかったらFalse
        """
        result = FavoriteMusic.query.filter_by(user_id = user_id,music_id = music_id).first()
        if not result:
            return False
        return True