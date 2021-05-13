import tweepy
import re
import emoji
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
file = open("pfizer_hk2.txt","w")
sia = SentimentIntensityAnalyzer()
words = set(nltk.corpus.words.words())
def cleaner(tweet):
    tweet = re.sub("@[A-Za-z0-9]+","",tweet) #Remove @ sign
    tweet = re.sub(r"(?:\@|http?\://|https?\://|www)\S+", "", tweet) #Remove http links
    tweet = " ".join(tweet.split())
    tweet = ''.join(c for c in tweet if c not in emoji.UNICODE_EMOJI) #Remove Emojis
    tweet = tweet.replace("#", "").replace("_", " ") #Remove hashtag sign but keep the text
    # tweet = " ".join(w for w in nltk.wordpunct_tokenize(tweet) \
    #      if w.lower() in words or not w.isalpha())
    return tweet

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        if status.place:
            print(str("time: ")+str(status.created_at)+"\n")
            print(str("names: ") +str(status.user.name.encode('utf-8')) + " " + str(status.user.screen_name.encode('utf-8'))+"\n")
            print('place:'+ str(status.place.full_name.encode('utf-8'))+"\n")
            print(str(status.text))
            print("\n")
            print('in place')
        if status.coordinates:

            print(str("time: ")+str(status.created_at)+"\n")
            print(str("names: ") +str(status.user.name) + " " + str(status.user.screen_name.encode('utf-8'))+"\n")
            print('coordinates:'+ str(status.coordinates)+"\n")
            print(str(status.text.encode))
            print("\n")
            print('in coords')
        #print(status.user.location)




# Authenticate to Twitter
auth = tweepy.OAuthHandler("YzrrCb2NcLgujZmlBkqzAKjvp", "I9kvBWtTPt2IC1xLbhhOXCbRRHOOUO8Ad3D9ibYFvWFoJSYDrm")
auth.set_access_token("1019960140496240640-5VpQDLpVW5edLJ5Ba31t83EZCsfvW1", "9alf36XNJj1Z5Vd05fDx8kDCbJIiClTPATR5bM69yp3QN")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)

#Stream
# myStreamListener = MyStreamListener()
# myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
# myStream.filter(track=['vaccine',"#COVIDVaccine","covid vaccine","Covid vaccine"],locations=[113.7512446747,22.1451403318,114.5114990503,22.6205622006])
search_words = "pfizer -filter:retweets"
date_since = "2020-11-15"
date_until = "2021-05-08"
geo='22.396427,114.109497,60km' #hk
#geo='31.046051,34.851612,60km' #israel
tweets = tweepy.Cursor(api.search,
              q=search_words,
              lang="en",
              full_text = True,
              since=date_since,
              until=date_until,
              geocode = geo).items(30)

results = [status._json for status in tweepy.Cursor(api.search,
                tweet_mode='extended',
              q=search_words,
              lang="en",
              full_text = True,
              since=date_since,
              geocode = geo).items(1000)]


for result in results:
    file.write(str(result["created_at"])+"\t")
    cleaned = cleaner(result["full_text"])
    file.write(str(sia.polarity_scores(cleaned)))
    file.write("\t")
    file.write(str(cleaned.encode('utf-8')))
    file.write("\n")
#
# file.write("\n\n\n\n\n\n")

# results = [status._json for status in tweepy.Cursor(api.search,
#                 tweet_mode='extended',
#               q=search_words,
#               lang="en",
#               full_text = True,
#               since=date_since,
#               until ="2021-04-21",
#               geocode = geo).items(400)]
#
#
# for result in results:
#     file.write(str(result["created_at"])+"\t")
#     cleaned = cleaner(result["full_text"])
#     file.write(str(sia.polarity_scores(cleaned)))
#     file.write("\t")
#     file.write(str(cleaned.encode('utf-8')))
#     file.write("\n")
