# -*- coding: utf-8 -*-
import re
import jieba
def distinct_line(doc):
    """对语料进行去重复操作"""
    doc = list(set(doc))
    return doc

def remove_character(text, delete_unchinese=False):
    """去除不需要的字符(或只保留中文)"""
    if delete_unchinese is True:
        # 只保留中文
        text = re.sub(u'[^\u4e00-\u9fa5]', '', text)
    else:
        # 去除特殊字符，只保留汉子，字母、数字
        text = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])","",text)
    return text

def get_stopwords():
    """加载停用词"""
    with open('../../source/stopwords.txt', 'rb') as f:
#        stopwords = [stopword.decode('utf-8').replace('\r\n', '').replace('\r', '').replace('\n', '') for stopword in f.readlines()]
        stopwords = [stopword.decode('utf-8').replace('\r\n', '') for stopword in f.readlines()]
    return  stopwords           

def remove_stopwords(text):
    stopword_list = get_stopwords()
    text = text.split(' ')
    text = [s.strip() for s in text if s not in stopword_list]
    text = ' '.join(text)
    return text

def get_corpus(doc):
    doc = distinct_line(doc)
    corpus = []
    for text in doc:
        text = remove_character(text, delete_unchinese=True)
        # 使用jieba分词
        text = jieba.cut(text)  # 使用jieba分词,得到一个可迭代对象
        text = ' '.join(text)  # 将该可迭代对象用空格拼接成字符串
        corpus.append(text)  # 将切好的词添加到list中
    return corpus

def processing_data(doc):
    """
    参数说明
    -------
    doc: 整个语料list
    
    返回值
    -----
    corpus: 返回处理好的语料list
    """
    corpus = get_corpus(doc)
    doc = []
    for text in corpus:
        text = remove_stopwords(text)
        doc.append(text)
    return doc
    
if __name__=='__main__':
    doc = ['文件 ， 然后 把 要 忽略 的 文件名 填 进去 ， Git 就 会 自动 忽略 ...', 
           '搜 了 半天 网上 的 都是 Python2 的 代码 ， 根本 不能 运行 ， 浪费 半天 时间', 
           '稍微 改 了 一下 2次 编码 整 成 同一 类型 ， 成功 匹配 。 ', 
           '原来 类型 str 和 byte 不是 同一 类型 无法 匹配 ']
    corpus = processing_data(doc)
    print(corpus)
#    text = remove_character(doc[0], delete_unchinese=True)
#    print(text)