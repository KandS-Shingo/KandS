import twitter
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


auth = twitter.OAuth(consumer_key= config.CONSUMER_KEY,
                     consumer_secret= config.CONSUMER_SECRET,
                     token= = config.ACCESS_TOKEN,
                     token_secret== config.ACCESS_TOKEN_SECRET)

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
