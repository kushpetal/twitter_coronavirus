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
import pandas as pd

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# store values in hashmap
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
hashmap = {}
for k,v in items:
    hashmap[k] = v

# get top 10 most tweeted countries/locations
top_10 = heapq.nlargest(10, hashmap, key=hashmap.get)
num_tweets = []
for i in top_10:
    num_tweets.append(hashmap[i])

df = pd.DataFrame(
    dict(
        x_axis = top_10,
        y_axis = num_tweets
        )
)

df_sorted = df.sort_values('y_axis')

# build bar chart
x = args.input_path.split('.')[2].upper()
key = args.key.split('#')[1]
plt.bar('x_axis', 'y_axis', data = df_sorted)
plt.suptitle(f'Tweets including "{key}"')
plt.xlabel(f'{x}')
plt.ylabel("COUNT")

# save chart as png file
plt.savefig(f'{key}_tweets_by_{x.lower()}.png')


