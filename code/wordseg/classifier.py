# -*- coding: utf-8 -*-
import pandas as pd
from processings import remove_character, processing_data
from extractors import get_TF
import jieba
import numpy as np
import time

def get_data():
    data = pd.read_csv('../../source/content.txt', sep='\t', header=None, names=['url', 'content', 'description'])
    data = data[data['content']!='NoSearchResult']
    data.fillna(0, inplace=True)
    data.reset_index(drop=True, inplace=True)
    contents = data['content']
    descriptions = data['description']
    doc = contents.astype('str') + descriptions.astype('str')
    doc = doc.values.tolist()
#    doc = doc[:2000]
    return doc

def get_corpus(doc):
    corpus = []
    for text in doc:
        text = remove_character(text, delete_unchinese=True)
        # 使用jieba分词
        text = jieba.cut(text)  # 使用jieba分词,得到一个可迭代对象
        text = ' '.join(text)  # 将该可迭代对象用空格拼接成字符串
        corpus.append(text)  # 将切好的词添加到list中
    return corpus

def get_doc_TF(corpus):
    """获取整个语料库的高频词汇"""
    doc = []
    for words in corpus:
        words = words.split(' ')
        for word in words:
            doc.append(word)
    doc = np.array(doc)
    tf_words = get_TF(doc, topK=100)
    return tf_words

def main():
    start_time = time.time()
    # 获取原始语料
    doc = get_data()
    # 将原始语料进行去特殊字符处理
#    corpus = get_corpus(doc)
    # 对分词后的语料进行去停用词等操作
    corpus = processing_data(doc)
    # 获取整篇文档的高频词汇
    tf_words = get_doc_TF(corpus)
    print(tf_words)
    end_time = time.time()
    cost_time = end_time - start_time
    print('共计花费 %s 秒' % round(cost_time, 2))
    
if __name__=='__main__':
    main()