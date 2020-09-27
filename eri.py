import requests
from bs4 import BeautifulSoup
import re
import sqlite3

# 接続先となるDBの名前。'/home/user/database.db'といった表現方法も可能。
dbname = 'database.db'

# コネクタ作成。dbnameの名前を持つDBへ接続する。
conn = sqlite3.connect(dbname, isolation_level=None)
cur = conn.cursor()

# ここから好きなだけクエリを打つ
# cur.execute('create table students(id integer,title String ,name text);')

# 処理をコミット
conn.commit()

urlName = "https://erihitomi.com/"
url = requests.get(urlName)
soup = BeautifulSoup(url.content, "html.parser")
# ブログタイトルを取得
title = soup.select_one("h2")

# ブログurlを取得
cardlink = soup.select_one("[class='cardtype__article-info']")
linktag = cardlink.find_previous("a")

# dbからデータを取得
table = cur.execute('select * from blog where name =? ', ('eri',))
result_set = table.fetchall()

for result in result_set:
  sql_id = result[0]
  sql_title = result[1]
  sql_name = result[2]

  #sqlのタイトルとhpのタイトルの一致で処理を分岐
  if sql_title != title.string:
    cur.execute("UPDATE blog SET title= ? where name = 'eri'", (title.string,))
  
  twitter_text = sql_name + "さんがブログを更新しました。" + title.string + linktag.get('href')
  print(twitter_text)
# 接続を切断
conn.close()
