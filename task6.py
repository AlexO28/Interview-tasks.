# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 23:32:19 2022

@author: Семья
"""

# Sample Input ["eat", "tea", "tan", "ate", "nat", "bat"]
# Sample Output [ ["ate", "eat", "tea"], ["nat", "tan"], ["bat"] ]

import collections


def group_words(words):
    words_dict = collections.defaultdict(list)
    for word in words:
        if (len(words_dict.keys()) == 0):
            words_dict[word].append(word)
        else:    
            found = False
            for key in words_dict.keys():
                if check(word, key):
                    words_dict[key].append(word)
                    found = True
            if (not found):
                words_dict[word].append(word)
    resList = []
    for key in words_dict.keys():
        resList.append(words_dict[key])
    return(resList)


def check(word1, word2):
   word1 = ''.join(sorted(word1))
   word2 = ''.join(sorted(word2))
   return(word1 == word2)