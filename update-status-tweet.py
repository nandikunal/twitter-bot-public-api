import requests as rq
import tweepy
import random
import time
import os

# Post Tweet
# client = tweepy.Client(consumer_key = <consumer_key>,
#                        consumer_secret = <consumer_secret>,
#                        access_token = <access_token>,
#                        access_token_secret = <access_token_secret>)

# response = client.create_tweet(text='Hello World! from API')
# print(response)

filename = 'upload_pic.jpg'

def tweet_message():
    consumer_key = '<consumer_key>'
    consumer_secret = '<consumer_secret>'
    access_token = '<access_token>'
    access_token_secret = '<access_token_secret>'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    request_string = rq.get("https://api.thedogapi.com/v1/breeds").json()
    val = random.randrange(len(request_string))
    pic_url = request_string[val]["image"]["url"]
    name = request_string[val]["name"]
    pic_name = name.replace(" ", "_")

    request = rq.get(pic_url, stream=True)
    message = "#pets #dogs #DogsofTwittter #lovedogs #{}".format(pic_name)

    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)
        response = api.update_status_with_media(message, filename)
        os.remove(filename)
    else:
        print("Unable to download image")

    print(response)

def main():
    while True:
        tweet_message()
        time.sleep(3600)

if __name__ == "__main__":
    main()
