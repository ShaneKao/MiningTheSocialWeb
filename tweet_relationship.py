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
q = "Paul George"
count = 10

search_results = twitter_api.search.tweets(q=q, count=count)
statuses = search_results['statuses']
import networkx as nx
import re
g = nx.DiGraph()

def get_rt_sources(tweet):
    rt_patterns = re.compile(r'(RT|via)((?:\b\W*@\w+)+)', re.IGNORECASE)
    return [ source.strip()
             for tuple in rt_patterns.findall(tweet)
                 for source in tuple
                     if source not in ("RT", "via") ]

for status in statuses:
    rt_sources = get_rt_sources(status['text'])
    if not rt_sources: continue
    for rt_source in rt_sources:
        g.add_edge(rt_source, status['user']['screen_name'], {'tweet_id' : status['id']})
            
print nx.info(g)
print g.edges(data=True)[0]

print sorted(nx.degree(g).values())
