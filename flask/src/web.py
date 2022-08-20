from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from dotenv import load_dotenv
from common.FavoriteMusicController import FavoriteMusicController
from common.MusicController import MusicController
from common.RecommendArtistController import RecommendArtistController

from common.libs.Database import init_db,db
from common.models.FavoriteMusic import FavoriteMusic

app = Flask(__name__)
load_dotenv()  # .envファイルの内容を環境変数として読み込み
CORS(
    app,
    supports_credentials=True
)
app.config.from_object('config.Config')
init_db(app)

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
    music_controller = MusicController()
    artist_name = str(request.form.get("artist_name"))
    # アーティスト名から楽曲リストを持ってくる
    re = music_controller.requestToSpotify(artist_name)
    return jsonify(re)


@app.route('/music/favorite/<purpose>', methods=["POST"])
def favorite_manager(purpose: str):
    """urlパラメータにごとに条件わけして処理
    Args:
        purpose (str): 可変urlパラメータ
    """
    favorite_controller = FavoriteMusicController(db,FavoriteMusic,purpose,request.form.to_dict())
    result = favorite_controller.run()
    return jsonify(result)

@app.route('/artist/recommend',methods=["GET"])
def recommend_artists():
    """おすすめアーティストを返す
    """
    recommend_controller = RecommendArtistController()
    result = recommend_controller.get_recommend_artists(request.args.get('user_id'))
    return jsonify(result)


if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(host='0.0.0.0', port=5000, debug=True)
    # app.run(host='0.0.0.0', port=8080, debug=True)
