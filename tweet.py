import tweepy
import time


# authenticate user
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)

api = tweepy.API(auth)


# BOT 1 - TESTING : print timeline details, my account details
public_tweets = api.home_timeline()
# prints tweets from home timeline
for tweet in public_tweets:
    print(tweet.text)
    
user = api.me()
# print my name
print(user.name)
#print my twitter handle
print(user.screen_name)
#print follower count
print(user.follower_count)

# func to handle request limit from Twitte
def limit_handler(cursor):
  while True:
    #generator
    yield cursor.next()
  # pause if you hit rate limit
  except tweepy.RateLimitError:
    time.sleep(500)

# BOT 2 - GENEROUS BOT: follow back whoever follows me
#use tweepy's cursor - can be used to paginate for any API methods that support pagination
for follower in  limit_handler(tweepy.Cursor(api.followers).items()):
  # print all followers
  print(follower.name)
  
  # follow back a follower if they have the same name as me
  if follower.name == 'Shriya':
    follower.follow()
  
  # follow back if they have followers > 100
  if follower.followers_count > 100:
    follower.follow()
    

# BOT 3 - Narcissist Bot - like tweets that contain the search word

search_str = "Python"
numOfTweets = 2

for tweet in tweepy.Cursor(api.search, search_str).items(numOfTweets):
  try:
    tweet.favorite()
    print('I liked the Tweet')
  except tweepy.TweepError as e:
    print(e.reason)
  except StopIteration:
    break
  
 #retweet the post
   try:
    tweet.retweet()
    print('I liked the Tweet')
  except tweepy.TweepError as e:
    print(e.reason)
  except StopIteration:
    break
