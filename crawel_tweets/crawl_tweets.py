import tweepy
import math
import json
import time
import sys

consumer_key = 'rAr4v8Znj20Yvzgk7k5zXQQ4F'
consumer_key_secret = 'EqfAVWH5lIvbnfIu9gSTFkJPM4a2X0tlpJjV8NZFK3TOdCpGB9'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAOk4bwEAAAAAl28%2FIuPszW5A9NySsBir4ZRfCvo%3DQvOGVBW3jF1NPD2YmJcb4cfOLiauEZlxqb91yaBK4t1hhZmWQq'
access_token = '1517815216582848512-5Nb9mndTHNcR90xPzEjR5BbGIbNenJ'
access_token_secret = 'hDDDakualeH66yFYLv5zUkAXZ6oiAZx80epVVRd9shwyA'


def get_ID_list(txtPath):
    ID_lists = []
    with open(txtPath, 'r') as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip('\n')
        ID_lists.append(line.split(','))
    return ID_lists


def retrive_tweets_list(filePath, tweet_fields_list:list, user_fields_list: list):
    set_name = filePath.split("/")[-1].split(".")[-3]
    client = tweepy.Client(bearer_token=bearer_token)
    ID_lists = get_ID_list(filePath)
    ID_lists_flatten = [i for row in ID_lists for i in row]
    ID_lists_100 = [ID_lists_flatten[100 * i:100 * (i + 1)] for i in range(math.ceil(len(ID_lists_flatten) / 100))]

    tweets_list = []
    counter = 0
    for ID_list in ID_lists_100:
        tl = []
        # tweets = client.get_tweets(ids=ID_list, tweet_fields=tweet_fields_list, user_fields=user_fields_list)
        while True:
            try:
                print("Try " + str(counter) + " IDlist, " + str(math.ceil(len(ID_lists_flatten) / 100) - counter)
                      +" remains")
                tweets = client.get_tweets(ids=ID_list, tweet_fields=tweet_fields_list, user_fields=user_fields_list)
            except tweepy.errors.TooManyRequests:
                print("Request failed, ")
                time.sleep(60)
                print("After 1 min, Retry:")
                continue
            break
        counter += 1
        if tweets.data is None:
            tweets_list.append(tl)
            continue
        for tweet in tweets.data:
            tl.append(tweet)
            with open("../project-data/" + set_name + ".data-object/" + str(tweet.id) + ".json", "w") as outfile:
                json.dump(tweet.data, outfile)
        tweets_list.append(tl)
    return tweets_list


if __name__ == "__main__":
    filePath = '../project-data/' + str(sys.argv[1]) + '.data.txt'
    tweet_fields_list = ['author_id', 'conversation_id', 'created_at', 'entities', 'geo', 'id',
                         'in_reply_to_user_id', 'lang', 'source', 'text']
    user_fields_list = ['created_at', 'description', 'entities', 'id', 'location', 'name', 'pinned_tweet_id',
                        'protected', 'public_metrics', 'url', 'username', 'verified', 'withheld']
    temp_data = retrive_tweets_list(filePath, tweet_fields_list, user_fields_list)
    print('finish')
