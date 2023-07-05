import snscrape.modules.twitter as sntwitter
import pandas as pd
import datetime

query = "reverse diabetes lang:en"
limit = 1000
tweets = []

# Set the start and end dates for the search
start_date = datetime.datetime(2011, 1, 1)
end_date = datetime.datetime(2013, 1, 1)

for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f'{query} since:{start_date.date()} until:{end_date.date()}').get_items()):
    if i >= limit:
        break
    else:
        tweets.append([tweet.date, tweet.user.username, tweet.content])
        df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
        
df.to_csv('tweeting.csv')