import tweepy
import time
consumer_key="zgniYqESN5XazgovSmVnaXme3"
consumer_secret="NxWbNExEdjNK8PHjGNbUwoxI73tDP9iAES1za6jsAWt8koSJoD"
access_token="1423720008-Zks50sKy6KaQhCvpbyKy8K51WJxk6rGQbo0futz"
access_token_secret="KKJZ4ia18kvOCSb1zTuepVmS59bioHaMfonY6BZhxS4qn"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
ids = []
user=raw_input("enter the user screen name")
for page in tweepy.Cursor(api.friends_ids, screen_name=user).pages():
    ids.extend(page)
    time.sleep(6)
topics=raw_input("what you want to know about").split()
for friends in ids :
     user = api.get_user(friends)
     print user.name
     for i in range(1,17):
   
      status=api.user_timeline(friends,count=160,page=i)
      for tweet in status :
         for s in topics:
            if " "+s.lower()+" " in (tweet.text.lower()):
                    print tweet.text
