#!/usr/bin/env python

import sys
import os
import twitter
from random import choice

TWITTER_CONSUMER_KEY = os.environ['TWITTER_CONSUMER_KEY']
TWITTER_CONSUMER_SECRET = os.environ['TWITTER_CONSUMER_SECRET']
TWITTER_ACCESS_TOKEN = os.environ['TWITTER_ACCESS_TOKEN']
TWITTER_ACCESS_TOKEN_SECRET = os.environ['TWITTER_ACCESS_TOKEN_SECRET']

api = twitter.Api(
    consumer_key=TWITTER_CONSUMER_KEY,
    consumer_secret=TWITTER_CONSUMER_SECRET,
    access_token_key=TWITTER_ACCESS_TOKEN,
    access_token_secret=TWITTER_ACCESS_TOKEN_SECRET
)

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    new_dict = {}
    final_list = []
    
    for line in corpus:
        separate_line = line.rstrip().split(' ')
        for word in separate_line:
            final_list.append(word)
    # iterate through list word-by-word, creating chains
    for index in range(len(final_list) - 2):
        key = (final_list[index], final_list[index + 1])
        new_dict[key] = new_dict.setdefault(key, [])
        new_dict[key].append(final_list[index + 2])
    return new_dict

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    emoticons = [" :)", " <3", " ;)", " 8-)", " o.O", " xo", " ^.^", " :p", " 0:-)", " :(", " -_-", " :D", " :*", " :-#", " :-7", " omg"]
    first_key = choice(chains.keys())
    first_value = choice(chains[first_key])
    new_string = first_key[0] + " " + first_key[1]
    next_key = (first_key[1], first_value)

    while (next_key in chains) and (len(new_string) < 110):   
        current_value = choice(chains[next_key])
        new_string = new_string + " " + next_key[1]
        next_key = (next_key[1], current_value)

    new_string = new_string.lower()
    return new_string + " " + current_value + choice(emoticons)

def main():
    args = sys.argv
    script, path = args
    file_to_parse = open(path)
    chain_dict = make_chains(file_to_parse)
    random_text = make_text(chain_dict)
    status = api.PostUpdate(random_text)

if __name__ == "__main__":
    main()