# Date: 2/2/23
# Author: Brandon Susini

# %%
import snscrape.modules.twitter as sntwitter
import pandas as pd

# %%
#Users to scrape from
twitter_handles = ["strombone1", "cesc4official"]
#YYYY-MM-DD
start = "2016-01-01"
end = "2023-02-02"

# %%
#Initialize dictionary to hold user keys and dataframes values
all_data = {}
#Loop through the handles and collect their tweets.
for handle in twitter_handles:
    query = "(from:{}) until:{} since:{}".format(handle, end, start)
    tweets = []
    limit = 100
    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        if len(tweets) == limit:
            break
        else:
            tweets.append([tweet.url,
                            tweet.date,
                            tweet.rawContent,
                            tweet.id,
                            tweet.user,
                            tweet.replyCount,
                            tweet.retweetCount,
                            tweet.likeCount,
                            tweet.quoteCount,
                            tweet.conversationId,
                            tweet.lang,
                            tweet.source,
                            tweet.coordinates
                            ])
    df_collected_tweets = pd.DataFrame(tweets, columns=['Url',
                                                        'Date',
                                                        'Content',
                                                        'Id',
                                                        'User',
                                                        'Reply Count',
                                                        'Retweet Count',
                                                        'Like Count',
                                                        'Quote Count',
                                                        'Conversation Id',
                                                        'Language',
                                                        'Source',
                                                        'Coordinates'
                                                        ])
    all_data[handle] = df_collected_tweets


# %%
#Export each table as its own csv file
#Not needed in submission code.
"""
for index, handle in enumerate(all_data.keys()):
    all_data[handle].to_csv(path_or_buf=f"tweets_{handle}.csv")
    print(f"Exported table #{index}")
"""
# %%
#Combine the two tables into a master table and export
#it as a csv file.
df_master = pd.concat([all_data[twitter_handles[0]], all_data[twitter_handles[1]]], ignore_index=True)
df_master.to_csv(path_or_buf=f"all_tweets.csv")



