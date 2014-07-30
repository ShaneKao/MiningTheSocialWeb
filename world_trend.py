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
WORLD_WOE_ID = 1
world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
print world_trends
import json

print json.dumps(world_trends, indent=1)
