import tweepy
import math

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

def retrive_tweets_list (filePath, tweet_fields_list):
    client = tweepy.Client(bearer_token=bearer_token)
    ID_lists = get_ID_list(filePath)
    ID_lists_flatten = [i for row in ID_lists for i in row]
    ID_lists_100 = [ID_lists_flatten[100*i:100*(i+1)] for i in range(math.ceil(len(ID_lists_flatten)/100))]

    tweets_list = []
    for ID_list in ID_lists_100:
        tl = []
        print(len(ID_list))
        tweets = client.get_tweets(ids=ID_list, tweet_fields=tweet_fields_list)
        if tweets.data == None:
            tweets_list.append(tl)
            continue
        for tweet in tweets.data:
            tl.append(tweet)
        tweets_list.append(tl)
    return tweets_list


if __name__ == "__main__":
    filePath = '../project-data/train.data.txt'
    tweet_fields_list = ['context_annotations','created_at','geo']
    temp_data = retrive_tweets_list(filePath, tweet_fields_list)
    print('finish')















