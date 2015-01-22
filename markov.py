# Notice here, we're explicitly nesting data structures, using a tuple as a key in a dictionary, and a list as the value.

#!/usr/bin/env python

import sys

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    # iterate through list word-by-word
    key_list = []
    for i in range(len(corpus)-1):
        key_list = []
        key_list[i] = (corpus[i], corpus[i+1])
        i += 1

#     print key_list
    #create key values from corpus words (all words but last word)
    #keys will be two words
    #values will be a list of words created by going through the text file
    # create dict with 2-word keys -- for word in range list length-1, list[i], list[i+1] // value = make another list of values
   # return {}

# def make_text(chains):
#     """Takes a dictionary of markov chains and returns random text
#     based off an original text."""
#     return "Here's some random text."

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
    print chain_dict
#     random_text = make_text(chain_dict)
#     print random_text

if __name__ == "__main__":
    main()