#!/usr/bin/env python

import sys

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    new_dict = {}
    # iterate through list word-by-word, creating chains
    for index in range(len(corpus) - 2):
        key = (corpus[index], corpus[index + 1])
        new_dict[key] = new_dict.setdefault(key, [])
        new_dict[key].append(corpus[index + 2])
    return new_dict

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    return "Here's some random text."

def main():
    args = sys.argv
    script, path = args
    file_to_parse = open(path)
    final_list = []
    
    for line in file_to_parse:
        separate_line = line.rstrip().split(' ')
        for word in separate_line:
            final_list.append(word)
  
    chain_dict = make_chains(final_list)
    random_text = make_text(chain_dict)
    print random_text

if __name__ == "__main__":
    main()