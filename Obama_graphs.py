
import csv
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import dates as mpl_dates
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta



plt.style.use('seaborn')

def read_twitter_data(file_path):
    tweet_data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)  # Read the header line

        for row in reader:
            tweet = {
                # 'user_screen': row[0],
                # 'username': row[1],
                'timestamp': datetime.strptime(row[2], "%m/%d/%Y"),
                # 'text': row[3],
                'tweet_embedded_text': row[4],
                # 'emojis': row[5],
                'comments': int(row[6]),
                'retweets': int(row[7]),
                'favorites': int(row[8]),
               
            }
            tweet_data.append(tweet)

    return tweet_data

#File name
file_path = 'obama_cleaned_data_final1.csv'
tweet_data = read_twitter_data(file_path)

##FAVOURTIES FUNCTION_____________________________________________________________
# def plot_favorites_timegraph(tweet_data, interval) :
#     start_date = min(tweet['timestamp'] for tweet in tweet_data)
#     end_date = max(tweet['timestamp'] for tweet in tweet_data)

#     if interval == 'daily':
#         delta = relativedelta(days=1)
#         xlabel_format = "%m/%d"
#     elif interval == 'monthly':
#         start_date = start_date.replace(day=1)
#         delta = relativedelta(months=1)
#         for tweet in tweet_data:
#             tweet['timestamp'] = tweet['timestamp'].replace(day=1) 
#         xlabel_format = "%m/%d"
#     elif interval == 'yearly':
#         start_date = start_date.replace(month=1, day=1)
#         delta = relativedelta(years=1)
#         for tweet in tweet_data:
#             tweet['timestamp'] = tweet['timestamp'].replace(month=1, day=1) 
#         xlabel_format = "%m/%Y"
#     else:
#         raise ValueError("Invalid interval. Please choose 'daily', 'weekly', or 'monthly'.")

#     likes_per_day = {}

#     ##Initialize dictionary 
#     current_date = start_date
#     while current_date <= end_date:
#         likes_per_day[current_date] = 0
#         current_date += delta

#     for tweet in tweet_data:
#         likes_per_day[tweet['timestamp']] += tweet['favorites']

#     dates = list(likes_per_day.keys())
#     counts = list(likes_per_day.values())

#  #RETWEETS FUNCTION__________________________________________________________________
# def plot_retweets_timegraph(tweet_data, interval) :
#     start_date = min(tweet['timestamp'] for tweet in tweet_data)
#     end_date = max(tweet['timestamp'] for tweet in tweet_data)

#     if interval == 'daily':
#         delta = relativedelta(days=1)
#         xlabel_format = "%m/%d"
#     elif interval == 'monthly':
#         start_date = start_date.replace(day=1)
#         delta = relativedelta(months=1)
#         for tweet in tweet_data:
#             tweet['timestamp'] = tweet['timestamp'].replace(day=1) 
#         xlabel_format = "%m/%d"
#     elif interval == 'yearly':
#         start_date = start_date.replace(month=1, day=1)
#         delta = relativedelta(years=1)
#         for tweet in tweet_data:
#             tweet['timestamp'] = tweet['timestamp'].replace(month=1, day=1) 
#         xlabel_format = "%m/%Y"
#     else:
#         raise ValueError("Invalid interval. Please choose 'daily', 'weekly', or 'monthly'.")
    
#     retweets_per_day = {}

#     ##Initialize dictionary 
#     current_date = start_date
#     while current_date <= end_date:
#         retweets_per_day[current_date] = 0
#         current_date += delta

#     for tweet in tweet_data:
#         retweets_per_day[tweet['timestamp']] += tweet['retweets']

#     dates = list(retweets_per_day.keys())
#     counts = list(retweets_per_day.values())

 #COMMENTS FUNCTION__________________________________________________________________
def plot_comments_timegraph(tweet_data, interval) :
    start_date = min(tweet['timestamp'] for tweet in tweet_data)
    end_date = max(tweet['timestamp'] for tweet in tweet_data)

    if interval == 'daily':
        delta = relativedelta(days=1)
        xlabel_format = "%m/%d"
    elif interval == 'monthly':
        start_date = start_date.replace(day=1)
        delta = relativedelta(months=1)
        for tweet in tweet_data:
            tweet['timestamp'] = tweet['timestamp'].replace(day=1) 
        xlabel_format = "%m/%d"
    elif interval == 'yearly':
        start_date = start_date.replace(month=1, day=1)
        delta = relativedelta(years=1)
        for tweet in tweet_data:
            tweet['timestamp'] = tweet['timestamp'].replace(month=1, day=1) 
        xlabel_format = "%m/%Y"
    else:
        raise ValueError("Invalid interval. Please choose 'daily', 'weekly', or 'monthly'.")
    
    comments_per_day = {}

    ##Initialize dictionary 
    current_date = start_date
    while current_date <= end_date:
        comments_per_day[current_date] = 0
        current_date += delta

    for tweet in tweet_data:
        comments_per_day[tweet['timestamp']] += tweet['comments']

    dates = list(comments_per_day.keys())
    counts = list(comments_per_day.values())



# # Favourites Graph--------------------------------------------------------------------
#     plt.plot(dates, counts, marker='o')
#     plt.xlabel('Date')
#     plt.ylabel('Favorites Count')
#     plt.title(f'Number of Favorites ({interval.capitalize()})')
#     plt.xticks(rotation=45)
#     plt.tight_layout()
#     plt.show()

# #Retweets Graph----------------------------------------------------------------------------
#     plt.plot(dates, counts, marker='o')
#     plt.xlabel('Date')
#     plt.ylabel('Retweets Count')
#     plt.title(f'Number of Retweets ({interval.capitalize()})')
#     plt.xticks(rotation=45)
#     plt.tight_layout()
#     plt.show()


#Comments Graph----------------------------------------------------------------------------
    plt.plot(dates, counts, marker='o')
    plt.xlabel('Date')
    plt.ylabel('Comments Count')
    plt.title(f'Number of Comments ({interval.capitalize()})')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()



# # FAVOURITES PLOT--------------------------------------------------------------------
# plot_favorites_timegraph(tweet_data, 'daily')
# plot_favorites_timegraph(tweet_data, 'monthly')
# plot_favorites_timegraph(tweet_data, 'yearly')

# #RETWEETS PLOT---------------------------------------------------------------------------
# plot_retweets_timegraph(tweet_data, 'daily')
# plot_retweets_timegraph(tweet_data, 'monthly')
# plot_retweets_timegraph(tweet_data, 'yearly')

#COMMENTS PLOT---------------------------------------------------------------------------
plot_comments_timegraph(tweet_data, 'daily')
plot_comments_timegraph(tweet_data, 'monthly')
plot_comments_timegraph(tweet_data, 'yearly')