import json, config
from requests_oauthlib import OAuth1Session

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS)


url = "https://api.twitter.com/1.1/direct_messages.json"

params = {"count" : 1}

req = twitter.get(url, params = params)

if req.status_code == 200:
    DM_list_json = json.loads(req.text)
    for DM in DM_list_json:
        
        #送信者の名前と、メッセージ内容を取得する
        twit_name = DM['sender_screen_name']
        twit_text = DM['text']
        print(twit_name)
        print(twit_text)

        # 返信する
        url = "https://api.twitter.com/1.1/direct_messages/new.json"
        params ={'screen_name' : twit_name,
                 'text' : twit_text+ " と言ったぞ"}
        
        req = twitter.post(url, params = params)

        if req.status_code != 200:
            print(req.reason)
        
    
else:
    print("ERROR: %d" % req.status_code)

# url = "https://api.twitter.com/1.1/direct_messages/new.json"

# params ={'screen_name' : "eguchishi",
#          'text' : "bello!"}
# req = twitter.post(url, params = params)

# if req.status_code == 200:
#     timeline = json.loads(req.text)  # stringをjson形式で解釈して、辞書配列に変換してくれる
#     for tweet in timeline:
#         print(tweet['user']['name']+'::'+tweet['text'])
#         print(tweet['created_at'])
#         print('----------------------------------------------------')
# else:
#     print("ERROR: %d" % req.status_code)
    
