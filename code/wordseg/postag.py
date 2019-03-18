# -*- coding: utf-8 -*-
"""词性标注"""
import jieba.posseg as psg
import pandas as pd
from processings import remove_character

def read_data():
    df = pd.read_csv('../../source/content.txt', sep='\t', header=None, names=['url', 'content', 'description'])
    df = df[df['content']!='NoSearchResult']
    df.fillna('0', inplace=True)
    df['doc'] = df['content'] + df['description']
    docs = df['doc'].values.tolist()
    segs = []
    for doc in docs:
        doc = remove_character(doc, delete_unchinese=True)
        segs.append(doc)
    return segs

def pos_tag(text):
    """使用jieba工具进行词性标注"""
    text_list = psg.cut(text)
    text = ' '.join(['{0}/{1}'.format(w, t) for w, t in text_list])
    return text

def main():
    segs = read_data()
    for seg in segs[:10]:
        print(seg)
        seg = pos_tag(seg)
        print(seg)


if __name__=='__main__':
    main()
    
