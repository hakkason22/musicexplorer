from common.models.FavoriteMusic import FavoriteMusic 
from common.artist.RecommendArtistData import RecommendArtistData
from common.artist.Artist import Artist
from common.libs.SpotifyAPIService import SpotifyAPIService

import random
import datetime

class RecommendArtistController:
    """おすすめアーティストに関するコントローラ
    """
    def __init__(self) -> None:
        self.spotify = SpotifyAPIService()

    def get_recommend_artists(self,user_id):
        # user_id が空だったら、有名アーティストを返す
        if not user_id:
            return self.get_popular_artists()

        try:
            # ユーザーidからお気に入り曲を全取得
            # 全取得しないようにしたい
            favorite_musics = FavoriteMusic.query.filter_by(user_id = user_id).all()
        except Exception as e:
            print(str(e))
            return {"error_message": str(e),"result":0}

        # お気に入り曲が空だったら、有名アーティストを返す
        if not favorite_musics:
            return self.get_popular_artists()

        # お気に入り曲からランダムな一つを取得
        rand_index = random.randint(0,len(favorite_musics)-1)
        favorite_music = favorite_musics[rand_index]

        # 最初からデータベースにartist情報も保存すべきか？
        # music_id から　artist_id を取得
        artist_id = self.spotify.get_track(favorite_music.music_id)['artists'][0]['id']

        # ランダムに取得したお気に入り楽曲のアーティストから、関連するアーティストを取得する
        recommend_artists = self.spotify.get_artist_related_artists(artist_id)

        recommend_artists_re = []
        for artist in recommend_artists['artists']:
            # Artist オブジェクトを生成して、RecommendArtistsData に　値を移し替える、vars() でフィールドを dict 型で取得
            recommend_artists_re.append(vars(RecommendArtistData(Artist(artist))))
        return recommend_artists_re

    def get_popular_artists(self):
        """人気アーティストを返す
        """
        currentDateTime = datetime.datetime.now()
        date = currentDateTime.date()
        year = date.strftime("%Y")

        # 現在の年で検索
        # マーケットはとりあえずJPにした
        recommend_artists = self.spotify.search(q=f"year:{year}",type='artist',limit=20)

        recommend_artists_re = []
        for artist in recommend_artists['artists']['items']:
            # Artist オブジェクトを生成して、RecommendArtistsData に　値を移し替える、vars() でフィールドを dict 型で取得
            # 人気度が50未満のアーティストはスルー
            if artist['popularity'] < 50:
                continue
            recommend_artists_re.append(vars(RecommendArtistData(Artist(artist['id'],artist['name'],artist['images']))))
        return recommend_artists_re



        