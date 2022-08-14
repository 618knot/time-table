def getMenu():
    from urllib import response
    import tweepy
    import requests
    import os
    from dotenv import load_dotenv

    load_dotenv()
    # 認証に必要なキーとトークン
    API_KEY = os.environ['API_KEY']
    API_SECRET = os.environ['API_SECRET']
    ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
    ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

    # APIの認証
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)




    for tweet in api.search_tweets(q='"今週のメニュー" from:@CISTcafe'):
        imageUrl = tweet.extended_entities['media'][0]['media_url']
        
        response = requests.get(imageUrl)
        image = response.content

        fileName = 'menu'
        fileNameJpg = fileName + '.jpg'

        with open(fileNameJpg, "wb")as f:
            f.write(image)
        
        # with open(fileName + '.pdf', "wb")as f:
        #     f.write(img2pdf.convert(fileNameJpg))

        print(imageUrl)
        print(tweet.text)
        print(tweet.created_at)
        print("=============================")