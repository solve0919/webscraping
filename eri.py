import requests
from bs4 import BeautifulSoup
import re
import sqlite3
import schedule
import time
import twitter
import json
from requests_oauthlib import OAuth1Session
import tweet_sys

class Eri:
  def eridata(self,username):
    username = "eri"
    urlName = "https://erihitomi.com/"
    url = requests.get(urlName)
    soup = BeautifulSoup(url.content, "html.parser")
    # 最新のブログタイトルを取得
    title = soup.select_one("h2")
    # 最新のブログurlを取得
    cardlink = soup.select_one("[class='cardtype__article-info']")
    linktag = cardlink.find_previous("a")

    # dbからデータを取得
    table = cur.execute('select * from blog where name =? ', (username,))
    result_set = table.fetchall()

    for result in result_set:
      sql_id = result[0]
      sql_title = result[1]
      sql_name = result[2]

    twitter_text = sql_name + "さんがブログを更新しました。\n" + title.string + linktag.get('href')

    tweet = tweet_sys.Tweet_sys()
    tweet.main(twitter_text) #つぶやく

    #sqlのタイトルとhpのタイトルの一致で処理を分岐
    if sql_title != title.string:
      cur.execute("UPDATE blog SET title= ? where name = 'eri'", (title.string,))
      api.PostUpdate(twitter_text)


# 接続を切断
conn.close()

# def main():
#   schedule.every(1).minutes.do(job)

#   while True:
#       schedule.run_pending()
#       time.sleep(1)
