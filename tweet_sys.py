import json
from requests_oauthlib import OAuth1Session
import os
from os.path import join, dirname
from dotenv import load_dotenv

class Tweet_sys:
  def main(self,tweet_content):

    #ここにKeyとToken
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    API_KEY = os.environ.get("API_KEY")
    API_KEY_SECRET = os.environ.get("API_KEY_SECRET")
    ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
    ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")

    twitter = OAuth1Session(API_KEY, API_KEY_SECRET,ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    url = "https://api.twitter.com/1.1/statuses/update.json"

    # tweet = self.tweet_content(tweet_content1))  # ツイート内容
    tweet = tweet_content

    params = {"status": tweet}

    req = twitter.post(url, params=params)  # ここでツイート

    if req.status_code == 200:  # 成功
        print("Succeed!")
    else:  # エラー
        print("ERROR : %d" % req.status_code)
  
    # def tweet_content(self, tweet_content1)):
    # return "Pythonからのテストツイートです\r改行する\r\n改行\n改行"
    

