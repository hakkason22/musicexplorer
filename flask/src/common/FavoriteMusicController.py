# coding:utf-8
from common.libs.FavoriteMusicData import FavoriteMusicData

class FavoriteMusicController:
    """お気に入り楽曲を管理するコントローラ
    """
    def __init__(self,db,model,purpose:str,favorite_music_data:dict):
        self.__db = db
        self.__FavoriteMusic = model
        self.__purpose = purpose
        self.__request_data = favorite_music_data

    def run(self):
        """状態によって処理を振り分ける

        Returns:
            dict: { error_message:(str), result:(0or1)[, data:(list)] }
        """
        if self.__purpose == 'register':
            return self.register()
        elif self.__purpose == 'list':
            return self.get_favorite_musics()
        elif self.__purpose == 'delete':
            return self.delete()
        else:
            return {"error_message":"Invalid request","result":0}

    def register(self):
        """お気に入り登録

        Returns:
            dict: { error_message:(str), result:(0or1) }
        """
        try:
            # 登録するお気に入り曲オブジェクトを作成
            register_favorite_music = self.__FavoriteMusic(**self.__request_data)

            # お気に入り曲を登録
            self.__db.session.add(register_favorite_music)
            self.__db.session.commit()
        except Exception as e:
            return {"error_message": str(e), "result":0}
        
        return {"error_message":"", "result":1}

    def get_favorite_musics(self):
        """お気に入り全取得

        Returns:
            dict: { error_message:(str), result:(0or1), data:(list) }
        """
        try:
            # ユーザーidからお気に入り曲を全取得
            find_favorite_musics = self.__FavoriteMusic.query.filter_by(user_id = self.__request_data['user_id']).all()

            # お気に入り曲オブジェクトを FavoriteMusicData でラップ（クライアントに渡す値を定義）して、そのリストを戻り値にする
            find_favorite_musics_re = []
            for m in find_favorite_musics:
                find_favorite_musics_re.append(vars(FavoriteMusicData(m)))
        except Exception as e:
            return {"error_message": str(e),"result":0}

        re = {"error_message":"","result":1}
        re['data'] = find_favorite_musics_re
        return re

    def delete(self):
        """お気に入り削除

        Returns:
            dict: { error_message:(str), result:(0or1) }
        """
        # レコードのid　からお気に入り曲を削除
        try:
            for id in self.__request_data['favorite_music_ids'].split(','):
                delete_favorite_music = self.__FavoriteMusic.query.get(int(id))
                self.__db.session.delete(delete_favorite_music)
            self.__db.session.commit()
        except Exception as e:
            return {"error_message": str(e),"result":0}

        return {"error_message":"","result":1}
