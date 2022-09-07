import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from concurrent.futures import ThreadPoolExecutor

import os

class SpotifyAPIService:
    
    def __init__(self) -> None:
        """spotipyの初期化
        """
        self.spotify = spotipy.Spotify(
            client_credentials_manager=SpotifyClientCredentials(client_id = os.environ['SPOTIFY_CLIENT_ID'], client_secret = os.environ['SPOTIFY_SECRET_ID']),
            language='ja')

    def search_artist_one(self,keyword:str = None)->str:
        """キーワードからアーティストを検索して情報を取得する

        Args:
            artist_name (str): アーティストの名前

        Returns:
            str: アーティストID
        """
        results = self.spotify.search(
            q=keyword, type="artist", market="JP", limit=1)    
       
        if not results["artists"]["items"]:
            return None
        #itemsの配列のうち一番最初に出てくるのが一番検索に近いアーティストとみなす
        artist = results["artists"]["items"][0]
        return artist

    def get_albums_of_artist(self,artist_id:str,limit:int=50,max_workers:int=10):
        # アーティストIDからアルバム情報を取得
        albums = []
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = []
            for i in range(max_workers):
                future = executor.submit(self.spotify.artist_albums, artist_id, limit=limit, album_type='album,single')
                futures.append(future)
            for future in futures: 
                if not future.result():
                    break   
                albums.extend(future.result()['items'])
                
        albums_dict = {}
        for album in albums:
            albums_dict[album['id']] = album
        return albums_dict
    
    def get_top_tracks_of_artist(self,artist_id:str):
        top_tracks = self.spotify.artist_top_tracks(artist_id,country = "JP")["tracks"]
        top_tracks_dict = {}
        for top_track in top_tracks:
            top_tracks_dict[top_track['id']] = top_track
        return top_tracks_dict

    def get_tracks_from_albums(self,album_ids:list,limit:int=50):
        tracks = []
        with ThreadPoolExecutor(max_workers=len(album_ids)) as executor:
            futures = []
            for album_id in album_ids:
                future = executor.submit(self.spotify.album_tracks,album_id,limit=limit)
                futures.append(future)
            for future in futures: 
                if not future.result():
                    continue
                tracks.extend(future.result()['items'])
        tracks_dict ={}
        for track in tracks:
            tracks_dict[track['id']] = track
        return tracks_dict

    def get_track_features_of_tracks(self,track_ids:list):
        track_features = []
        max = 100
        i = 0
        while i < len(track_ids)//100*100:
            pre_i = i
            i += max
            track_features.extend(self.spotify.audio_features(track_ids[pre_i:i]))
        track_features.extend(self.spotify.audio_features(track_ids[i:]))

        track_features_dict = {}
        for track_feature in track_features:
            track_features_dict[track_feature['id']] = track_feature
        return track_features_dict