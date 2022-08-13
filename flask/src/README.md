# musicexplorer_api

# versions

- Python: 3.10.4

# ライブラリの補足

- dotenv
  - 開発環境でのみ使用
- spotipy
  - [公式ドキュメント](https://spotipy.readthedocs.io/en/2.19.0/)
- ~~mysql.connector~~
  - [参考文献](https://self-development.info/mysql-connector-python%E3%81%A7mysql%E3%83%BBmariadb%E3%81%AB%E6%8E%A5%E7%B6%9A%E3%81%99%E3%82%8B/)

# migration の仕方
- ~~srcディレクトリの中で以下のコマンドを実行~~
- flaskコンテナの中で実行
~~~
$ docker container exec [flaskコンテナ名] [コンテナ内で実行するコマンド]
~~~
- 初期化
~~~python
$ flask db init
~~~
- migrate処理
~~~python
#　modelクラスの変更の差分をmigrationファイルとして作成する
$ flask db migrate 
# 未実行のmigrationを実行する
$ flask db upgrade
~~~
- データベースを一つ前のバージョンに戻す
~~~python
$ flask db downgrade
~~~