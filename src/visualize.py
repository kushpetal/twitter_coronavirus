#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import heapq


# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
hashmap = {}
for k,v in items:
    hashmap[k] = v

top_10 = heapq.nlargest(10, hashmap, key=hashmap.get)
num_tweets = []
for i in top_10:
    num_tweets.append(hashmap[i])

sorted_data = sorted(zip(num_tweets, top_10))
num_tweets, top_10 = zip(*sorted_data)


x = args.input_path.split('.')[1].upper()
key = args.key.split('#')[1]
plt.bar(top_10, num_tweets)
plt.suptitle(f'Number of Tweets by {x}')
plt.savefig(f'{key}_tweets_by_{x.lower()}.png')


