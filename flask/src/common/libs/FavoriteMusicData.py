
from common.models.FavoriteMusic import FavoriteMusic

class FavoriteMusicData:
    def __init__(self,favorite_music:FavoriteMusic) -> None:
            self.favorite_music_id = favorite_music.id
            self.music_name = favorite_music.music_id
            self.music_name = favorite_music.music_name
            self.valence = favorite_music.valence
            self.energy = favorite_music.energy