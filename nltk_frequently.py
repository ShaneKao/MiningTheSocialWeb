# -*- coding: utf-8 -*-
import twitter
CONSUMER_KEY = 'UrgjuFOpYdQ3gadtcdYAXm1Jt'
CONSUMER_SECRET ='DjHsX0W7W2b3cpxpBWpKfSwuCrx8EuBmjk4NKnVX5uzMowFhha'
OAUTH_TOKEN = '2590693668-swLBxY8iKn1onlEVrKAnbKJjAfQPJiYl6gNHRRm'
OAUTH_TOKEN_SECRET = '4Fmm7zwv96Y6QwOaChbIIjXGSMcvVt8mQQckzpbq6mxSW'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(domain='api.twitter.com', 
                              api_version='1.1',
                              auth=auth
                             )
q = "馬英九"
count = 100

search_results = twitter_api.search.tweets(q=q, count=count)
statuses = search_results['statuses']
for _ in range(5): 
    try:
        next_results = search_results['search_metadata']['next_results']
    except KeyError as e: 
        break

kwargs = dict([ kv.split('=') for kv in next_results[1:].split("&") ]) 
search_results = twitter_api.search.tweets(**kwargs)
statuses += search_results['statuses']
import json
# print json.dumps(statuses[0:2], indent=1,ensure_ascii=False)


tweets = [ status['text'] for status in statuses ]

words = []
for t in tweets:
    words += [ w for w in t.split() ]



import nltk

freq_dist = nltk.FreqDist(words)
print(freq_dist.values()) 
print(freq_dist.keys())

