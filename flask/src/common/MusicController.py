# API処理用のモジュール
"""API処理用のモジュール
"""
import itertools
# from difflib import SequenceMatcher
from common.libs.SpotifyAPIService import SpotifyAPIService
from common.artist.Artist import Artist

# SpotifyAPIへのリクエスト処理を別クラスへカプセル化
# このクラスからそのモジュールを使う
# ただ、もしかしたら、やる必要ないかも？
class MusicController:
    """SpotifyAPIとのやりとり用のクラス
    """

    def __init__(self) -> None:
        self.spotify_service = SpotifyAPIService()
        self.artist = None

    def run(self,keyword:str)->None:
        if not self.__search_artist_one(keyword):
            return {"error_message":"No artists hit","result":0}

        tracks = self.__get_tracks_of_artist(self.artist.get_id())
        if tracks == None:
            return {"error_message":"No tracks hit","result":0}

        return tracks

    def __search_artist_one(self,keyword:str)->None:
        self.artist =  Artist(self.spotify_service.search_artist_one(keyword))
        if not self.artist:
            return False
        return True

    
    def __get_tracks_of_artist(self, artist_id: str) -> dict:
        """アーティストIDからすべてのトラックの情報を入手
        """

        if not artist_id:
            return None
        # アーティストIDからアルバム情報を取得
        albums = self.spotify_service.get_albums_of_artist(artist_id,limit=50)
        if not albums:
            return None

        tracks = {}

        #アルバムから楽曲を取得
        tracks.update(self.spotify_service.get_tracks_from_albums(list(albums.keys())))
        #アーティストIDから人気曲を取得
        tracks.update(self.spotify_service.get_top_tracks_of_artist(artist_id)) 

        #ルール1: トラックを名前で一意にする
        tracks_id_name = []
        for track in tracks.values():
            tracks_id_name.append({'id':track['id'],'name':track['name']})
        for i in itertools.combinations(tracks_id_name , 2):
            #i、itertools.combinations(temp_tracknames_list, 2)自体はタプル
            # s = SequenceMatcher(None, a = i[0][0],b = i[1][0])
            if i[0]['name'] == i[1]['name']:
                if i[0]['id'] in tracks:
                    del tracks[i[0]['id']]  

        # トラックの特徴データを取得
        track_features = self.spotify_service.get_track_features_of_tracks(list(tracks.keys()))
        #ルール2: パラメータの被りを解消
        param_dict = {}
        for track_feature in list(track_features.values()):
            if (track_feature['valence'],track_feature['energy']) in param_dict:
                del track_features[param_dict[(track_feature['valence'],track_feature['energy'])]]
            param_dict[(track_feature['valence'],track_feature['energy'])] = track_feature['id']

        #戻り値の整形
        tracks_re = []
        for track_id,track in tracks.items():
            if not (track_id in track_features.keys()):
                continue
            track_re = {
                "artist_name": self.artist.name,
                "music_name": track['name'],
                "valence": track_features[track_id]["valence"],
                "energy": track_features[track_id]["energy"],
                "music_id": track_id
            }
            tracks_re.append(track_re)

        return tracks_re



