# coding:utf-8
import mysql.connector
import sys
import os

# ここは別のライブラリを使う
# またモデルを介してデータベースにアクセスする
class FavoriteMusicController:
    def __init__(self):
        # データベースとの接続を開始
        try:
            self.conn = mysql.connector.connect(
                host=os.environ.get("DB_HOST_NAME"),
                port=os.environ.get("DB_PORT"),
                user=os.environ.get("DB_USER_NAME"),
                password=os.environ.get("DB_USER_PASS"),
                database=os.environ.get("DB_NAME"))
            self.conn.ping(reconnect=True)
            self.cur = self.conn.cursor(dictionary=True)
        except Exception as e:
            print('[DB Connection Error]', e)
            sys.exit(1)
    
    def index():
        pass

    def register(self, data: dict):
        try:
            # すでに同様のレコードがあるかのチェック
            self.cur.execute(
                "SELECT * FROM favorite_musics WHERE user_id=%s AND music_id=%s", (data['user_id'], data['music_id']))
            if self.cur.fetchone():
                duplication = {"status_code": 200,
                               "message": "Elements already registered"}
                return duplication

            # insert処理
            sql = (
                "INSERT INTO favorite_musics (music_id, music_name, valence, energy, user_id) "
                "VALUES (%s, %s, %s, %s, %s)"
            )
            t_data = (data['music_id'], data['music_name'],
                      data['valence'], data['energy'], data['user_id'])
            self.cur.execute(sql, t_data)
            self.conn.commit()

            return {"status_code": 200,
                    "message": "Registration has been successfully completed"}
        except Exception as e:
            return {"status_code": 500,
                    "message": e}

    def getlist(self, user_id: str):
        try:
            self.cur.execute(
                "SELECT * FROM favorite_musics WHERE user_id=%s", (user_id,))
            t_data = self.cur.fetchall()
            r_data = []
            for d in t_data:
                r_data.append({
                    "music_name": d["music_name"],
                    "valence": d["valence"],
                    "energy":  d["energy"],
                    "music_id": d["music_id"],
                    "id": d["id"]
                })
            return r_data
        except Exception as e:
            return {"status_code": 500,
                    "message": e}

    def delete(self, id_: str):
        try:
            sql = ("DELETE FROM favorite_musics WHERE id = %s")
            self.cur.execute(sql, (id_,))
            self.conn.commit()
            return {"status_code": 200,
                    "message": "Registration has been successfully completed"}
        except Exception as e:
            return {"status_code": 500,
                    "message": e}

    def __del__(self):
        # データベースとの接続を切断
        self.cur.close()
        self.conn.close()
