import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from concurrent.futures import ThreadPoolExecutor

import os
import time

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

    def get_albums_of_artist(self,artist_id:str,limit:int=20):
        # アーティストIDからアルバム情報を取得
        albums = self.spotify.artist_albums(artist_id, limit=limit, album_type='album,single',offset=0)['items']

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
                if not future.result()['items']:
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
        with ThreadPoolExecutor(max_workers=len(track_ids)//100+1) as executor:
            futures = []
            while i < len(track_ids)//100*100:
                pre_i = i
                i += max
                future = executor.submit(self.spotify.audio_features,track_ids[pre_i:i])
                futures.append(future)
            future = executor.submit(self.spotify.audio_features,track_ids[i:])
            futures.append(future)
            for future in futures:
                track_features.extend(future.result())
            
        track_features_dict = {}
        for track_feature in track_features:
            track_features_dict[track_feature['id']] = track_feature
        return track_features_dict

    def search(self,q:str,type:str,limit:int=20):
        data = self.spotify.search(q=q,limit=limit,type=type,market='JP')
        return data
    
    def get_artist_related_artists(self,artist_id:str):
        artists = self.spotify.artist_related_artists(artist_id)
        return artists

    def get_track(self,track_id:str):
        track = self.spotify.track(track_id)
        return track