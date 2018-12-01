import twitter
consumer_key = "YOUR CONSUMER KEY"
consumer_secret = "YOUR CONSUMER SECRET KEY"
acces_token = "YOUR ACCES TOKEN"
acces_secret = "YOUR ACCES TOKEN SECRET"

api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=acces_token,
                  access_token_secret=acces_secret)




tweet = input("What do you wanna write your followers ?: ")
if len(tweet) > 141:
    print("Make sure your tweet not longer than 140 characters!")
else:
    tweet = api.PostUpdate(tweet)
    print("CONGRATS YOU DID IT !")
