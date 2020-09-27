import sqlite3

# 接続先となるDBの名前。'/home/user/database.db'といった表現方法も可能。
dbname = 'database.db'

# コネクタ作成。dbnameの名前を持つDBへ接続する。
conn = sqlite3.connect(dbname)
cur = conn.cursor()

# ここから好きなだけクエリを打つ
cur.execute('create table blog(id integer,title String ,name text);')

cur.execute("insert into blog values(1, 'a', 'eri')")

# 処理をコミット
conn.commit()

# 接続を切断
conn.close()
