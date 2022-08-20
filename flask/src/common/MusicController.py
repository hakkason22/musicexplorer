# API処理用のモジュール
"""API処理用のモジュール
"""

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import itertools
from difflib import SequenceMatcher
import os

# SpotifyAPIへのリクエスト処理を別クラスへカプセル化
# このクラスからそのモジュールを使う
# ただ、もしかしたら、やる必要ないかも？
class MusicController:
    """SpotifyAPIとのやりとり用のクラス
    """

    def __init__(self) -> None:
        # 初期化
        self.spotify = spotipy.Spotify(
            client_credentials_manager=SpotifyClientCredentials(client_id = os.environ['SPOTIFY_CLIENT_ID'], client_secret = os.environ['SPOTIFY_SECRET_ID']),
            language='ja')

    def requestToSpotify(self, artist_name: str = None) -> dict:
        """与えられた引数によって条件分岐して

        Args:
            artist_name (str): アーティストの名前

        Returns:
            dict: アーティストの楽曲情報リスト
                format: 
                [
                    {
                        "music_name":"value",
                        "valence":"value",
                        "energy":"value",
                        "music_url:"value"
                    },
                    '''
                    '''
                ]
        """
        if not artist_name:
            return self.ex.incorrectParam()
        elif "artist_name" in locals():
            artist_id = self.__getIdByArtist(artist_name)
            if artist_id == None:
                return { "message": "No artists hit" }
            data = self.__getAllTracksByArtistId(artist_id)
            if data == None:
                return { "message": "No Tracks hit" }
            return data
        else:
            return { "message": "Incorrect parameter" }

    def __getIdByArtist(self, artist_name: str) -> str:
        """アーティスト名からアーティストIDを入手する

        Args:
            artist_name (str): アーティストの名前

        Returns:
            str: アーティストID
        """
        results = self.spotify.search(
            q=artist_name, type="artist", market="JP", limit=1)    
        # resultはsptifyにアーティストについて教えてで検索かけて出た検索結果
        
        items = results["artists"]["items"]
        # アーティストの欄を見ると、アーティスト名のリストがバーッてあっていろんな情報が入ってる
        #キーがitemsの情報は検索でヒットしたアーティスト名をとってきて、itemsという変数に配列を格納
        if not items:
            return None
        #itemsの配列のうち一番最初に出てくるのが一番検索に近いアーティスト
        artist = items[0]
        artist_id = artist["id"]
        self.artist_name = artist["name"]
        return artist_id

    
    



    def __getAllTracksByArtistId(self, artist_id: str) -> dict:
        """アーティストIDからすべてのトラックの情報を入手

        Args:
            artist_Id (str): アーティストのID

        Returns:
            list: トラック情報のリスト
        """
        # アーティストIDからアルバム情報を取得
        results = self.spotify.artist_albums(
            artist_id, limit=20, album_type='album')
        album_records = results['items']
        if not album_records:
            return None

        a_trackId_list = []
        temp_tracknames_list = [] 
        t_track_info = {}
        tracks_total = 0
        t_name_and_Id_set = {} 

        #アーティストIDからアーティストの人気曲を取得する
        top_trackslist = self.spotify.artist_top_tracks(artist_id,country = "JP")
        for track in top_trackslist["tracks"]:
            print(track["id"])
            a_trackId_list.append(track['id'])
            temp_tracknames_list.append([track['name'],track['id']]) 
            t_track_info[track['id']] = {"name": track['name']}
            t_name_and_Id_set[track['name']] = track['id'] 
            

        # アルバムIDからトラック情報を取得
        for a_data in album_records:
            album_id = a_data['id']
            tracks_data = self.spotify.album_tracks(album_id)
            tracks_total += len(tracks_data['items'])
            if tracks_total > 100:
                break
            # トラック情報から名前とIDを取得

            for t_data in tracks_data['items']:
                a_trackId_list.append(t_data["id"])
                temp_tracknames_list.append([t_data["name"], t_data["id"]]) 
                t_track_info[t_data["id"]] = {"name": t_data["name"]}
                t_name_and_Id_set[t_data["name"]] = t_data["id"] 
            
            


        #曲の重複対策
        compare_namelist = []
        exclude_namelist = []
        modified_tracknames_list = []

        
        # #曲名からLiveやinstrumentなどを抜く
        # for i in range(len(temp_tracknames_list)):
        #     if ("live" in temp_tracknames_list[i].lower()):
        #         temp_lowercase = temp_tracknames_list[i].lower()
        #         modified_tracknames_list.append(temp_lowercase.replace("live",""))
        #     elif ("instrument" in temp_tracknames_list[i].lower()):
        #         temp_lowercase = temp_tracknames_list[i].lower()
        #         modified_tracknames_list.append(temp_lowercase.replace("instrument",""))
        #     else:
        #         lowercase = temp_tracknames_list[i].lower()
        #         modified_tracknames_list.append(lowercase)
        #print(temp_tracknames_list)
        

        #曲名の類似度の高い曲の組み合わせを抽出
        for i in itertools.combinations(temp_tracknames_list , 2):
            #i、itertools.combinations(temp_tracknames_list, 2)自体はタプル

            s = SequenceMatcher(None, a = i[0][0],b = i[1][0])
            
            if s.ratio() >= 1.00: 



                #設定値は0.7（ここで調整）
                compare_namelist.append(i)
                #print('類似度：{0}%,{1}'.format(round(s.ratio()*100,1), i))    
        
        
        #曲名の類似性の高い組み合わせのうち、消去する曲名を決定  
        for i in range(len(compare_namelist)):
            if len(compare_namelist[i][0][0]) >= len(compare_namelist[i][1][0]):
                exclude_namelist.append(compare_namelist[i][0])
            else:
                exclude_namelist.append(compare_namelist[i][1])
        for i in exclude_namelist:
            if i == "長く短い祭":
                print(i)

        #消去する曲名から消去する曲のIDを取得し、曲のIDリストから消去
        #曲のIDリストを更新
        for i in exclude_namelist:
            try:  
                a_trackId_list.remove(i[1])
            except:
                continue
            
               
        
        a_track_set = set(a_trackId_list)



        
        

        track_list = []
        # トラックIDから各種パラメータを取得
        track_features = self.spotify.audio_features(list(a_track_set))
        for track_feature in track_features:
            # 戻り値の整形
            id = track_feature["id"]
            record = {
                "artist_name": self.artist_name,
                "music_name": t_track_info[id]["name"],
                "valence": track_feature["valence"],
                "energy": track_feature["energy"],
                "music_id": id
            }
            track_list.append(record)

        #パラメータの被りを解消
        track_list = self.__delete_same_param_music(track_list)

        return track_list

    def __delete_same_param_music(self,track_list:list):
        """valenceとenergyの組み合わせが同じ曲を片方だけ残すようにする

        Args:
            track_list (list): 返却する楽曲のリスト

        Returns:
            list: ラップした楽曲のリスト、ディープコピー
        """
        filtered_list = []
        param_dict = {}
        for t in track_list:
            if (t['valence'],t['energy']) in param_dict:
                continue
            param_dict[(t['valence'],t['energy'])] = t['music_id']
            filtered_list.append(t)
        return filtered_list




