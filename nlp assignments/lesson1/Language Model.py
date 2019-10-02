# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 18:14:02 2019

@author: cli
"""

#Language Model
corpus = 'article_9k.txt'
FILE = open(corpus, encoding='UTF-8').read()

import jieba
max_length = 5000000
sub_file = FILE[:max_length]
TOKENS = list(jieba.cut(sub_file))

from collections import Counter
words_count = Counter(TOKENS)
_2_gram_words = [TOKENS[i] + TOKENS[i+1] for i in range(len(TOKENS)-1)]
_2_gram_word_counts = Counter(_2_gram_words)

def get_gram_count(word, wc):
    if word in wc: return wc[word]/len(wc)
    else:
        return wc.most_common()[-1][-1]/len(wc)

def two_gram_model(sentence):
    stoken = list(jieba.cut(sentence))
    probability = 1 
    for i in range(len(stoken)-1):
        word = stoken[i]
        next_word = stoken[i+1]
        _two_gram_c = get_gram_count(word+next_word, _2_gram_word_counts)
        _one_gram_c = get_gram_count(next_word, words_count)
        pro = _two_gram_c / _one_gram_c
        probability *= pro
    return probability

print(two_gram_model('我是神仙'))
print(two_gram_model('好好学习天天向上'))