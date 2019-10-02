# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 18:12:51 2019

@author: cli
"""

#Sentence Generation System Using Syntax Tree
say = '''
sentence = 主语 | 主语 谓语 | 主语 谓语 宾语
主语 = 你 | 我 | 他 | 她
谓语 = 喜欢 | 讨厌 | 害怕 | 搞定 | 征服
宾语 = 你 | 猪 | 狗 | 她 | 傻逼 
'''
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

print(generate_say(say, 'sentence'))