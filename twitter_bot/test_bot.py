import twitter
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


auth = twitter.OAuth(consumer_key="eOxg5Cfv3BkfVrmUKLQ0psbq8",
consumer_secret="06QXFWEjowmKTGtw7kkDZzLQeQtURGQqQXjC07AXQQLIgOoBl5",
token="933296923817021440-KiieMOOp7x26GRcEJ6KRCJcYeuZClfr",
token_secret="qXcxCDAJmo5C6UQlxwyPIYnkpO26rawmNRl6qpxhSRC8y")

t = twitter.Twitter(auth=auth)

#ツイートのみ
status="this is orasuke!" #投稿するツイート
t.statuses.update(status=status) #Twitterに投稿

#画像付きツイート
# pic=""　#画像を投稿するなら画像のパス
# with open(pic,"rb") as image_file:
#  image_data=image_file.read()
# pic_upload = twitter.Twitter(domain='upload.twitter.com',auth=auth)
# id_img1 = pic_upload.media.upload(media=image_data)["media_id_string"]
# t.statuses.update(status=status,media_ids=",".join([id=img1]))
