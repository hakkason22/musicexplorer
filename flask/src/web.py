from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from dotenv import load_dotenv
from common.FavoriteMusicController import *
from common.MusicController import *
from exception.MyException import *

app = Flask(__name__)
load_dotenv()  # .envファイルの内容を環境変数として読み込み
CORS(
    app,
    supports_credentials=True
)


@app.route('/')
def Home():
    """トップページを表示

        Returns:
            str: render_template('テンプレート名')でページを返す
    """
    return "tes"


@app.route('/music/list', methods=["POST"])
def send_music_list():
    """アーティスト名からアーティストの曲情報を提供する

    アーティスト名から曲情報
        data(dict): jsonify()に渡す引数
            format: 
            [
                {
                    "music_name":"value",
                    "valence":"value",
                    "arousal":"value",
                    "music_id:"value",
                    "artist_name":"value"
                },
                '''
                '''
            ]

    Returns:
        str: json形式の楽曲リストを返す
    """
    sf1 = MusicController()
    artist_name = str(request.form.get("artist_name"))
    # アーティスト名から楽曲リストを持ってくる
    re = sf1.requestToSpotify(artist_name)
    return jsonify(re)


@app.route('/music/favorite/<purpose>', methods=["POST"])
def favoriteManager(purpose: str):
    """urlパラメータにごとに条件わけして処理
    Args:
        purpose (str): 可変urlパラメータ
    """
    if purpose == 'register':
        db = FavoriteMusicController()
        data = request.form.to_dict()
        re = db.register(data)
        # print(re)
        return jsonify(re)

    elif purpose == 'list':
        db = FavoriteMusicController()
        user_id = request.form.get('user_id')
        re = db.getlist(user_id)
        return jsonify(re)
    elif purpose == 'delete':
        db = FavoriteMusicController()
        id_ = request.form.get('id')
        re = db.delete(id_)
        return jsonify(re)
    else:
        return jsonify(unknownError())


if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(host='0.0.0.0', port=5000, debug=True)
    # app.run(host='0.0.0.0', port=8080, debug=True)
