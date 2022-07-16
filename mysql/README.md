# 手動の実行手順
## MySQLコンテナに入る
 docker container exec -it [mysqlのコンテナ名] bash
## SQLファイルを実行
 mysql -u root -p [DB名] < musicexplorer_db.sql
