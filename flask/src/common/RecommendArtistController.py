from common.models.FavoriteMusic import FavoriteMusic 
from common.artist.RecommendArtistData import RecommendArtistData
from common.artist.Artist import Artist

from sqlalchemy.sql import func
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
import random

class RecommendArtistController:
    """おすすめアーティストに関するコントローラ
    """
    def __init__(self) -> None:
        # 初期化
        self.spotify = spotipy.Spotify(
            client_credentials_manager=SpotifyClientCredentials(client_id = os.environ['SPOTIFY_CLIENT_ID'], client_secret = os.environ['SPOTIFY_SECRET_ID']),
            language='ja')

    def get_recommend_artists(self,user_id):
        try:
            # ユーザーidからお気に入り曲を全取得
            favorite_musics = FavoriteMusic.query.filter_by(user_id = user_id).all()
        except Exception as e:
            print(str(e))
            return {"error_message": str(e),"result":0}

        # お気に入り曲からランダムな一つを取得
        rand_index = random.randint(0,len(favorite_musics)-1)
        favorite_music = favorite_musics[rand_index]

        # 最初からデータベースにartist情報も保存すべきか？
        # music_id から　artist_id を取得
        artist_id = self.spotify.track(favorite_music.music_id)['artists'][0]['id']

        # ランダムに取得したお気に入り楽曲のアーティストから、関連するアーティストを取得する
        recommend_artists = self.spotify.artist_related_artists(artist_id)

        recommend_artists_re = []
        for artist in recommend_artists['artists']:
            # Artist オブジェクトを生成して、RecommendArtistsData に　値を移し替える、vars() でフィールドを dict 型で取得
            recommend_artists_re.append(vars(RecommendArtistData(Artist(artist['id'],artist['name'],artist['images']))))
        return recommend_artists_re



        