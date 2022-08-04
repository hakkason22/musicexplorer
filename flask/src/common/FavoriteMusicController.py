# coding:utf-8
import mysql.connector
import sys
import os
from common.libs.FavoriteMusicData import FavoriteMusicData

class FavoriteMusicController:
    def __init__(self,db,model,purpose:str,favorite_music_data:dict):
        self.__db = db
        self.__FavoriteMusic = model
        self.__purpose = purpose
        self.__request_data = favorite_music_data

    def run(self):

        if self.__purpose == 'register':
            self.register()
            return {'message':'success!!'}
        elif self.__purpose == 'list':
            return self.get_favorite_musics()
        elif self.__purpose == 'delete':
            self.delete()
            return {'message':'success!!'}
        else:
            return {'message':'false!!'}

    def register(self):
        """お気に入り登録
        """
        # 登録するお気に入り曲オブジェクトを作成
        register_favorite_music = self.__FavoriteMusic(**self.__request_data)

        # お気に入り曲を登録
        self.__db.session.add(register_favorite_music)
        self.__db.session.commit()
        
        return

    def get_favorite_musics(self):
        """お気に入り全取得

        Returns:
            list: [{key1:value,key2:value…},{…},…]
        """
        # ユーザーidからお気に入り曲を全取得
        find_favorite_musics = self.__FavoriteMusic.query.filter_by(user_id = self.__request_data['user_id']).all()

        # お気に入り曲オブジェクトを FavoriteMusicData でラップ（クライアントに渡す値を定義）して、そのリストを戻り値にする
        find_favorite_musics_re = []
        for m in find_favorite_musics:
            find_favorite_musics_re.append(vars(FavoriteMusicData(m)))

        return find_favorite_musics_re

    def delete(self):
        """お気に入り削除
        """
        # レコードのid　からお気に入り曲を削除
        for id in self.__request_data['favorite_music_ids']:
            delete_favorite_music = self.__FavoriteMusic.query.get(int(id))
            self.__db.session.delete(delete_favorite_music)

        self.__db.session.commit()
        
        return
