# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 10:47:38 2019

@author: cli
"""
import random

def generate(grammar_rule, target):
    if target in grammar_rule:
        candidates = grammar_rule[target]
        candidate = random.choice(candidates)
        return ''.join(generate(grammar_rule, target=c.strip()) for c in candidate.split())
    else:
        return target
    
def generate_say(grammar_str: str, target, stmt_split='=', or_split='|'):
    rules = dict()
    for line in grammar_str.split('\n'):
        if not line:continue
        stmt, expr = line.split(stmt_split)
        rules[stmt.strip()] = expr.split(or_split)
    generated = generate(rules, target=target)
    return generated

guest = """
guest = 自己 寻找 活动
自己 = 我 | 俺 | 我们 
寻找 = 看看 | 找找 | 想做点 | 问问
活动 = 咨询 | 了解 | 投保
"""

host = """
host = 寒暄 报数 询问 业务相关 结尾 
报数 = 我是 数字 号 ,
数字 = 单个数字 | 数字 单个数字 
单个数字 = 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 
寒暄 = 称谓 打招呼 | 打招呼
称谓 = 人称 ,
人称 = 先生 | 女士 | 小朋友
打招呼 = 你好 | 您好 
询问 = 请问你要 | 您需要
业务相关 = 投保 具体业务
投保 = 咨询 | 购买
具体业务 = 汽车险 | 意外险 | 财产险 | 特殊险
结尾 = 吗？| 如何？ | 行不？
"""
#print(generate_say(host, 'host'))
#print(generate_say(guest,'guest'))


def generate_n(grammar_str: str, target, n : int):
    sentences = list()
    for i in range(n):
        sentences.append(generate_say(grammar_str, target))
    return sentences
        
        
corpus = 'F:/BaiduNetdiskDownload/ai px/nlp课程/lesson 1/train.txt'
FILE = open(corpus, encoding='UTF-8').read()
import jieba
TOKENS = list(jieba.cut(FILE))
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

def generate_best(grammar_str: str, target: str, n : int):
    result = list()
    sens = generate_n(grammar_str,target,5)
    for sen in sens:
        result.append([sen, two_gram_model(sen)])
    result_sorted = sorted(result, key=lambda x: x[1], reverse=True)
    return result_sorted[0][0]
    
print(generate_best(host,'host',5))
print(generate_best(guest,'guest',4))